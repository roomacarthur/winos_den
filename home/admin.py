from django.contrib import admin
from .models import ContactUs, NewsLetter


# Register your models here.
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'submitted_on',
        'name',
        'email',
        'message',
    )
    list_filter = (
        'name',
        'email',
    )
    search_fields = (
        'submitted_on',
        'name',
        'email',
    )

    ordering = ('-submitted_on',)


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'signed_up_on',
    )
    list_filter = (
        'email',
        'signed_up_on',
    )
    search_fields = (
        'email',
        'signed_up_on',
    )

admin.site.register(ContactUs, ContactAdmin)
admin.site.register(NewsLetter, NewsLetterAdmin)
