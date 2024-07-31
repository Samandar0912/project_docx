from django.urls import path
from .views import IndexView

app_name = 'main' #=> Asosiy app
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    
]
