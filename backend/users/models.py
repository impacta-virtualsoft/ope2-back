from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for OPE2 Divina Hamburgueria."""

    #: First and last name do not cover name patterns around the globe
    email = models.EmailField(_("Email"), unique=True)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = models.CharField(max_length=200)  # type: ignore
    last_name = models.CharField(max_length=200)  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def is_cashier(self):
        if self.groups.filter(name="Caixa"):
            return True
        else:
            return False

    def is_kitchen(self):
        if self.groups.filter(name="Cozinha"):
            return True
        else:
            return False

    def is_adm(self):
        if self.groups.filter(name="Administrativo"):
            return True
        else:
            return False

    def is_owner(self):
        if self.groups.filter(name="Proprietario"):
            return True
        else:
            return False

    # def is_superuser(self):
    #     return self.groups.filter(name="Superuser")
