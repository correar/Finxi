from django.test import TestCase
from django.urls import reverse
#from django.utils.formats import localize
import locale

from .models import Empresa, Categoria, Produto

locale.setlocale(locale.LC_ALL, '')

#def create_categoria(categoria_nome):
#    return Categoria.objects.create(categoria_nome=categoria_nome)

#def create_produto(produto_nome, preco_custo, unidades, total_venda, empresas, categorias)
#    return Produto.objects.create(produto_nome=produto_nome, preco_custo=preco_custo, unidades=unidades, total_venda=total_venda, empresas=empresas,categorias=categorias)

class EmpresaModelTests(TestCase):
    def setUp(self):
        Empresa.objects.create(empresa_nome="Agd20")
        
    def test_empresa(self):
        empresa = Empresa.objects.get(empresa_nome="Agd20")
        return empresa

class CategoriaModelTests(TestCase):
    def setUp(self):
        Categoria.objects.create(categoria_nome="alimentador")

    def test_categoria(self):
        categoria = Categoria.objects.get(categoria_nome="alimentador")
        return categoria

class ProdutoModelTests(TestCase):
    def setUp(self):
        Empresa.objects.create(empresa_nome="Agd20")
        Categoria.objects.create(categoria_nome="alimentador")
        empresa = Empresa.objects.get(empresa_nome="Agd20")
        categoria = Categoria.objects.get(categoria_nome="alimentador")
        produto = Produto.objects.create(produto_nome="ALIMENTADOR BICO SILICONE - ABU01", preco_custo="5.70", unidades="9", total_venda="108.00", categorias=categoria)
        produto.empresas.add(empresa)
    
    def test_produto(self):
        empresa = Empresa.objects.get(empresa_nome="Agd20")
        categoria = Categoria.objects.get(categoria_nome="alimentador")
        produto = Produto.objects.get(produto_nome="ALIMENTADOR BICO SILICONE - ABU01", preco_custo="5.70", unidades="9", total_venda="108.00", categorias=categoria)
        return produto