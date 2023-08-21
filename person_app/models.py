from django.db import models

# Create your models here.
class Person(models.Model): 
    last_name = models.TextField() 
    first_name = models.TextField()

    def __str__(self): 
        return f'{self.last_name}, {self.first_name}'
    
class Reservation (models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Phone number', max_length=200)
    booking_time = models.DateTimeField(auto_now=True)
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name