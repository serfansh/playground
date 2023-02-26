from django.shortcuts import render
from .models import Clothes

def home(request):
    products = Clothes.objects.all()

    context = {'products': products}
    return render(request, 'store/store.html', context)