from __future__ import unicode_literals
from django.db import models
import bcrypt

# Create your models here.
class RegisterManager(models.Manager):
	def basic_validate(self, postData):
		errors={}
		if len(postData['email_login']) < 4:
			errors['email']	= 'Email must contain 4 characters'
		if len(postData['password']) < 8:
			errors['password'] = 'Password must contain 8 characters'
		return errors


class Registration(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


	objects = RegisterManager()


class LoginManager(models.Manager):
	def basic_validate(self, postData):
		error = {}
		user = Login.objects.filter(email=postData['email_login'])
		if user:
			user =Login.objects.get(email=postData['email_login'])

		if not user.password == postData['password']:
			return error
		else:
			error['user_exists'] = 'Email and password does not match'
		
		return error

	objects = RegisterManager()
