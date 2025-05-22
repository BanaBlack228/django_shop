
from django.urls import reverse_lazy

from .forms import CategoryCreateForm, ProductCreateFrom
from django.views.generic import (CreateView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView,
                                  ListView,)
from .models import Category,Product

################################### АДМИНКА ###########################################

# Класс для создания новой категории
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'admin_pages/add_category.html'
    success_url = reverse_lazy('staff:categories')


# Класс для просмотра категорий
class CategoryListView(ListView):
    model = Category
    template_name = 'admin_pages/list_category.html'
    context_object_name = 'categories'

# Класс для создания товара
class ProductCrateView(CreateView):
    model = Product
    form_class = ProductCreateFrom
    template_name = 'admin_pages/add_product.html'
    success_url = reverse_lazy ('staff:products')

# Класс для отображения товаров
class ProductListView(ListView):
    model = Product
    template_name = 'admin_pages/list_product.html'
    context_object_name = 'products'

#Класс для отображения информации о товаре
class ProductDetailView(DetailView):
    model = Product
    template_name = 'admin_page/detail_product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'