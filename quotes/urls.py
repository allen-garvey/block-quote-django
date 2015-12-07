from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^daily-quote/?$', views.daily_quote, name='daily_quote'),
    url(r'^$', views.index, name='index'),
]

admin.site.site_header = "Block Quote 2 Administration"
admin.site.site_title = "Block Quote 2 Admin"