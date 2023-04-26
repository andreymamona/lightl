from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Product
from django.core.paginator import Paginator
from django.core.cache import cache


def index(request):
    title = request.GET.get("title")

    products = Product.objects.all()

    if title is not None:
        products = products.filter(title__icontains=title)

    sort_price = request.GET.get("sort_price")
    if sort_price is not None:
        if sort_price == 'up':
            products = products.order_by("price")
        elif sort_price == 'down':
            products = products.order_by("-price")

    result = cache.get(f"products-view-{title}-{sort_price}")
    if result is not None:
        return result

    paginator = Paginator(products, 18)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    context = {
        "products": products,
    }

    response = render(request, "index.html", context)
    cache.set(f"products-view-{title}", response, 60 * 60)
    return response
    # return render(request, "index.html", context)


def product_view(request):
    item_id = request.GET.get("id")
    try:
        product = Product.objects.get(id=item_id)
    except Product.DoesNotExist:
        return HttpResponse(f"Ooops...wrong ID<br> <p><a href='/'>Main page</a></p>")
    context = {
        "product": product,
    }
    return render(request, "product_detail.html", context)
