from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Product
from django.db.models import Sum, F


def index(request):
    products = Product.objects.all()

    sort_price = request.GET.get("sort_price")
    if sort_price is not None:
        if sort_price == 'up':
            products = products.order_by("price")
        elif sort_price == 'down':
            products = products.order_by("-price")

    context = {
        "products": products,
    }

    return render(request, "index.html", context)


def product_view(request):
    item_id = request.GET.get("id")
    try:
        product = Product.objects.get(id=item_id)
    except Product.DoesNotExist:
        return HttpResponse(f"Ooops...wrong ID<br> <p><a href='/'>Main page</a></p>")
    context = {
        "product": product,
    }
    return render(request, "product.html", context)
