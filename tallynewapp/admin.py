from django.contrib import admin
from tallynewapp.models import Godowns,StockCategory,Stockgroup,Taxability,Unit,Gst,Unitcode,Type
# Register your models here.
admin.site.register(Godowns)
admin.site.register(StockCategory)
admin.site.register(Stockgroup)
admin.site.register(Taxability)
admin.site.register(Unit)
admin.site.register(Gst)
admin.site.register(Unitcode)
admin.site.register(Type)
