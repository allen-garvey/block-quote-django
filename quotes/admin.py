from django.contrib import admin

# Register your models here.
from .models import Author
from .models import QuoteGenre
from .models import SourceType
from .models import Source
from .models import Quote
from .models import DailyQuote

admin.site.register(Author)
admin.site.register(QuoteGenre)
admin.site.register(SourceType)
admin.site.register(Source)
admin.site.register(Quote)
admin.site.register(DailyQuote)