from django.urls import path
from .views import new_product, product_detail, product_update, product_delate

app_name = 'products'
urlpatterns = [
    path('new', new_product, name='new'),
    path('<int:pk>/detail', product_detail, name='detail'),
    path('<int:pk>/update', product_update, name='update'),
    path('<int:pk>/delate', product_delate, name='delate'),
]
