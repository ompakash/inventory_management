from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import *

# Create your views here.
@login_required
def index(request):
    return render(request,'dashboard/index.html')

@login_required
def staff(request):
    return render(request,'dashboard/staff.html')

@login_required
def product(request):
    return render(request,'dashboard/product.html')

@login_required
def order(request):
    return render(request,'dashboard/order.html')