from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

class CustomUser(AbstractUser):

    ROLE_CHOICES = (('guest', 'Guest'),
                ('customer', 'Customer'),
                ('staff', 'Staff'),
                ('manager', "Manager"),
                ('admin', 'Admin')
)
    username = None

    phone_number = models.CharField(max_length=20, unique=True, verbose_name="Telefon nomeri")
    
    email = models.EmailField(blank=True, null=True)

    full_name = models.CharField(max_length=50)

    role = models.CharField(max_length=30, choices=ROLE_CHOICES)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

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
    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number


class Profile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to="images/avatars/", null=True, blank=True)
    birthday = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

