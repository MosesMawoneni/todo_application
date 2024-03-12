from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """create user"""

    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError(_("Please enter an email address because it is required"))
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError(_("is_staff must be set to True"))

        if other_fields.get("is_superuser") is not True:
            raise ValueError(_("is_superuser must be set to True"))

        if other_fields.get("is_active") is not True:
            raise ValueError(_("is_active must be set to True"))

        return self.create_user(email, password, other_fields)