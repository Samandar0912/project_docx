from django.urls import path
from .views import IndexView, ModelDetailView

app_name = 'main' #=> Asosiy app
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<str:category_name>/category', ModelDetailView.as_view(), name='detail'),
    
]
