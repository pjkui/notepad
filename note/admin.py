from django.contrib import admin

# Register your models here.
from note.models import Note
from note.models import User
from note.models import NoteAuthor

admin.site.register(Note)
admin.site.register(NoteAuthor)
admin.site.register(User)
