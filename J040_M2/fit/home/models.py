from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    assigned_by = models.CharField(max_length=20)

    def __str__(self):
        return self.name
