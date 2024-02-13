from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# from django.views.decorators.clickjacking import xframe_options_sameorigin
# Create your views here.
# def home(request):
#     return render(request, 'index.html', {})

def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = "index.html"
    ordering = ['-date_published']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category = cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})

def searchPost(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(caption__contains = searched)
        return render(request, 'search_post.html', {'searched': searched, 'posts': posts})
    else:
        return render(request, 'search_post.html', {})

class PostDetailView(DetailView):
    model = Post
    template_name = "detail.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)

        things = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = things.total_likes()

        liked = False
        if things.likes.filter(id = self.request.user.id):
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        # context["form"] = self.form
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # fields = '__all__'
    # fields = ('pic','caption','author')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    # success_url = reverse_lazy('add-comment')
    def get_success_url(self):
        # return reverse_lazy('detail', kwargs={'pk': self.kwargs['pk']})
        return reverse_lazy('add-comment', kwargs={'pk': self.kwargs['pk']})

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = "add_category.html"
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "edit_post.html"
    # fields = ('pic','caption')

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')
