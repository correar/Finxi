from django.urls import path

from . import views

app_name = 'vendas'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('empresas/', views.EmpresasView.as_view(), name='empresas'),
    path('empresa/', views.EmpresaCreate, name='empresa'),
    path('produtos/', views.ProdutosView.as_view(), name='produtos'),
    path('produto/', views.ProdutoCreate, name='produto'),
]