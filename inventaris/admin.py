from django.contrib import admin
from .models import (
    Kategori,
    Supplier,
    Lokasi,
    Barang,
    Inventory,
    StockMovement
)


admin.site.register(Kategori)
admin.site.register(Supplier)
admin.site.register(Lokasi)
admin.site.register(Barang)
admin.site.register(Inventory)
admin.site.register(StockMovement)