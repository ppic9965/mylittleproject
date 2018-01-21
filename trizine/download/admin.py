from django.contrib import admin

# Register your models here.
from .models import WebzineDown

class WebzineAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title"]

    class Meta:
        model = WebzineDown

admin.site.register(WebzineDown, WebzineAdmin)