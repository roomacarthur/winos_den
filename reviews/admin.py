from django.contrib import admin
from .models import Reviews
# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
    )

admin.site.register(Reviews, ReviewAdmin)
