from django.db import models


class Resume(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    resume = models.TextField()


class Gear_order(models.Model):
    client_name = models.CharField(max_length=30)
    client_email = models.EmailField()
    order_name = models.TextField()
    order_drawing = models.ImageField()


class Rack_neck_order(models.Model):
    client_name = models.CharField(max_length=30)
    client_email = models.EmailField()
    order_name = models.TextField()
    order_drawing = models.ImageField()


class Worm_gear_order(models.Model):
    client_name = models.CharField(max_length=30)
    client_email = models.EmailField()
    order_name = models.TextField()
    order_drawing = models.ImageField()
