from django.shortcuts import render
from django.shortcuts import redirect
from urllib import request
from django.http import HttpResponseBadRequest
import re
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views import View
from . models import Product
from . models import Diet, Track
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.db.models import Count
from django.contrib import messages
from .forms import Customer
from django.http import JsonResponse
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request , "app/home.html")



def contact(request):
    return render(request , "app/contact.html")



class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())
    



class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"app/category.html",locals())
    



class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals())



class DietPlan(View):
    def get(self,request,val):
        product = Diet.objects.filter(type=val)
        time = Diet.objects.filter(type=val).values('time')
        return render(request,"app/dietplan.html",locals())
    




class DietPlanTime(View):
    def get(self,request,val):
        product = Diet.objects.filter(title=val)
        title = Diet.objects.filter(type=product[0].type).values('title')
        return render(request,"app/dietplan.html",locals())




class DietDetail(View):
    def get(self,request,pk):
        product = Diet.objects.get(pk=pk)
        return render(request,"app/dietdetails.html",locals())

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregi.html',locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Register Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request, 'app/customerregi.html',locals())
    

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulations! Profile save succesfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request, 'app/profile.html',locals())
    


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',locals())




def add_to_progress(request):
        user= request.user
        product_id= request.GET.get('prod_id')
        product = Product.objects.get(id=product_id)
        Track(user=user,product=product).save()
        return redirect("/track")
  





def show_track(request):
    user=request.user
    cart = Track.objects.filter(user=user)
    return render(request, 'app/addtoprogress.html',locals())


def remove_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Track.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        track = Track.objects.filter(user=user)
        amount = amount 
        data={
            'amount':amount,
        }
        return JsonResponse(data)