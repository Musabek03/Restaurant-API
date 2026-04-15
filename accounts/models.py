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
    
    email = models.EmailField(unique=True)

    full_name = models.CharField(max_length=50)

    role = models.CharField(max_length=30, choices=ROLE_CHOICES)

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


class Profile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profiles')
    avatar = models.ImageField(upload_to="images/avatars/", null=True, blank=True)
    birthday = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

