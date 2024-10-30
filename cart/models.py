from django.db import models
from product.models import Product
from customer.models import Customer
import uuid

# Create your models here.
class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return sum([item.total for item in self.cart_items.all()])
    
    def __str__(self):
        return f"Cart of {self.user.username}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        if self.product:
            return self.product.price * self.quantity
        return 0.0
    
    def __str__(self):
        return f"{self.product.name} (Qty {self.quantity})"
    
    class Meta:
        ordering = ['date_added']
    
    