from django.contrib import admin
from django.urls import path
from . import views #mở view.py

urlpatterns = [
    # đường dẩn view.py def home
    # name ="tên" , tức là đặt cả cái đường dẩn thành 1 cái "tên" để lúc dùng       
    # <a href="{% url 'tên' %}"> unicode hex; quay lại đường dẫn tên tên </a>     sẽ trỏ về cái đường dẩn đã đặt       

    path('', views.home, name="home"), 
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),




    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

]
