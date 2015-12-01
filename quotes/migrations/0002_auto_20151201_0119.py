# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyQuote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_used', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote_content', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(to='quotes.Author')),
                ('genre', models.ForeignKey(to='quotes.QuoteGenre')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('release_date', models.DateField(null=True, blank=True)),
                ('url', models.CharField(max_length=200, null=True, blank=True)),
                ('author', models.ForeignKey(to='quotes.Author')),
                ('parent_source', models.ForeignKey(blank=True, to='quotes.Source', null=True)),
                ('source_type', models.ForeignKey(to='quotes.SourceType')),
            ],
        ),
        migrations.AddField(
            model_name='quote',
            name='source',
            field=models.ForeignKey(to='quotes.Source'),
        ),
        migrations.AddField(
            model_name='dailyquote',
            name='quote',
            field=models.ForeignKey(to='quotes.Quote'),
        ),
    ]
