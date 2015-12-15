from django.db import models
from django.db.models import Max
from random import randint

# Create your models here.
class Author(models.Model):
    author_last = models.CharField(max_length=200, blank=True, null=True)
    author_first = models.CharField(max_length=200)
    author_middle = models.CharField(max_length=200, blank=True, null=True)
    
    def full_name(self):
        string_name = self.author_first
        if self.author_middle is not None:
            middle_name = self.author_middle
            if len(middle_name) == 1:
                middle_name = middle_name + '.'
            string_name = string_name + " " + middle_name
        if self.author_last is not None:
            string_name = string_name + " " + self.author_last
        return string_name

    def __unicode__(self):
        string_name = self.author_first
        if self.author_middle is not None:
            middle_name = self.author_middle
            if len(middle_name) == 1:
                middle_name = middle_name + '.'
            string_name = string_name + " " + middle_name
        if self.author_last is not None:
            string_name =  self.author_last + ', ' + string_name
        return string_name
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
    source_type = models.ForeignKey(SourceType)
    release_date = models.DateField(blank=True, null=True)
    parent_source = models.ForeignKey('self', blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.title
    class Meta:
        ordering = ['title']

class Quote(models.Model):
    quote_content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(QuoteGenre)
    author = models.ForeignKey(Author, blank=True, null=True)
    source = models.ForeignKey(Source)
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

    @staticmethod
    def get_random(latest_daily_quote_id = None):
        max_id = DailyQuote.objects.aggregate(Max('id'))['id__max']
        if latest_daily_quote_id is None:
            latest_daily_quote_id = DailyQuote.objects.all().order_by('-id')[:1][0].pk
        random_daily_quote = None
        while random_daily_quote is None or random_daily_quote.pk == latest_daily_quote_id:
            try:
                random_daily_quote = DailyQuote.objects.get(pk=randint(1, max_id))
            except DailyQuote.DoesNotExist:
                pass
        return random_daily_quote

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










