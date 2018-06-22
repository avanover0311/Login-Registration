from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Registration, LoginManager


def index(request):
    response = "Hello, I am your first request!"
    return render(request, 'first_apps/index.html')

def create(request):
	print(request.POST)
	errors = Registration.objects.basic_validate(request.POST)

	if len(errors):
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		Registration.objects.create(first_name=request.POST['first_name'],
			last_name=request.POST['last_name'],email=request.POST['email'],
			password=request.POST['password']) 
		return redirect('/')

def login(request):
	print(request.POST)

	err = LoginManager.objects.basic_validate(request.POST)
	print(err)

	if err:
		for key, value in err.items():
			print('key:', key, 'value:', value)
			messages.errors(request, value)

	return redirect('/')			


def update(req, id):

	user =User.objects.get(id = id)
	user.last_name = 'changed name'
	user.save()
	print(user)
	return redirect('/')


