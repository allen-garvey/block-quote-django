from django.db import models
from django.db.models import Max
from random import randint
import re

# Create your models here.
class Author(models.Model):
    author_last = models.CharField(max_length=200, blank=True, null=True, default=None)
    author_first = models.CharField(max_length=200)
    author_middle = models.CharField(max_length=200, blank=True, null=True, default=None)
    
    def middle_name(self):
        if self.author_middle:
            middle_name = self.author_middle
            if len(middle_name) == 1:
                middle_name = middle_name + '.'
            return middle_name
        else:
            return None

    def full_name(self):
        string_name = self.author_first
        if self.author_middle:
            string_name = string_name + " " + self.middle_name()
        if self.author_last:
            string_name = string_name + " " + self.author_last
        return string_name

    def list_name(self):
        string_name = self.author_first
        if self.author_middle:
            string_name = string_name + " " + self.middle_name()
        if self.author_last:
            string_name =  self.author_last + ', ' + string_name
        return string_name

    def __unicode__(self):
        return self.list_name()
    class Meta:
        ordering = ['author_last', 'author_first', 'author_middle']

class SourceType(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name
    class Meta:
        ordering = ['name']

class QuoteGenre(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name
    class Meta:
        ordering = ['name']

class Source(models.Model):
    author = models.ForeignKey(Author, blank=True, null=True)
    title = models.CharField(max_length=200)
    sort_title = models.CharField(max_length=200, editable=False, null=True)
    source_type = models.ForeignKey(SourceType)
    release_date = models.DateField(blank=True, null=True)
    parent_source = models.ForeignKey('self', blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True, default=None)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.title
    def save(self, *args, **kwargs):
        if self.sort_title == None:
            self.sort_title = re.sub(r'^\s*(a|an|the)?\s+', '', self.title, 0, re.IGNORECASE)
        super(Source, self).save(*args, **kwargs)
    class Meta:
        ordering = ['sort_title']

class Quote(models.Model):
    quote_content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(QuoteGenre)
    author = models.ForeignKey(Author, blank=True, null=True)
    source = models.ForeignKey(Source)
    
    @staticmethod
    def get_random(latest_quote_id = -1):
        max_id = Quote.objects.aggregate(Max('id'))['id__max']
        random_quote = None
        while random_quote is None or random_quote.pk == latest_quote_id:
            try:
                random_quote = Quote.objects.get(pk=randint(1, max_id))
            except Quote.DoesNotExist:
                pass
        return random_quote

    def __unicode__(self):              # __unicode__ on Python 2
        return self.quote_content

    def get_author(self):
        if self.author is not None:
            return self.author
        elif self.source.author is not None:
            return self.source.author
        else:
            return self.source.parent_source.author

class DailyQuote(models.Model):
    quote = models.ForeignKey(Quote)
    date_used = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        quote_author = self.quote.get_author()
        return {
                'id' : self.id,
                'datetime' : self.date_used,
                'quote' : {
                        'id'   : self.quote.id,
                        'body' : self.quote.quote_content,
                        'author' : {
                                    'first' : quote_author.author_first,
                                    'middle' : quote_author.author_middle,
                                    'last' : quote_author.author_last,
                                    'full_name' : quote_author.full_name()
                                },
                        'source' : self.quote.source.title            
                    }
                }
    def __unicode__(self):              # __unicode__ on Python 2
        return str(self.quote.id) + ' ' + self.date_used.strftime('%m/%d/%Y %H:%M')










