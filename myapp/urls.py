from django.urls import path
from .views import IndexView, ArticleListView, CategoryFilterView

app_name = 'main' #=> Asosiy app
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/<int:pk>',CategoryFilterView.as_view(), name='categoryFilter'),
    path('science/<int:pk>',ArticleListView.as_view(), name='article_list'),
    
]
