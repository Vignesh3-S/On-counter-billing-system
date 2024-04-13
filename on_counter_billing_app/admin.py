from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from on_counter_billing_app.models import Employee,Product,Customer,Bill_Customer,Employee_Profile

class CustomUserAdmin(UserAdmin):
    admin.site.site_header = "On Counter Billing Administration"
    model = Employee
    list_display = ("Employee_username","last_login","is_active",)
    list_filter = ("is_staff", "is_active","is_superuser",)
    fieldsets = (
        ("Employee Details", {"fields": ("Employee_name","Employee_username","password","slug",)}),
        ("Permissions", {"fields": ("is_staff", "is_active","is_superuser","groups", "user_permissions",)}),
        ("Important Dates", {"fields": ("Employee_Joining_date","Employee_update_date","last_login",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "Employee_name","Employee_username","password1", "password2",
            )}
        ),
    )
    readonly_fields = ("Employee_Joining_date","Employee_update_date","last_login",)
    search_fields = ("Employee_username",)
    ordering = ("Employee_Joining_date",)

admin.site.register(Employee, CustomUserAdmin)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Bill_Customer)
admin.site.register(Employee_Profile)


# Register your models here.
