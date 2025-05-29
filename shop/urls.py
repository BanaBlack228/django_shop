from django.urls import path

from shop.views import ProductsByCategoryListView

app_name = 'shop'
urlpatterns = [
    path('products/<slug:slug>/', ProductsByCategoryListView.as_view(), name='index_category'),
    path('', ProductsByCategoryListView.as_view(), name='index'),
]
