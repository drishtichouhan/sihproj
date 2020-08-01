from django.db import models

# Create your models here.

class User(abstractUser):
	USER_TYPE_CHOICES = (

		(1,'complainant'),
		(2,'volunteer'),
		(3,'sho'),
	)
	user_type = models.PositiveSmallIntergerField(choices=USER_TYPE_CHOICES)


class complainant(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

class volunteer(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

class sho(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)