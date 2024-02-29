from django.db import models

class Phone(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    issue = models.TextField()
    repair_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.brand} {self.model}"

class RepairService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
