from django.contrib import admin
from tallynewapp.models import Godowns,StockCategory,Stockgroup,Taxability,Unit,Gst
# Register your models here.
admin.site.register(Godowns)
admin.site.register(StockCategory)
admin.site.register(Stockgroup)
admin.site.register(Taxability)
admin.site.register(Unit)
admin.site.register(Gst)
