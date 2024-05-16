from rest_framework import serializers
from .models import Employee,Product,Customer,Bill_Customer,Employee_Profile
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.text import slugify
import random
from django.contrib.auth.models import Group
    

class Employee_Serializer(serializers.ModelSerializer):
    password = serializers.CharField( write_only=True,required=True,help_text = 'create a strong passsword using alphanumerics and special characters.',
        style={'input_type': 'password', 'placeholder': 'Password','minlength':8,'maxlength':15})
    confirm_password = serializers.CharField( write_only=True,required=True,help_text='same as in the password field.',
        style={'input_type': 'password', 'placeholder': 'Confirm Password','minlength':8,'maxlength':15})
    
    class Meta:
        model = Employee
        exclude = ['id']
    
    def create(self,data):
        print(data)
        department = data.get('Employee_department')
        if department == 'Product_Adder' or department == 'Product_Seller' or department == 'Customer_Adder':
            group = Group.objects.get(name=department)
            data['groups'] = [group] 
        else:
            raise serializers.ValidationError('invalid value to the department field.')
            
            
        if data.get('password') != data.get('confirm_password'):
                raise serializers.ValidationError({'message':['Your password and confirm password mis-matched']})
        try:
            validate_password(password=data.get('password'))
        except ValidationError as e:
            raise serializers.ValidationError(list(e))
        data.pop('confirm_password')    
        data['password'] = make_password(data.get('password'))
        data['slug'] = slugify(data.get('Employee_username'))
        data['is_active'] = True
        return super(Employee_Serializer,self).create(data)
    
    def update(self, instance,data):
        if data.get('password') != data.get('confirm_password'):
                raise serializers.ValidationError({'message':['Your password and confirm password mis-matched']})
        try:
            validate_password(password=data.get('password'))
        except ValidationError as e:
            raise serializers.ValidationError(list(e))
        data.pop('confirm_password')
        instance.slug = slugify(data.get('Employee_username',instance.Employee_username))
        return super(Employee_Serializer,self).update(instance,data)

class Employee_Profile_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_Profile
        fields = '__all__'
    
    def to_representation(self, instance):
        employee = super(Employee_Profile_Serializer, self).to_representation(instance)
        employee['Employee'] = instance.Employee.Employee_name
        return employee
    
    def create(self,data):
        data['slug'] = slugify(data.get('Employee'))
        return super(Employee_Profile_Serializer,self).create(data)
    
    def update(self, instance,data):
        instance.slug = slugify(data.get('Employee',instance.Employee))
        return super(Employee_Profile_Serializer,self).update(instance,data)

class Customer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ['id']
    
    def create(self,data):
        data['slug'] = str(slugify(data.get('Customer_name'))) + str(random.randrange(1000,9999)) 
        return super(Customer_Serializer,self).create(data)
    
    def update(self, instance,data):
        instance.slug = str(slugify(data.get('Customer_name',instance.Customer_name)))+str(random.randrange(1000,9999))
        return super(Customer_Serializer,self).update(instance,data)
    
class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['id']
    
    def to_representation(self, instance):
        product = super(Product_Serializer, self).to_representation(instance)
        product['Product_price'] = "Rs."+str(instance.Product_price)+" only."
        return product
    
    def create(self,data):
        data['slug'] = str(slugify(data.get('Product_name'))) + str(random.randrange(1000,9999)) 
        return super(Product_Serializer,self).create(data)
    
    def update(self, instance,data):
        instance.slug = str(slugify(data.get('Product_name',instance.Product_name)))+str(random.randrange(1000,9999))
        return super(Product_Serializer,self).update(instance,data)

class Bill_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bill_Customer
        exclude = ['id']
        
    def to_representation(self, instance):
        user = super(Bill_Serializer, self).to_representation(instance)
        user['Employee'] = instance.Employee.Employee_name
        user['Customer'] = instance.Customer.Customer_name
        user['Product'] = instance.Product.Product_name
        user['Price_per_quantity'] = "Rs."+str(instance.Price_per_quantity)
        return user
    
    def create(self,data):
        #print(data)
        data['slug'] = str(slugify(data.get('Customer')))+str(slugify(data.get('Product')))+str(slugify(data.get('Employee')))+str(random.randrange(1000,9999))  
        super(Bill_Serializer,self).create(data)
        obj = Bill_Customer.objects.get(slug=data['slug'])
        #print("obj",obj)
        if data.get('GST') > 0:
            gst = data.get('Price_per_quantity')*data.get('GST')/100
            #print(data.get('Count'))
            #print(data.get('Price_per_quantity'))
            obj.Total_Price = float("{0:.2f}".format(data.get('Count')*data.get('Price_per_quantity')))+float("{0:.3f}".format(gst))
        else:
            obj.Total_Price = float("{0:.2f}".format(data.get('Count')*data.get('Price_per_quantity')))
        obj.save()
        return obj