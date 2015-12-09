from django.shortcuts import render

# Create your views here.
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from .models import DailyQuote
from .models import Quote
from django.utils import timezone

def index(request):
    return HttpResponse("Hello, world. You're at the quotes index.")

def daily_quote(request):
	latest_daily_quote = DailyQuote.objects.all().order_by('-id')[:1]
	if(latest_daily_quote[0].date_used.date() >= timezone.now().date()):
		todays_quote = latest_daily_quote[0].to_dict()
	else:
		todays_quote = {}
	todays_quote = latest_daily_quote[0].to_dict()
	return JsonResponse(todays_quote)