from django.shortcuts import render

import re
from urllib2 import Request, urlopen
from urllib import urlencode

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect

import django.contrib.auth as auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext, loader

# Create your views here.
def index(request):
	#template = loader.get_template('spotlightapp/index.html')

	result = True
	context = RequestContext(request, {
		'result': result
		})

	#return HttpResponse(template.render(context))
	return HttpResponse("whatever")
