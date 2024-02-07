from django.shortcuts import render, get_object_or_404
from .models import Flower
from django.http import HttpResponseRedirect
from .forms import MyForm

# Create your views here.
def index(request):
    q= request.GET.get('q', None)
    items = ''
    if q is None or q is "":
        flowers = Flower.objects.all()
    elif q is not None:
        flowers = Flower.objects.filter(title__contains=q)      
    return render(request, 'index.html', {'flowers':flowers})

def detail(request, slug=None):
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'detail.html', {'flower':flower})

def tags(request, slug=None):
    flowers = Flower.objects.filter(tags__slug=slug)
    return render(request, 'index.html', {'flowers':flowers})

def create(request):
    if request.method == 'POST':
        form= MyForm(request.POST)
        if form.is_valid():
         print(form.cleaned_data['title'])
         form.save()
        return HttpResponseRedirect('/')
    else:
        form = MyForm()
    return render(request, 'edit.html',{'form': form})


def edit(request, pk=None):
    flower = get_object_or_404(Flower, pk=pk)
    if request.method == "POST":
        form = MyForm(request.POST, instance=flower)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm(instance=flower)
    return render(request, 'edit.html', {'form': form})



def delete(request, pk=None): 
    flower = get_object_or_404(Flower, pk=pk)
    flower.delete()
    return HttpResponseRedirect('/')