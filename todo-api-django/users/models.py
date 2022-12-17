from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    realname = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    code = models.CharField(max_length=4, default="")#para verificar con un código que se envíe por sms un menaje de 4 dígitos 
    is_verify = models.BooleanField(default=False) #para throlled
    
    class Meta:
        db_table = "users_apps"
