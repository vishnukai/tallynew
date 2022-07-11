from django.urls import path,include
from.import views

 
urlpatterns = [
    path('',views.home,name='home'),
    path('stock_grp',views.stock_grp,name='stock_grp'),
    path('groupalter/<int:id>',views.groupalter,name='groupalter'),
    path('editunit',views.editunit,name='editunit'),
    path('editgodown',views.editgodown,name='editgodown'),
    path('stockcat',views.stockcat,name='stockcat'),
    path('newgroupemploye',views.newgroupemploye,name='newgroupemploye'),
    path('stockgroup',views.stockgroup,name='stockgroup'),
]