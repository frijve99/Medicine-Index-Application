from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=200)
    generic_name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=4)
    batch_number = models.CharField(max_length=100)
    other_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name