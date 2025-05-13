from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    organizer = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    attendees = models.JSONField(default=list)
    
    def __str__(self):
        return self.title