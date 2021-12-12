from django.contrib import admin

# Register your models here.
from .models import Contact, Record, Photo,  Nxt_Match, New, Videos,UpComingMatches

admin.site.register(Contact)
admin.site.register(Record)
admin.site.register(Photo)
admin.site.register(Nxt_Match)
admin.site.register(New)
admin.site.register(Videos)
admin.site.register(UpComingMatches)





