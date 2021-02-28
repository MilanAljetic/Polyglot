from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Language_nativ(models.Model):
    language = models.CharField(max_length=20)
    flag = models.ImageField(upload_to='state_flag', blank=True)

    def __str__(self):
        return self.language


class Language_learn(models.Model):
    language = models.CharField(max_length=20)
    flag = models.ImageField(upload_to='state_flag', blank=True)

    def __str__(self):
        return self.language

class User_profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    language_nativ = models.ForeignKey(Language_nativ, on_delete=models.CASCADE, null=True)
    language_learn = models.ForeignKey(Language_learn, on_delete=models.CASCADE, null=True)
    picture = models.ImageField(upload_to='user_image', blank=True)
    logged = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return str(self.name)


class Group(models.Model):
    author = models.ForeignKey(User_profile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User_profile, null=True, related_name='names')
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
    
    
class Group_post(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30, null=True)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title

RATE_USER = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]

class Rate(models.Model):
    user = models.ForeignKey(User_profile, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=200)
    rate = models.PositiveIntegerField(choices = RATE_USER, blank=True, null=True)

    def __str__(self):
        return self.text