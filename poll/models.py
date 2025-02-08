from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

class Poll(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    

    def __str__(self) -> str:
        return self.name
  
class Choice(models.Model):
    text = models.CharField(max_length=50)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, blank=True, related_name='choices')

    def __str__(self) -> str:
        return self.text    

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.user +"  "+ self.choice