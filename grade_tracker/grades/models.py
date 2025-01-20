from django.db import models

class Grade(models.Model):
    subject = models.CharField(max_length=100)
    grade = models.FloatField()

    def __str__(self):
        return f"{self.subject}: {self.grade}"
