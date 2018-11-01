from django.db import models
import datetime
from django.utils.timezone import now
from datetime import datetime
# Create your models here.



class Message(models.Model):
	talker = models.CharField(max_length=20)
	message = models.CharField(max_length=128)
	time = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.talker + " " + self.message

class Work(models.Model):
	name = models.CharField(max_length=64)
	img = models.CharField(max_length=64, default = "cover.png")
	classname = models.CharField(max_length=64, default = "portfolio-wrapper1")
	classification = models.CharField(max_length=64, default = "Others")

	def __str__(self):
		return self.name

class Comment(models.Model):
	author = models.CharField(max_length=20)
	comment = models.CharField(max_length=128)
	work = models.ForeignKey(Work, on_delete=models.CASCADE,default=1)

	def __str__(self):
		return self.author + " " + self.comment

# class ReplyMessage(models.Model):
#     orginalMessage = models.ForeignKey(Message, on_delete=models.CASCADE)
#     talker = models.CharField(max_length=20)
#     content = models.CharField(max_length=128)

#     def __str__(self):
#         return self.orginalMessage.message + '-' + str(self.id)