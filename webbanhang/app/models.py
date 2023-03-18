#models lưu dữ liệu database vào db.sqlite3 và truyền dữ liệu ra cho view.py đọc
# cmd: pip install pillow            cho việc upload hình anh3len6 csdl

# lấy cơ sở dữ liệu và đưa vào db.sqlite3
from django.db import models
from django.contrib.auth.models import User
#from phonenumber_field.modelfields import PhoneNumberField







class Customer(models.Model): #khách hàng
    #"OneToOneField"  là khóa chính , kiểu dữ liệu str
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=False)
    #"CharField" kiểu dữ liệu str có giới hạn số lượng chữ
    #"TextField" kiểu dữ liệu str không giới hạn số lượng chữ
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)

    def __str__(self): #str string
        return self.name






# là trích dẩn {{.product}} trong html  trỏ trực tiếp  
class Product(models.Model): #sản phẩmm
    
    name = models.CharField(max_length=200,null=True)
    #"FloatField" trường số thực , kiểu dữ liệu float
    price = models.FloatField()
    #"BooleanField" là field có true,false,null
    digital = models.BooleanField(default=False,null=True,blank=False)
    # hình sau khi up lên sẽ nằm bừa bãi , vào setting.py của webbanhang(phần chính) để chỉnh sửa lại
    image = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.name

    # sau khi return, điều chỉnh thuộc tính của image
    @property
    def ImageURL(self):
        try: #nếu có
            url = self.image.url
        except:
            url = ''
        return url








class Order(models.Model): # đặt hàng
    
    # "ForeignKey" khóa phụ
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    # "DateTimeField" định dạng trường thời gian
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)

    # tổng số lượng vật phẩm
    @property # item count
    
    def get_cart_items_total_count(self):

        # đặt biến orderitems với tất đường dẩn "class Order" lấy tất cả dữ liệu của "class Orderitem"
        orderitems = self.orderitem_set.all()

        # tổng ( biến item nằm trong ortheritems 
        # <-> orderitems -> lấy số lượng của sản phẩm -> vòng lập in ra list số lượng)
        total_item_count = sum([item.quantity for item in orderitems])
        return total_item_count

    # tổng giá của tất cả vật phẩm trong orderitems list
    @property
    def get_cart_total_prices_count(self): # price count

        # đặt biến orderitems với tất đường dẩn "class Order" lấy tất cả dữ liệu của "class Orderitem"
        orderitems = self.orderitem_set.all()

        # # tổng ( biến item nằm trong ortheritems 
        # <-> orderitems -> biến đã định nghĩa "def get_total(self)" trong "class Orderitem"  
        # -> vòng lập in ra list ((giá sản phẩm ) * (số lượng sản phẩm)) với sản phảm giá và số lượng nằm cùng 1 loại sản phẩm
        total_price = sum([item.get_total_quantity_price_per_items for item in orderitems])
        return total_price







class OrderItem(models.Model): # list item đặt hàng của 1 khách hàng mua nhiều lân

    # là trích dẩn {{.product}} trong html trỏ đến "class Product" gián tiếp thông qua biến product của "class OrderItem"    
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    #"IntegerField" trương số nguyên 
    quantity = models.IntegerField(default=0,null=True,blank=True )
    date_added = models.DateTimeField(auto_now_add=True)
  
    # ko càn def return

    @property
    def get_total_quantity_price_per_items(self):
        
        total_price_per_items = self.product.price * self.quantity
        return total_price_per_items






class ShippingAddress(models.Model): # địa chỉ giao hàng

    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    mobile = models.CharField(max_length=10,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.address)








#phone_number = models.IntegerField(max_length=10, null=True, blank=False)
#phone_number_globle = PhoneNumberField(null=False, blank=False, unique=True)


#In the form:

#from phonenumber_field.formfields import PhoneNumberField
#class ClientForm(forms.Form):
    #phone = PhoneNumberField()