from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Customer(AbstractUser):
    phone_number = models.CharField(max_length=15)

    groups = models.ManyToManyField(
        Group,
        related_name = 'customer_set',
        blank = True,
        help_text = 'The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name = 'customer_set',
        blank = True,
        help_text = 'Specific permissions for this user.',
    )

    def __str__(self):
        return self.username
    
    