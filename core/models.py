from django.db import models
import uuid

#don't Delete Default model 
class Default(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)