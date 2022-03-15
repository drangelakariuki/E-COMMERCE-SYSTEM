from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# collection model
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    
    def __str__(self) -> str:
        return self.description

class Collection(models.Model):
    title = models.CharField(max_length = 255)
    featured_product = models.ForeignKey('Product', on_delete = models.SET_NULL, null=True,related_name='+',blank=True)
    def __str__(self):
        return '%s' % (self.title)

    class meta:
        ordering = ['product_type']

# customer model
class Customer(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255, unique=True)
    phone_number = models.CharField(max_length= 11,unique=True)
    
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
    class meta:
        ordering = ['first_name']

# product model
class Product(models.Model):
    product_image = models.ImageField(null=True, blank=True)
    product_name = models.CharField(max_length = 255)
    slug = models.SlugField(default ='-')
    product_description = models.CharField(max_length = 255, null = True, blank = True) 
    product_price = models.DecimalField(max_digits= 8, decimal_places = 2,validators= [MinValueValidator(1)])
    product_inventory = models.PositiveIntegerField() # inventory or hand
    last_updated = models.DateTimeField(auto_now = True)
    collection = models.ForeignKey('Collection', on_delete = models.PROTECT)
    promotions = models.ManyToManyField(Promotion,blank = True)
    

    def __str__(self):
        return '%s' % (self.product_name)
    '''
       @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
            return url
    '''


class Order(models.Model):
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS =[
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
        ]
    customer = models.ForeignKey(Customer, on_delete = models.PROTECT)
    placed_at = models.DateTimeField(auto_now_add = True)
    payment_status = models.CharField(max_length = 1, choices = PAYMENT_STATUS, default = 'P')
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete = models.PROTECT)
    quantity_ordered = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits= 8, decimal_places = 2)
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity_ordered = models.PositiveSmallIntegerField()


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    town = models.CharField(max_length = 255)
    area = models.CharField(max_length = 255)

    def __str__(self):
        return self.town




