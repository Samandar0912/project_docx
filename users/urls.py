from django.urls import path
from .views import SignupView, ProfileView

app_name = 'users'
urlpatterns = [
    path('signup/',SignupView.as_view(), name='signup'),
    path('profile/<str:username>',ProfileView.as_view(), name='profile'),
]
