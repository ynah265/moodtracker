from django.db import models

class MoodEntry(models.Model):
    mood = models.CharField(max_length=50)
    journal_entry = models.TextField()

    def __str__(self):
        return self.mood
