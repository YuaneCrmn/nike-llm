from django.db import models
from django.contrib.auth.models import User

SHIRT_SIZES = [
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
]

SHIRT_COLORS = [
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ('white', 'White'),
]

class Shirt(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shirts')
    size = models.CharField(max_length=10, choices=SHIRT_SIZES, default='S')
    color = models.CharField(max_length=10, choices=SHIRT_COLORS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} Shirt by {self.user.username}"
    