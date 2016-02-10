# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.


'''@python_2_unicode_compatible     # only if you need to support Python 2
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)'''
        

@python_2_unicode_compatible     # only if you need to support Python 2        
class Post(models.Model):
    #auth.user из приложения(файла) auth
    author = models.ForeignKey('auth.User',)
    title = models.CharField(max_length=120, unique=True)
    category = models.CharField(max_length=50)
    text = models.TextField()
    views = models.IntegerField(default=0)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
 #todo       
class User(models.Model):
    pass

                           
                                                                                 