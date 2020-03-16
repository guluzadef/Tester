from base_user.models import MyUser
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
User = MyUser


class Team(models.Model):
    text=RichTextUploadingField()

    def __str__(self):
        return f'{self.text},{self.id}'


class FB(models.Model):
    text=models.CharField(max_length=255)


    def __str__(self):
        return f'{self.text}'