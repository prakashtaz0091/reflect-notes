from django.db import models
from django.forms import CharField
from ckeditor.fields import RichTextField


class Question(models.Model):

    question = models.TextField()
    answer = RichTextField(null=True,blank = True)
    approved = models.BooleanField(default=False)


    def __str__(self):
        return self.question


