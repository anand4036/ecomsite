from django.shortcuts import render
from.models import products,order
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    product_objects = products.objects.all()
    #search function
    item_name = request.GET.get('item_name')
    if item_name !=''and item_name is not None:
        product_objects = product_objects.filter(title__icontains= item_name)
    #paginator function
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request,'shop/index.html',{'product_objects':product_objects})

def detail(request,id):
    product_object = products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object': product_object})

def checkout(request):
    if request.method == "POST":
        item = request.POST.get('item',"")
        name = request.POST.get('name',"")
        phone = request.POST.get('phone',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        address2 = request.POST.get('address2',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        pincode = request.POST.get('pincode',"")


        Order = order(item=item,name=name,phone=phone,email=email,address=address,address2=address2,city=city,state=state,pincode=pincode)
        Order.save()


    return render(request,'shop/checkout.html')

