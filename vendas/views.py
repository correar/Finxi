from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.db.models import Avg, Sum, Q

from .models import Empresa, Produto, Categoria
from .forms import EmpresaForm, ProdutoForm, read_upload_file


class IndexView(generic.ListView):
    model = Produto
    template_name = 'vendas/index.html'

class EmpresasView(generic.ListView):
    model = Empresa
    template_name = 'empresas/empresas.html'
    context_object_name = 'empresas'
    def get_queryset(self):
        return Empresa.objects.all()

def EmpresaCreate(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST or None, request.FILES)

        if form.is_valid():
            form.save()
            e = Empresa.objects.last()
            read_upload_file(e.documento())
            return redirect('/empresas')
    else:
        form = EmpresaForm()    
    return render(request, 'empresas/cadastro_empresa.html', {'form':form})
    
class ProdutosView(generic.ListView):
    model = Produto
    template_name = 'produtos/produtos.html'
    context_object_name = 'produtos'
    def get_queryset(self):
        result = Produto.objects.all()
        query = self.request.GET.get('q')
        if query:
            result = Produto.objects.filter(
                Q(produto_nome__icontains=query) |
                Q(categorias__categoria_nome__icontains=query) |
                Q(empresas__empresa_nome__icontains=query)
            )
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        if query:
            total_venda = Produto.objects.filter(
                Q(produto_nome__icontains=query) |
                Q(categorias__categoria_nome__icontains=query) |
                Q(empresas__empresa_nome__icontains=query)
            ).aggregate(Sum('total_venda'))
            media_venda = Produto.objects.filter(
                Q(produto_nome__icontains=query) |
                Q(categorias__categoria_nome__icontains=query) |
                Q(empresas__empresa_nome__icontains=query)
            ).aggregate(Avg('unidades'))
        else:
            total_venda = Produto.objects.all().aggregate(Sum('total_venda'))
            media_venda = Produto.objects.all().aggregate(Avg('unidades'))
        context['total'] = total_venda
        context['media'] = media_venda
        return context

def ProdutoCreate(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            handle_upload_file(request.FILES['file'])
            return redirect('/produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/cadastro_produto.html', {'form':form})