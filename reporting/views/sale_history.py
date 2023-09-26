from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from internal.models import Order, Package_Category
from django.shortcuts import render,


@api_view(['GET'])
def index(request):
    order = Order.objects.all()
    user = User.objects.all()
    package_categories = Package_Category.objects.all()
    all_package = len(Package_Category.objects.all())
    all_order = len(Order.objects.all())
    content = {
        "titile" :"home",
        "order":order,
        "user":user,
        'package_categories':package_categories,
        "cnt_package ": all_package,
        "cnt_order":all_order,

    }
    return render(request)