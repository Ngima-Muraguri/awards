from django.db import models
import datetime
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='images/')
    bio =models.TextField()
    contact = models.CharField(max_length=22)

    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.save()


class Projects(models.Model):
    title = models.CharField(max_length=122)
    image = models.ImageField(default='default.jpg', upload_to='images/')
    description = models.TextField()
    live_link = models.URLField(max_length=222, default='url')
    posted_by = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE )
    date_posted = models.DateTimeField(auto_now_add=True)

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()


    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects


    def __str__(self):
        return self.title