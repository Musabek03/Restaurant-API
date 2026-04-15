from django.db import models

class Table(models.Model):

    number = models.CharField(max_length=30)
    capacity = models.PositiveIntegerField(verbose_name="Stolga neshe adam siyiwi")
    location = models.CharField(max_length=80)
    is_active = models.BooleanField(default=True)



