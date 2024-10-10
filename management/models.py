from django.db import models

# Create your models here.


class Equipment(models.Model):
    name = models.CharField(max_length=255, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    flag = models.BooleanField(default=True, help_text="Whether its active or not")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
