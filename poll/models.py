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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='polls')
    description = models.TextField()

    @property
    def total_vote(self):
        return sum(i.vote_count for i in self.choices.all())

    def __str__(self) -> str:
        return self.name

  
class Choice(models.Model):
    text = models.CharField(max_length=50)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, blank=True, related_name='choices')
    vote_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.text    

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self) -> str:
        return f'{self.user} {self.choice}'