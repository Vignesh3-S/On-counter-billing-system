Welcome, If you want to test the REST API the go through the details below.

INSTRUCTIONS TO HOW TO TEST REST API

For Testing use the credentials,
	
	Employee_username = Mall_admin
	password = Amin123@#

use the below values as the Department values:
		
		--> Customer_Adder
		--> Product_Adder
		--> Product_Seller



1)  url : on_counter_billing/employee/token/ 
    why : To get access and refresh token
    method : POST
    values to be send : Employee_username and password

2)  url : on_counter_billing/employee/token/refresh/ 
    why : To get access token
    method : POST
    values to be send : refresh token
--------------------------------------------------------

admin or user has the the add_employee permission can perform action .

3)  url : on_counter_billing/employee/
    why : To get all employees
    method : GET
    Authentication : access token

4)  url : on_counter_billing/employee/
    why : To create an employee
    method : POST
    Authentication : access token
    values to be send : Employee_name, Employee_username, password, confirm_password, Employee_department

5)  url : on_counter_billing/employee/{slug}/
    why : To get an employee
    method : GET
    Authentication : access token

6)  url : on_counter_billing/employee/{slug}/
    why : To update an employee with all field
    method : PUT
    Authentication : access token
    values to be send : Employee_name, Employee_username, password, confirm_password

7)  url : on_counter_billing/employee/{slug}/
    why : To update an employee with selected field
    method : PATCH
    Authentication : access token
    values to be send : Employee_name or Employee_username or password and confirm_password

8)  url : on_counter_billing/employee/{slug}/
    why : To delete an employee
    method : DELETE
    Authentication : access token

---------------------------------------------
admin and all employees cn create their profile.  

9)  url : on_counter_billing/employee_profile/
    why : To get all employees
    method : GET
    Authentication : access token

10) url : on_counter_billing/employee_profile/
    why : To create an employee profile
    method : POST
    Authentication : access token
    values to be send : Employee_mobile, Employee_email, Employee_address, Employee

11) url : on_counter_billing/employee_profile/{slug}/
    why : To get an employee profile
    method : GET
    Authentication : access token

12) url : on_counter_billing/employee_profile/{slug}/
    why : To update an employee profile with all field
    method : PUT
    Authentication : access token
    values to be send : Employee_mobile, Employee_email, Employee_address, Employee

13) url : on_counter_billing/employee_profile/{slug}/
    why : To update an employee profile with selected field
    method : PATCH
    Authentication : access token
    values to be send : Employee_mobile or Employee_email or Employee_address or Employee

14) url : on_counter_billing/employee_profile/{slug}/
    why : To delete an employee profile
    method : DELETE
    Authentication : access token

-------------------------------------------------------
Employee (Customer_Adder) and Admin can perform the action. 

15) url : on_counter_billing/customer/
    why : To get all customers
    method : GET
    Authentication : access token

16) url : on_counter_billing/customer/
    why : To create an customer
    method : POST
    Authentication : access token
    values to be send : Customer_mobile, Customer_email, Customer_address, Customer_name

17) url : on_counter_billing/customer/{slug}/
    why : To get an customer
    method : GET
    Authentication : access token

18) url : on_counter_billing/customer/{slug}/
    why : To update an customer with all fields
    method : PUT
    Authentication : access token
    values to be send : Customer_mobile, Customer_email, Customer_address, Customer_name

19) url : on_counter_billing/customer/{slug}/
    why : To update an customer with selected field
    method : PATCH
    Authentication : access token
    values to be send : Customer_mobile or Customer_email or Customer_address or Customer_name

20) url : on_counter_billing/customer/{slug}/
    why : To delete an customer
    method : DELETE
    Authentication : access token

-----------------------------------------------------------------
Employee (Product_Adder) and admin can perform actions. 

21) url : on_counter_billing/product/
    why : To get all products
    method : GET
    Authentication : access token

22) url : on_counter_billing/product/
    why : To create an product
    method : POST
    Authentication : access token
    values to be send : Product_name, Product_description, Product_quantity, Product_count, Product_price

23) url : on_counter_billing/product/{slug}/
    why : To get an product
    method : GET
    Authentication : access token

24) url : on_counter_billing/product/{slug}/
    why : To update an product with all fields
    method : PUT
    Authentication : access token
    values to be send : Product_name, Product_description, Product_quantity, Product_count, Product_price

25) url : on_counter_billing/product/{slug}/
    why : To update an product with selected field
    method : PATCH
    Authentication : access token
    values to be send : Product_name or Product_description or Product_quantity or Product_count or Product_price

26) url : on_counter_billing/product/{slug}/
    why : To delete an product
    method : DELETE
    Authentication : access token
  
------------------------------------------------------------
Employee (Product_Seller)can CREATE bill. Admin can GET, DELETE, LIST bills.  

27) url : on_counter_billing/bill/
    why : To get all bills
    method : GET
    Authentication : access token

28) url : on_counter_billing/createbill/
    why : To create an bill
    method : POST
    Authentication : access token
    values to be send : Employee, Customer, Product, count, price

29) url : on_counter_billing/bill/{slug}/
    why : To get an bill
    method : GET
    Authentication : access token

30) url : on_counter_billing/bill/{slug}/
    why : To delete an bill
    method : DELETE
    Authentication : access token

--------------------------------------------------------------
only admin can perform action.

31) url : on_counter_billing/analyze/
    why : To analyze the sales
    method : GET
    Authentication : access token

----------------------------------------------------------------

32) url : api/schema/docs/
    why : To get swagger ui
    method : GET
