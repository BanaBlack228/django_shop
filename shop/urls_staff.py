

from django.urls import path
from .views import CategoryCreateView, CategoryListView, ProductCrateView, ProductListView, ProductDetailView

app_name = 'staff'
urlpatterns = [
    path('categories/add/', CategoryCreateView.as_view(), name='category_add'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/add/', ProductCrateView.as_view(),name='products_add'),
    path('products/', ProductListView.as_view(), name='products'),

]

