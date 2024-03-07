from django.db import models

# Create your models here.

class Shift(models.Model):
    SHIFT_CHOICES = (
        ('Day', 'Day Shift'),
        ('Night', 'Night Shift'),
    )
    shift_type = models.CharField(max_length=10, choices=SHIFT_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.shift_type

class Employee(models.Model):
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    joining_date = models.DateTimeField(null=True,blank=True)
    is_available = models.BooleanField(default=True)
    shift_type = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name

class Ticket(models.Model):
    number = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    resolution_end_date = models.DateTimeField(null=True, blank=True)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.number