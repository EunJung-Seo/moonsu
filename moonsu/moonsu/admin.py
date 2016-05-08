from django.contrib import admin

from moonsu.models import Phrase


@admin.register(Phrase)
class PhraseModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'content',
    )
