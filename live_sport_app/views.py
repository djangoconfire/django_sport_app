from django.shortcuts import render
from models import Order
from forms import OrderForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
# Create your views here.

def home(request):
    return render(request,'base.html',{})


# here dashboard
def dashboard(request):
    orders=Order.objects.all().order_by('-order_created')
    paginator=Paginator(orders,10)
    page=request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        ## if page not an integer deliver to first page
        orders = paginator.page(1)
    except EmptyPage:
        ## page is out of range
        orders = paginator.page(paginator.num_pages)
    form = OrderForm()
    return render(request,'dashboard.html',{'orders':orders,'form':form})

def create_order(request):
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=OrderForm()

    return render(request,'order_form.html',{'form':form})

