from rest_framework import generics
from .serializers import (Employee_Profile_Serializer,Employee_Serializer,Customer_Serializer,
Product_Serializer,Bill_Serializer)
from .models import Employee_Profile,Employee,Product,Customer,Bill_Customer
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from django.shortcuts import render
from .permission import (Employee_Permission,Employee_Profile_Permission,Customer_Permission,Product_Permission,
                         Product_Sell_Permission)


def home(request):
    return render(request,'on_counter_billing_app/home.html')

class Showall_Add_Employee(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employee_Serializer
    permission_classes = [Employee_Permission]
    
class Get_Update_Delete_Employee(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employee_Serializer
    permission_classes = [Employee_Permission]
    lookup_field = 'slug'

class All_Create_Employee_Profile(generics.ListCreateAPIView):
    queryset = Employee_Profile.objects.all()
    serializer_class = Employee_Profile_Serializer
    permission_classes = [Employee_Profile_Permission]

class Get_Update_Delete_Employee_Profile(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee_Profile.objects.all()
    serializer_class = Employee_Profile_Serializer
    permission_classes = [Employee_Profile_Permission]
    lookup_field = 'slug'

class Getall_Create_Customer(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = Customer_Serializer
    permission_classes = [Customer_Permission]
    
    def post(self,request,*args,**kwargs):
        user = Employee.objects.get(id = request.user.id)
        print(user.Employee_department)
        if user.Employee_department == 'Customer_Adder':
            return self.create(request,*args,**kwargs)
        else:
            return Response('Not allowed to add customer',status=status.HTTP_401_UNAUTHORIZED)
    
class Get_Update_Delete_Customer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = Customer_Serializer
    permission_classes = [Customer_Permission]
    lookup_field = 'slug'

class Showall_Create_Product(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Product_Serializer
    permission_classes = [Product_Permission]
    
    def post(self,request,*args,**kwargs):
        try:
            Product.objects.get(Product_name = request.data['Product_name'],Product_quantity = request.data['Product_quantity'],
                                    Product_price = request.data['Product_price'],Product_description = request.data['Product_description'])
        except:
            return self.create(request,*args,**kwargs)
        else:
            return Response('Product already added',status=status.HTTP_409_CONFLICT)

class Get_Update_Delete_Product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = Product_Serializer
    permission_classes = [Product_Permission]
    lookup_field = 'slug'

class Create_Bill(generics.CreateAPIView):
    serializer_class = Bill_Serializer
    permission_classes = [Product_Sell_Permission]
    
    def post(self,request,*args,**kwargs):
        user = Employee.objects.get(id=request.user.id)
        print(request.user)
        if user.id == int(request.data['Employee']):
            product_id = request.data['Product']
            employee_id = request.data['Employee']
            product = Product.objects.get(id = product_id)
            employee = Employee.objects.get(id = employee_id)
            try:
                employee_profile = Employee_Profile.objects.get(Employee = employee)
                employee_profile.maximum_sale += int(request.data['Count'])
                employee_profile.save()
            except:
                return Response('Please create your Employee Profile before make a bill.',status=status.HTTP_307_TEMPORARY_REDIRECT)
            product.Product_quantity = product.Product_quantity - int(request.data['Count'])
            product.maximum_sale += int(request.data['Count'])
            product.save()
            return self.create(request,*args,**kwargs)
        else:
            return Response('Not allowed to sell the product / Employee id should be yours.',status=status.HTTP_401_UNAUTHORIZED)

class All_Bills(generics.ListAPIView):
    queryset = Bill_Customer.objects.all()
    serializer_class = Bill_Serializer
    permission_classes = [IsAdminUser]


class Get_Delete_Bill(generics.RetrieveDestroyAPIView):
    queryset = Bill_Customer.objects.all()
    serializer_class = Bill_Serializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
    
class Analytics(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request,*args,**kwargs):
        Employee_queryset = Employee_Profile.objects.all()
        Product_queryset = Product.objects.all()
        serialized_employee_set = Employee_Profile_Serializer(Employee_queryset,many = True)
        serialized_product_set = Product_Serializer(Product_queryset,many = True)
        employee_result = list()
        product_result = list()
        for i in [serialized_employee_set.data,serialized_product_set.data]:
            names = []
            count = []
            for j in i:
                if i == serialized_employee_set.data:
                    names.append(j['Employee'])
                    count.append(j['maximum_sale'])
                elif i == serialized_product_set.data:
                    names.append(j['Product_name'])
                    count.append(j['maximum_sale'])
            get_max_from_count = max(count)
            for k in range(len(count)):
                if get_max_from_count in count:
                    if i == serialized_employee_set.data:
                        employee_result.append(names[count.index(get_max_from_count)])
                    elif i == serialized_product_set.data:
                        product_result.append(names[count.index(get_max_from_count)])
                    names.pop(count.index(get_max_from_count))
                    count.remove(get_max_from_count)
        return Response(f"Maximum sales made by the Employee(s) : {employee_result}. The product that sells the most : {product_result}")
    


        
    


