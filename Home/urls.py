from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView, AddCommentView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="detail"),
    path('upload/', AddPostView.as_view(), name="add"),
    path('add-category/', AddCategoryView.as_view(), name="add-category"),
    path('edit/<int:pk>/', UpdatePostView.as_view(), name="edit"),
    path('delete/<int:pk>/', DeletePostView.as_view(), name="delete"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('like/<int:pk>/', LikeView, name="like"),
    path('post/<int:pk>/add_comment', AddCommentView.as_view(), name="add-comment"),
    path('search-post/', views.searchPost, name="search-post"),
    # path('add-comment/<int:pk>/', TemplateView.as_view(template_name = 'add-comment.html'), name = 'commenting'),
]
