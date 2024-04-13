"""
URL configuration for on_counter_billing_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (All_Create_Employee_Profile,Showall_Add_Employee,Get_Update_Delete_Employee,
Get_Update_Delete_Employee_Profile,Getall_Create_Customer,Showall_Create_Product,Get_Update_Delete_Customer,
Get_Update_Delete_Product,Create_Bill,Get_Delete_Bill,All_Bills,Analytics)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('employee/token/', TokenObtainPairView.as_view(), name='employee_token_pair'), # to get jwt tokens (access,refresh)
    path('employee/token/refresh/', TokenRefreshView.as_view(), name='employee_token_refresh'),    # to get jwt refresh token
    path('employee/',Showall_Add_Employee.as_view(),name = 'list_create_employee'), # to get all employees and create employee (only for admin)
    path('employee/<slug:slug>/',Get_Update_Delete_Employee.as_view(),name = 'get_update_delete_employee'), # to get, update and delete an employee. (only for admin) 
    path('employee_profile/',All_Create_Employee_Profile.as_view(),name = 'create_profile'), # to create an profile by an admin
    path('employee_profile/<slug:slug>/',Get_Update_Delete_Employee_Profile.as_view(),name = 'get_update_profile'), # to get, update and delete profile (only for admin)
    path('customer/',Getall_Create_Customer.as_view(),name = 'list_create_customer'),# to list all and create a customers (only for admin)
    path('customer/<slug:slug>/',Get_Update_Delete_Customer.as_view(),name = 'get_update_delete_customer'),# to get, update and delete customers (only for admin)
    path('product/',Showall_Create_Product.as_view(),name = 'list_create_product'), # to list, add product by admin
    path('product/<slug:slug>/',Get_Update_Delete_Product.as_view(),name = 'get_update_delete_product'), # to get, update and delet product by admin  
    path('bill/',All_Bills.as_view(),name = 'list_bills'), # to view all bills by admin
    path('bill/<slug:slug>/',Get_Delete_Bill.as_view(),name = 'get_delete_bill'),# to get a specific bill 
    path('createbill/',Create_Bill.as_view(),name = 'create_bill'), # to create a bill by employee
    path('analyze/',Analytics.as_view(),name='analyze'), # to analyze the sales
 
]
