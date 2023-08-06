from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))
 
class Post(models.Model):
    title = models.CharField(max_length=210, unique=True)
    slug = models.SlugField(max_length=210, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
    

class Booking(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.PositiveIntegerField()
    comments = models.TextField(blank=True)
    canceled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"

    def clean(self):
        # Check for double booking
        if self.pk is None:  # Only check for new instances (not updating)
            conflicting_bookings = Booking.objects.filter(
                date=self.date,
                time=self.time,
                canceled=False
            )
            if conflicting_bookings.exists():
                raise ValidationError("This time slot is already booked.")

    def cancel_booking(self):
        if not self.canceled:
            self.canceled = True
            self.save()

    def is_cancellable(self):
        return not self.canceled


class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    table_limit = models.IntegerField()

class Menu(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

