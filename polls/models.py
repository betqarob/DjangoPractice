import datetime
from django.db import models
from django.utils import timezone

# Class for Questions
class Question(models.Model):
    text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date quetsion was published')

    def __str__(self):
        return self.text
    
    #checks if the question was published recently 
    def published_recent(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Class for Choices
class Choice(models.Model):
    #Creates an instance of the question from the question class 
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    
    choice_text = models.CharField(max_length = 200)
    
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text