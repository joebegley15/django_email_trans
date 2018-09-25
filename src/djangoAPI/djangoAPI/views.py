from django.http import HttpResponse
from django.shortcuts import render

def email(req):
	return render(req,"index.html")