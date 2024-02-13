from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
# from django.contrib.auth import views as auth_views
from .import views
urlpatterns = [
    path('sign-up/', UserRegisterView.as_view(), name="signup"),
    path('edit-profile/', UserEditView.as_view(), name="edit-profile"),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name = 'Registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name = 'Registration/change-password.html')),
    path('password-success/', views.password_success, name='password-success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='user-profile'),
    path('edit-profile/<int:pk>/page/', EditProfilePageView.as_view(), name='edit-profile-page'),
    path('create-profile/page/', CreateProfilePageView.as_view(), name='create-profile-page'),
    path('fav/<int:id>/', views.add_favourite, name='add-favourite'),
    path('profile/favourites/', views.favourite_list, name='favourite-list'),
]
