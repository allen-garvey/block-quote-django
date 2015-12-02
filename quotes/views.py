from django.shortcuts import render

# Create your views here.
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from .models import DailyQuote

def index(request):
    return HttpResponse("Hello, world. You're at the quotes index.")

def daily_quote(request):
	# daily_quote = DailyQuote.objects.order_by('date_used')[:1]
	daily_quote = DailyQuote.objects.all()
	return JsonResponse(serializers.serialize("json", DailyQuote.objects.all()))