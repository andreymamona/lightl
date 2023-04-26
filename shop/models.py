from django.conf import settings
from django.db import models
from django.db.models import ImageField


class Product(models.Model):
    external_id = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    price_usd = models.FloatField(default=0)
    image = ImageField(upload_to="products/", default="default_img.jpg")
    description = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f'Product: {self.title} Price: {self.price}'
