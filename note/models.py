from django.db import models

# Create your models here.
class  Note(models.Model):
	title=models.CharField(max_length=60)
	color=models.CharField(max_length=10)
	author_id=models.IntegerField()
	noteType=models.IntegerField()
	createTime=models.DateTimeField()
	publish=models.DateTimeField()
	content=models.TextField()

class User(models.Model):
	username=models.CharField(max_length=40)
	password=models.CharField(max_length=40)
	nickname=models.CharField(max_length=40)
	loginIP=models.CharField(max_length=12)

class NoteAuthor(models.Model):
	userID=models.ForeignKey(User)
	noteID=models.ForeignKey(Note)
