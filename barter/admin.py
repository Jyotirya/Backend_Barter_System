from django.contrib import admin
from .models import Item, BarterLogs

# Register your models here.
class BarterItemAdmin(admin.ModelAdmin):
    list_display = (
        "itemId",
        "name",
        "seller",
        "deadline",
        "timeCreated",
        "status"
    )
    # list_filter = ("is_active",)
    search_fields = ("name", "itemId", "seller")

admin.site.register(Item, BarterItemAdmin)
admin.site.register(BarterLogs)