from django.db import models

class Empresa(models.Model):
    empresa_nome = models.CharField(max_length=200)
    document = models.FileField(upload_to='assets/file/', default='')
    def __str__(self):
        return self.empresa_nome
    def documento(self):
        return self.document

class Categoria(models.Model):
    categoria_nome = models.CharField(max_length=200)
    def __str__(self):
        return self.categoria_nome

class Produto(models.Model):
    produto_nome = models.CharField(max_length=200)
    preco_custo = models.DecimalField(max_digits=11, decimal_places=2)
    unidades = models.IntegerField(default=1)
    total_venda = models.DecimalField(max_digits=11, decimal_places=2)
    empresas = models.ManyToManyField(Empresa)
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.produto_nome




