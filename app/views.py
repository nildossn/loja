from django.shortcuts import render, redirect
from app.forms import ProdutoForm, CategoriaForm
from app.models import Produto, Categoria

# Create your views here.
def home(request):
    data = {}
    data['db'] = Produto.objects.all()
    return render(request, 'index.html', data)

# Formulário para produto
def form(request):
    data = {}
    data['form'] = ProdutoForm()
    return render(request, 'form.html', data)

# Formulário para categoria
def form2(request):
    data = {}
    data['form2'] = CategoriaForm()
    return render(request, 'form2.html', data)

def create(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def create2(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista')

def view(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    data['form'] = ProdutoForm(instance=data['db'])
    return render(request, 'form.html', data)

def edit2(request, pk):
    data = {}
    data['ls'] = Categoria.objects.get(pk=pk)
    data['form2'] = CategoriaForm(instance=data['ls'])
    return render(request, 'form2.html', data)

def update(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    form = ProdutoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def update2(request, pk):
    data = {}
    data['ls'] = Categoria.objects.get(pk=pk)
    form = CategoriaForm(request.POST or None, instance=data['ls'])
    if form.is_valid():
        form.save()
        return redirect('lista')

def delete(request, pk):
    db = Produto.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def delete2(request, pk):
    ls = Categoria.objects.get(pk=pk)
    ls.delete()
    return redirect('lista')

def lista(request):
    data ={}
    data['ls'] = Categoria.objects.all()
    return render(request, 'lista_cat.html', data)