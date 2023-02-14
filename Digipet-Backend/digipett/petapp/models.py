from django.db import models
from django.contrib.auth.models import AbstractUser

from ckeditor.fields import RichTextField



class UserModel(AbstractUser):


    
    
    realibility_number = models.IntegerField(null=True, blank = True, default = 100)
    
    

    class Meta:
        verbose_name = 'MY-USERS'
        verbose_name_plural= 'USER-MODEL'
    


class PetModel(models.Model):

    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, null = True, related_name='MY_PETS')
    choices = [
            ('CAT','CAT'),
            ('DOG','DOG'),
            ('FISH','FISH'),

    ]

    from datetime import datetime
    pet_name = models.CharField(max_length=50)

    nickname = models.CharField(blank=True, max_length=50, default = None)
    
    

    category = models.CharField(choices=choices,blank = True, max_length=20 ) 
    
    story = RichTextField(blank=True,max_length=5000)

    pet_img = models.ImageField(upload_to = 'media',blank = True)

    sleep_level = models.FloatField(default = 10)
    hunger_level = models.FloatField(default = 10)
    happiness_level = models.FloatField(default=10)
    water_level = models.FloatField(default=10)

    hp_level = models.FloatField(default=10)

    eating_time = models.DateTimeField(auto_now = False, default =datetime.now())
    sleep_time = models.DateTimeField(auto_now=False,default =datetime.now())
    pet_time = models.DateTimeField(auto_now = False,default =datetime.now())

    water_time = models.DateTimeField(auto_now=False,default =datetime.now())

    pet_active = models.BooleanField(default=True)
## auto_add_now

    ##sevme,uyuma,yedirme fonksiyonları
    ##tarih farkı fonksiyonları 

    #algoritmayı arkada backend yapmalı.
    
        
   

    class Meta:
        verbose_name = 'MY-PETS'
        verbose_name_plural= 'PET-MODEL'

    def __str__(self):
        return self.pet_name
  

    
    




    