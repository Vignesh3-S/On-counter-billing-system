from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

class Employee_manager(BaseUserManager):
    def create_user(self, Employee_username, password, **extra_fields):
        if not Employee_username:
            raise ValueError(_("The Username must be set"))
        user = self.model(Employee_username=Employee_username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, Employee_username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("slug",slugify(Employee_username))

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(Employee_username, password, **extra_fields)