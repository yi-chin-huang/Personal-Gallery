from django.db import models

# Create your models here.



class Message(models.Model):
	talker = models.CharField(max_length=20)
	message = models.CharField(max_length=128)

	def __str__(self):
		return self.talker + " " + self.message
# class ReplyMessage(models.Model):
#     orginalMessage = models.ForeignKey(Message, on_delete=models.CASCADE)
#     talker = models.CharField(max_length=20)
#     content = models.CharField(max_length=128)

#     def __str__(self):
#         return self.orginalMessage.message + '-' + str(self.id)