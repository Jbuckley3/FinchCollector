from django.db import models
from django.urls import reverse
from datetime import date

# The Toy model for our ManyToMany relationship
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.color} {self.name}'

    def get_absolute_url(self):
        return reverse('toy_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Feeding(models.Model):
    MEALS = [
        ('SEEDS', 'Seeds'),
        ('INSECTS', 'Insects'),
        ('FRUITS', 'Fruits'),
        # Add more choices as needed
    ]

    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=10,
        choices=MEALS,
        default=MEALS[0][0]
    )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date} for {self.finch}"

    class Meta:
        ordering = ['-date']
