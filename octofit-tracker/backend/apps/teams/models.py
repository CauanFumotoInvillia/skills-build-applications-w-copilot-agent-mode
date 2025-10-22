from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TeamActivity(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=100)
    date = models.DateField()
    duration = models.DurationField()

    def __str__(self):
        return f"{self.activity_name} - {self.team.name}"