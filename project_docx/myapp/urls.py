from django.urls import path
from .views import IndexView, ModelDetailView, categoryFilter, articleFilter

app_name = 'main' #=> Asosiy app
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('<str:category_name>/category', ModelDetailView.as_view(), name='detail'),
    path('category/<int:pk>',categoryFilter, name='category_list'),
    path('science/<int:pk>',articleFilter, name='article_list'),
    
]
