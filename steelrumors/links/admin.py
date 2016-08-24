from django.contrib import admin
from .models import Link, Vote


class LinkAdmin(admin.ModelAdmin):
    pass


class VoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Link, LinkAdmin)
admin.site.register(Vote, VoteAdmin)
