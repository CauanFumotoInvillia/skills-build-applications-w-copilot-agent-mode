from djongo import models


class Activity(models.Model):
    # Use a simple integer duration (minutes) to match the population script
    _id = models.ObjectIdField(primary_key=True, db_column='_id')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.IntegerField(help_text='Duration in minutes')
    distance = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} by {self.user.username} on {self.date}"