from django.db import models

class Payment(models.Model):
    currency = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.currency} {self.amount} - {self.description[:50]}"
