from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from Home.models import Profile, Post
# from django.http import HttpResponseRedirect

def favourite_list(request):
    new = Post.objects.filter(favourites = request.user)
    return render(request, 'favourites.html', {'new': new})
   

def add_favourite(request, id):
    post = get_object_or_404(Post, id=id)
    if post.favourites.filter(id = request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'Registration/create-profile-page.html'
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'Registration/edit-profile-page.html'
    # success_url = reverse_lazy('user-profile')
    success_url = reverse_lazy('home')
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url']

class ShowProfilePageView(DetailView):
    model = Profile 
    template_name = 'Registration/user-profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])

        context["page_user"] = page_user
        return context

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('password-success')

def password_success(request):
    return render(request, 'Registration/password-success.html', {})

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'Registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'Registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user