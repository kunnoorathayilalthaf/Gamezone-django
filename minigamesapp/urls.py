from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_function,name='home'),
    path('categories',views.categories_function,name='categories'),
    path('<slug:slug>/',views.products_function,name='products'),
    path('products/<slug:slug>/',views.productdetail_function,name='productsdetails'),
    path('wishlist',views.wishlist_function,name='wishlist'),
    path('blog-details',views.blogdetail_function,name='blogdetails'),
    path('signup',views.signup_function,name='signup'),
    path('login',views.login_function,name='login'),
    path('add_to_wishlist',views.add_to_wishlist,name='add_to_wishlist'),
    path('removecart/<int:cart_id>/',views.removecart,name='removecart'),
    path('logout',views.logout_function,name='logout'),
    path('search',views.search_function,name='search'),    
    
]