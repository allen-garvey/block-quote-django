from django.contrib import admin

# Register your models here.
from .models import Author
from .models import QuoteGenre
from .models import SourceType

admin.site.register(Author)
admin.site.register(QuoteGenre)
admin.site.register(SourceType)