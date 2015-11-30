from django.db import models

# Create your models here.
class Author(models.Model):
    author_last = models.CharField(max_length=200, blank=True, null=True)
    author_first = models.CharField(max_length=200)
    author_middle = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
    	string_name = self.author_first
    	if self.author_middle is not None:
    		middle_name = self.author_middle
    		if len(middle_name) == 1:
    			middle_name = middle_name + '.'
    		string_name = string_name + " " + middle_name
    	if self.author_last is not None:
    		string_name = string_name + " " + self.author_last
		return string_name

class SourceType(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):              # __unicode__ on Python 2
		return self.name

class QuoteGenre(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):              # __unicode__ on Python 2
		return self.name