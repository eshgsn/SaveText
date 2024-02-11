from django.db import models
import datetime
import uuid

# Create your models here.

class Users(models.Model):
    name = models.CharField(
        max_length=30, blank=False, null=False
    )
    email = models.CharField(
        max_length= 30, blank=False, null= False, unique=True
    )
    password = models.CharField(
        max_length=16, blank=False, null=False
    )
    userId = models.UUIDField(
        blank=False,null=False, default=uuid.uuid4(), unique=True
    )
    createdAt = models.DateTimeField(
        null=False, blank=False, default=datetime.datetime.now()
    )
    updatedAt = models.DateTimeField(
        null=False, blank=False, default=datetime.datetime.now()
    )


class UserData(models.Model):
    dataId = models.UUIDField(
        blank=False,null=False, default=uuid.uuid4(), unique=True
    )
    fileName = models.CharField(
        max_length=30, blank=False, null=False
    )
    textFile = models.TextField(
         blank=True, null= True
    )
    ownerUserId = models.UUIDField(
        blank=False,null=False 
    )
    createdAt = models.DateTimeField(
        null=False, blank=False, default=datetime.datetime.now()
    )
    updatedAt = models.DateTimeField(
        null=False, blank=False, default=datetime.datetime.now()
    )
    
    
