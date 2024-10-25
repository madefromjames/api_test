import uuid
from django.db import models
from cart.models import Cart
from django.utils import timezone

# Create your models here.
def order_code():
    return f'ORD{str(uuid.uuid4())[:8]}'

class Order(models.Model):
    class Status(models.TextChoices):
        PROCESSING = 'PROCESSING', "Processing"
        PACKAGING = 'PACKAGING', "Packaging"
        DISPATCHED = 'DISPATCH', "Dispatch"
        DELIVERED = 'DELIVERED', "Delivered"
        CANCELLED = 'CANCELLED', "Cancelled"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    code = models.CharField(max_length=15, default=order_code, editable=False, unique=True)
    time = models.DateTimeField(default=timezone.now)
    payment = models.BooleanField(default=False)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PROCESSING)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    delivery_address = models.TextField(blank=True, null=True)
    dispatched_at = models.DateTimeField(blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.status == self.Status.DISPATCHED:
            self.dispatched_at = timezone.now()
        elif self.status == self.Status.DELIVERED:
            self.delivered_at = timezone.now()
        elif self.status == self.Status.CANCELLED:
            self.payment = False
            self.dispatched_at = None
            self.delivered_at = None
        if self.payment:
            self.status = self.Status.PROCESSING
        self.total = sum(item.total for item in self.cart.cart_items.all())
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.code