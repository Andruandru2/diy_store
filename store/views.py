from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Order
from django.shortcuts import redirect

# Create your views here.
def home(request):
    products = Product.objects.order_by('-id')[:3]   # fetch datas for database
    return render(request, 'store/home.html', {'products':products}) # render - sends it to html 

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/product_detail.html', {'product':product})


def buy_now(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        quantity = int(request.POST.get('quantity'))

        total_price = product.price * quantity

        order = Order.objects.create(
            product=product,
            name=name,
            address=address,
            quantity=quantity,
            total_price=total_price
        )

        message = f"Order Details:%0AName: {name}%0AProduct: {product.name}%0AQuantity: {quantity}%0ATotal: ₹{total_price}"
        phone = "919632046967"
        whatsapp_url = f"https://wa.me/{phone}?text={message}"

        return render(request, 'store/success.html', {
            'whatsapp_url': whatsapp_url
        })

    return render(request, 'store/checkout.html', {'product': product})

def all_products(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(request, 'store/all_products.html', {'products': products})

def about(request):
    return render(request, 'store/about.html')
