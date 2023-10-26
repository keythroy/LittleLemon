from django.db import models

class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.Name} with {self.No_of_guests} guests at {self.BookingDate}"
    
class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Inventory = models.IntegerField()
    
    def __str__(self) -> str:
        return self.Title