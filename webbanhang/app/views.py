# phần dẫn đường trang web để xem 
# view.py lấy dữ liệu từ models.py và truyền lên path html
from django.shortcuts import render

#HttpResponse    thông báo phản hồi HTTP server trả về cho client
#JsonResponse   kiểu dữ liệu trả vè từ json
from django.http import HttpResponse,JsonResponse 
from .models import *

# import json trong django
import json









def home(request): #yêu cầu trỏ về file templates/app/home.html
    
    #nếu gửi yêu cầu user(trong CSDL Customers) đa được xác thực      
    if request.user.is_authenticated:
        
        # khách hàng là gửi yêu cầu đến user -> customer        
        customer = request.user.customer 
        
        # lưu Order vào cái mà user tạo (ở bên models.py) -> quản lý -> lấy hay tạo, hóa đơn giao dịch chưa thành công
        # đặt biến order lấy thông tin từ "class Order"(models.py)        
        order, created = Order.objects.get_or_create(customer =customer,complete =False)          
        
        # biến order đã đặt ở trên gán "class Order"(models.py)
        # order.orderitem_set.all()       trong "class Order" trỏ về orderitem trong models.py và lấy tất cả        
        items = order.orderitem_set.all()
        
        # biến cartItems đã đặt ở trên gán "class Order"(models.py)
        # order.get_cart_items_total_count là tử "class Order"(models.py)
        # trỏ vào "class Order"(models.py)     def get_cart_items_total_count(self):
        cartItems = order.get_cart_items_total_count

    else:
        items=[]
        order={'get_cart_items_total_count':0 ,'get_cart_total_prices_count':0}
        cartItems = order['get_cart_items_total_count']

    # đặt biến products lấy tất cả thông tin từ "class Product"(models.py) 
    products = Product.objects.all() 
    
    # với products bên phải là đã dc định nghĩa phía trên và csdl trong models
    context={'products': products,'cartItems':cartItems}
    return render(request,'app/home.html',context) 








def cart(request): #yêu cầu trỏ về file templates/app/cart.html

    #nếu gửi yêu cầu user(trong CSDL Customers) đa được xác thực  
    if request.user.is_authenticated:
        
        # khách hàng là gửi yêu cầu đến user -> customer
        customer = request.user.customer 
       
        # lưu Order vào cái mà user tạo (ở bên models.py) -> quản lý -> lấy hay tạo, hóa đơn giao dịch chưa thành công
        # đặt biến order lấy thông tin từ "class Order"(models.py) 
        order, created = Order.objects.get_or_create(customer =customer,complete =False)          
        
        # biến order đã đặt ở trên gán "class Order"(models.py)
        # order.orderitem_set.all()       trong "class Order" trỏ về orderitem trong models.py và lấy tất cả
        items = order.orderitem_set.all()

        # biến cartItems đã đặt ở trên gán "class Order"(models.py)
        # order.get_cart_items_total_count là tử "class Order"(models.py)
        # trỏ vào "class Order"(models.py)     def get_cart_items_total_count(self):
        cartItems = order.get_cart_items_total_count

    else:
        items=[]
        order={'get_cart_items_total_count':0 ,'get_cart_total_prices_count':0}
        cartItems = order['get_cart_items_total_count']

    #với dữ liệu 'items' truyền vào giá trị items ở phía trên mới tạo
    #với dữ liệu 'order' truyền vào giá trị order ở phía trên mới tạo
    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'app/cart.html',context) 







def checkout(request): #yêu cầu trỏ về file templates/app/checkout.html
    
    #nếu gửi yêu cầu user(trong CSDL Customers) đa được xác thực  
    if request.user.is_authenticated:
        
        # khách hàng là gửi yêu cầu đến user -> customer
        customer = request.user.customer 
       
        # lưu Order vào cái mà user tạo (ở bên models.py) -> quản lý -> lấy hay tạo, hóa đơn giao dịch chưa thành công
        # đặt biến order lấy thông tin từ "class Order"(models.py) 
        order, created = Order.objects.get_or_create(customer =customer,complete =False)          
        
        # biến order đã đặt ở trên gán "class Order"(models.py)
        # order.orderitem_set.all()       trong "class Order" trỏ về orderitem trong models.py và lấy tất cả
        items = order.orderitem_set.all()
        
        # biến cartItems đã đặt ở trên gán "class Order"(models.py)
        # order.get_cart_items_total_count là tử "class Order"(models.py)
        # trỏ vào "class Order"(models.py)     def get_cart_items_total_count(self):
        cartItems = order.get_cart_items_total_count

    else:
        items=[]
        order={'get_cart_items_total_count':0 ,'get_cart_total_prices_count':0}
        cartItems = order['get_cart_items_total_count']

    #với dữ liệu 'items' truyền vào giá trị items ở phía trên mới tạo
    #với dữ liệu 'order' truyền vào giá trị order ở phía trên mới tạo
    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'app/checkout.html',context) 








def updateItem(request): #yêu cầu trỏ 

    #json.loads(request.body)
    #chạy file json gửi yêu cầu đến "body"(app/static/app/js/cart.js)
    data = json.loads(request.body)

    #định nghĩa lại biến productId bên python , vì productId bên thuộc về bên cart.js
    productId = data['productId']
    action = data['action']

    # đặt lại biến , yêu cầu dữ liệu(-> models ->db.sqlite3) từ data base user -> customer
    customer =request.user.customer

    # Product(models.py) -> productId(cart.js) 
    # -> biến id = productId được đặt biến phía trên 
    #-> nối với biến productId trong java scripts
    product = Product.objects.get(id = productId)

    #customer =customer,complete =False  
    # trích xuất trong Order(models.py) biến customer -> Customer , chưa hoàn tất hóa đơm
    order, created = Order.objects.get_or_create(customer = customer,complete =False)
    
    #trong "Orderitem"(models.py) -> lấy 
    # biến "order" mới tạo = biến order tạo ở trên và 
    # biến "product" mới tạo = biến product đã tạo phía trên
    orderItem, created = OrderItem.objects.get_or_create(order =order,product =product)
    
    # nếu biến action - phương thức "add"|thêm vào| mũi tên huông trên|add to cart
    if action =='add':
        orderItem.quantity +=1

    # nếu biến action - phương thức "remove" |gỡ ra | mũi tên hướng xuống    
    elif action =='remove':
        orderItem.quantity -=1
    
    #lưu lại giá trị thêm/bớt ở hàm if elif phía trên vào "class Ordertem"(models.py)
    orderItem.save()
    
    if orderItem.quantity<=0:
        
        # xóa data của Orderitem(models.py) ->dbsqlite3
        orderItem.delete()

    return JsonResponse('added', safe=False)














def about(request): #yêu cầu trỏ về file templates/app/about.html
    context={}
    return render(request,'app/about.html',context) 

def contact(request): #yêu cầu trỏ về file templates/app/contact.html
    context={}
    return render(request,'app/contact.html',context) 