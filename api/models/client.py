from django.db import models


class Client(models.Model):

    referral = models.ForeignKey('Agent', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    phone = models.CharField(max_length=16)
    passport = models.CharField(max_length=11)
    score = models.IntegerField()
