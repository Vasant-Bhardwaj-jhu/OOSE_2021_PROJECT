from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    address1 = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    state = models.CharField(max_length=200, default="")
    country = models.CharField(max_length=200, default="")
    music = models.IntegerField(null=True, default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    visual = models.IntegerField(null=True, default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    performing = models.IntegerField(null=True, default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    film = models.IntegerField(null=True, default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    lectures = models.IntegerField(null=True, default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    fashion = models.IntegerField(null=True, default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    food = models.IntegerField(null=True, default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    festivals = models.IntegerField(null=True, default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    charity = models.IntegerField(null=True, default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sports = models.IntegerField(null=True, default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    nightlife = models.IntegerField(null=True, default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    family = models.IntegerField(null=True, default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])


class Event(models.Model):
    name = models.TextField(default="")
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    start_time_display = models.DateTimeField(null=True)
    end_time_display = models.DateTimeField(null=True)
    duration = models.DurationField(null=True, blank=True)
    category = models.CharField(max_length=200, default="")
    picture = models.URLField(max_length=300, null=True, blank=True)
    tickets = models.URLField(max_length=300, null=True, blank=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    description = models.TextField(null=True, blank=True)
    address1 = models.TextField(default="")
    city = models.TextField(default="")
    state = models.TextField(default="")
    country = models.TextField(default="")
    zip_code = models.TextField(default="")
    temporary = models.BooleanField(default=True)
    attendees = models.ManyToManyField("User", related_name="attending")

    def __str__(self):
        return f"Event {self.id}: {self.name}"

    def __hash__(self):
        return hash(self.name)