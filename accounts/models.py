from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    ROLE_CHOICES = (('guest', 'Guest'),
                ('customer', 'Customer'),
                ('staff', 'Staff'),
                ('manager', "Manager"),
                ('admin', 'Admin')
)

    phone_number = models.CharField(max_length=20, unique=True, verbose_name="Telefon nomeri")
    
    email = models.EmailField()

    full_name = models.CharField(max_length=50)

    role = models.CharField()

    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ["phone_number"]

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        blank=True,
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_set",
        blank=True,
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.username

