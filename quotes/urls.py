from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^daily-quote/?$', views.daily_quote, name='daily_quote'),
    url(r'^$', views.index, name='index'),
]