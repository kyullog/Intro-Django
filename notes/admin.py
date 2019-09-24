# Register models here to have them show up in the admin view

from django.contrib import admin
from .models import Note, PersonalNote
# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')


admin.site.register((Note, PersonalNote), NoteAdmin)
