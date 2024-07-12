from django.db import models

class Product(models.Model):
    UNIT_CHOICES = [
        ('kg', 'Kilograms'),
        ('pcs', 'Pieces'),
        ('m', 'Meters'),
    ]

    name = models.CharField(max_length=100, unique=True)  # Added unique=True
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)

    def __str__(self):
        return self.name

    def is_low_stock(self):
        return self.quantity < 5  # Define threshold for low stock

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name