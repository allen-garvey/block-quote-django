from django.db import models
from django.utils.encoding import force_bytes

# Create your models here.
class Author(models.Model):
    author_last = models.CharField(max_length=200, blank=True, null=True)
    author_first = models.CharField(max_length=200)
    author_middle = models.CharField(max_length=200, blank=True, null=True)
    def __unicode__(self):
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
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

class QuoteGenre(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

class Source(models.Model):
    author = models.ForeignKey(Author, blank=True, null=True)
    title = models.CharField(max_length=200)
    source_type = models.ForeignKey(SourceType)
    release_date = models.DateField(blank=True, null=True)
    parent_source = models.ForeignKey('self', blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.title

class Quote(models.Model):
    quote_content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(QuoteGenre)
    author = models.ForeignKey(Author, blank=True, null=True)
    source = models.ForeignKey(Source)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.quote_content

class DailyQuote(models.Model):
    quote = models.ForeignKey(Quote)
    date_used = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return str(self.quote.id) + ' ' + self.date_used.strftime('%m/%d/%Y %H:%M')










