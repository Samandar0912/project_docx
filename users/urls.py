from django.urls import path
from .views import SignupView, ProfileView, UpdateProfileView, logout_view

app_name = 'users'
urlpatterns = [
    path('signup/',SignupView.as_view(), name='signup'),
    path('profile/<str:username>',ProfileView.as_view(), name='profile'),
    path('update',UpdateProfileView.as_view(), name='update'),
    path('logout/', logout_view, name='logout'),
]
