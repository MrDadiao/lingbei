from django.shortcuts import render, render_to_response, HttpResponse
from django.http import HttpResponse
from django.db.models import Q
from django import forms
from .models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

class UserForm(forms.Form):
	username = forms.CharField(label='用户名', max_length=50)
	password = forms.CharField(label='密码', widget=forms.PasswordInput())


def login(request):
	if request.method == 'POST':
		userform = UserForm(request.POST)
		if userform.is_valid():
			username = userform.cleaned_data['username']
			password = userform.cleaned_data['password']
			
			user = User.objects.filter(username__exact=username, password__exact=password)
			
			if not user:
				username = userform.cleaned_data['username']
				password = userform.cleaned_data['password']
				
				User.objects.create(username=username, password=password)
	
	
	else:
		userform = UserForm()
	return render_to_response('login.html', {'userform': userform})




# Create your views here.
