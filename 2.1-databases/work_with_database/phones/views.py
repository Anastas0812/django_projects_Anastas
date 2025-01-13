from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone




def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_option = request.GET.get('sort', 'name')
    if sort_option == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort_option == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    elif sort_option == 'name':
        phones = Phone.objects.all().order_by('name')
    else:
        phones = Phone.objects.all().order_by('name')

    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
