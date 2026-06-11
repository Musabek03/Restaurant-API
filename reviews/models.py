from django.db import models
from accounts.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator



class Review(models.Model):
    customer = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5),
    ],
    verbose_name="rating")

    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)