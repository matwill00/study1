from django.db import models
class Resume(models.Model):
    email = models.CharField(max_length=255)
    test = models.TextField()


