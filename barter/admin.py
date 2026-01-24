from django.contrib import admin
from .models import Item, BarterLog, Wishlist, ItemImage

# Register your models here.
class BarterItemAdmin(admin.ModelAdmin):
    list_display = (
        "itemId",
        "name",
        "seller",
        "deadline",
        "timeCreated",
    )
    search_fields = ("name", "itemId", "seller")

admin.site.register(Item, BarterItemAdmin)
admin.site.register(BarterLog)
admin.site.register(Wishlist)
admin.site.register(ItemImage)