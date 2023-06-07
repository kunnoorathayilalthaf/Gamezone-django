from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Products,Cart
from .forms import UserRegistrationForm,loginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,InvalidPage



# Create your views here.
def index_function(request):
    
    products_list=Products.objects.filter(is_active=True)
    paginator=Paginator(products_list,12)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    context={"products":products}
    return render(request,'index.html',context)

def categories_function(request):
    categories=Category.objects.filter(is_active=True)  
    context={"categories":categories}
    return render(request,'categories.html',context)

def products_function(request,slug):
    category=get_object_or_404(Category,slug=slug)
    products=Products.objects.filter(is_active=True,category=category)
    context={"category":category,"products":products}
    return render(request,'products.html',context)

def productdetail_function(request,slug):
    products=get_object_or_404(Products,slug=slug)

    
    context={"products":products}
    return render(request,'productdetails.html',context)

@login_required
def wishlist_function(request):
    user=request.user
    products=Products.objects.filter(is_active=True)
    cart_products=Cart.objects.filter(user=user)
    context={
        'cart_products':cart_products,'products':products}
    return render(request,'wishlist.html',context)


def blogdetail_function(request):
    return render(request,'blog-details.html')

@login_required
def add_to_wishlist(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=get_object_or_404(Products,id=product_id)

    item_already_in_wishlist=Cart.objects.filter(product=product_id,user=user)
    if item_already_in_wishlist:
        cp=get_object_or_404(Cart,product=product_id,user=user)
        messages.error(request,'This Game has been added already')
        cp.save()
    else:
        Cart(user=user,product=product).save()
    return redirect('wishlist')

login_required
def removecart(request,cart_id):
    if request.method == 'GET':
        cp=get_object_or_404(Cart,id=cart_id)
        cp.delete()
    return redirect('wishlist')

def signup_function(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            messages.success(request,'Registered successfully')
        else:
            messages.error(request,'Registration failed')
    else:
        form=UserRegistrationForm()
    context={'form':form}
    return render(request,'signup.html',context)


def login_function(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/categories')
        
        form=loginForm()
        return render(request,'login.html',{'form':form})
    
    elif request.method == 'POST':
        form=loginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                messages.success(request,f'Hi {username.title()} ,Welcome back!')
                return redirect('/categories')
        else:
            messages.error(request,f'Invalid username or password')
            return render(request,'login.html',{'form':form})

def logout_function(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('/login')

def search_function(request):
    q=request.GET.get('q','')
    data=Products.objects.filter(title__icontains=q).order_by('-id')
    context={"data":data}
    return render(request,'search.html',context)




    

