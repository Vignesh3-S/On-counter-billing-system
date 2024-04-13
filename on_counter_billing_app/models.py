from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,Group,Permission
from phonenumber_field.modelfields import PhoneNumberField
from .managers import Employee_manager
from django.utils.translation import gettext as _

employee_add_product,created = Group.objects.get_or_create(name="Product_Adder")
employee_add_customer,created = Group.objects.get_or_create(name="Customer_Adder")
employee_sell_product,created = Group.objects.get_or_create(name="Product_Seller")
product_permission = Permission.objects.get(codename='add_product')
customer_permission = Permission.objects.get(codename='add_customer')
sell_permission = Permission.objects.get(codename='add_bill_customer')
employee_add_product.permissions.add(product_permission)
employee_sell_product.permissions.add(sell_permission)
employee_add_customer.permissions.add(customer_permission)
employee_add_customer.save()
employee_sell_product.save()
employee_add_product.save()

class Employee(AbstractBaseUser,PermissionsMixin):
    Department_choices = [('Product_Adder','Product_Adder'),('Product_Seller','Product_Seller'),('Customer_Adder','Customer_Adder'),]
    Employee_name  = models.CharField(max_length=30,verbose_name=_("Name"))
    Employee_department = models.CharField(max_length=20,choices=Department_choices,verbose_name='Department')
    Employee_username = models.CharField(max_length=30,verbose_name=_("Username"),unique=True)
    Employee_Joining_date = models.DateTimeField(auto_now_add=True,verbose_name=_("Date Of Join"))
    Employee_update_date = models.DateTimeField(auto_now=True,verbose_name=_('Account Updated'),null=True)
    last_login = models.DateTimeField(verbose_name=_("Last login"),null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    slug = models.SlugField(null=False,max_length = 50,blank=True,unique=True)
    
    objects = Employee_manager()
    
    USERNAME_FIELD = 'Employee_username'
    REQUIRED_FIELDS = ['Employee_name','password']
    
    def __str__(self):
        return self.Employee_username

class Employee_Profile(models.Model):
    Employee = models.OneToOneField("Employee", verbose_name=_("Employee_id"), on_delete=models.CASCADE)
    Employee_mobile = PhoneNumberField(verbose_name = _("Mobile Number"))
    Employee_email = models.EmailField(verbose_name=_("Email"),unique=True)
    Employee_address = models.TextField(verbose_name=_("Address"),max_length = 200)
    Employee_image = models.ImageField(verbose_name=_("Image"),upload_to="Employees_images",null=True)
    Employee_profile_Joining_date = models.DateTimeField(auto_now_add=True,verbose_name=_("Date Of Join"),blank=True,null=True)
    Employee_profile_update_date = models.DateTimeField(auto_now=True,verbose_name=_('Account Updated'),null=True,blank=True)
    maximum_sale = models.IntegerField(verbose_name = "Maximum sale",default=0)
    slug = models.SlugField(null=False,max_length = 50,blank=True,unique=True)
    
    def __str__(self):
        return f"{self.Employee.Employee_username}'s profile"

class Product(models.Model):
    Product_name = models.CharField(max_length=30,verbose_name = _("Name"))
    Product_description = models.TextField(verbose_name=_("Description"),max_length=100)
    Product_quantity = models.CharField(verbose_name=_("Quantity"),max_length = 10,help_text=_("Quantity like 1kg, 1.5lit, 200g. if no weight leave it blank"))
    Product_count = models.IntegerField(verbose_name = _("Count"))
    Product_price = models.DecimalField(verbose_name=_("Price Per quantity/count in Rs."),max_digits=10,decimal_places=2)
    Product_image = models.ImageField(upload_to="product_images",null=True)
    Product_add_date = models.DateTimeField(auto_now_add=True,verbose_name=_("Date Of Add"),blank=True)
    Product_update_date = models.DateTimeField(auto_now=True,verbose_name=_('Date of Update'),null=True,blank=True)
    maximum_sale = models.IntegerField(verbose_name = "Maximum sale",default=0)
    slug = models.SlugField(null=False,max_length = 50,blank=True,unique=True)
    
    def __str__(self):
        return f'{self.Product_name} - {self.Product_quantity}'

class Customer(models.Model):
    Customer_name  = models.CharField(max_length=30,verbose_name=_("Name"))
    Customer_mobile = PhoneNumberField(verbose_name = _("Mobile Number"))
    Customer_email = models.EmailField(verbose_name=_("Email"),unique=True)
    Customer_address = models.TextField(verbose_name=_("Address"),max_length = 100)
    Customer_Joining_date = models.DateTimeField(auto_now_add=True,verbose_name=_("Date Of Join"),blank=True)
    Customer_update_date = models.DateTimeField(auto_now=True,verbose_name=_('Account Updated'),null=True,blank=True)
    slug = models.SlugField(null=False,max_length = 50,blank=True,unique=True)
    
    def __str__(self):
        return self.Customer_name

class Bill_Customer(models.Model):
    Employee = models.ForeignKey("Employee",on_delete=models.CASCADE,verbose_name=_("Employee_id"))
    Customer = models.ForeignKey("Customer",on_delete=models.CASCADE,verbose_name=_("Customer_id"))
    Product = models.ForeignKey("Product",on_delete = models.CASCADE,verbose_name = _("Product_id"))
    Count = models.IntegerField(verbose_name = _("Count"))
    Price = models.DecimalField (max_digits=10,decimal_places=2)
    Sell_date = models.DateTimeField(auto_now_add=True,verbose_name=_("Date Of sell"),blank=True)
    slug = models.SlugField(null=False,max_length = 50,blank=True,unique=True)
    
    def __str__(self):
        return f"{self.Employee.Employee_name}--{self.Product.Product_name}--{self.Customer.Customer_name}"
    

    
    
    
