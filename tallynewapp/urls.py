from django.urls import path,include
from.import views

 
urlpatterns = [
    path('',views.home,name='home'),
    path('stock_grp',views.stock_grp,name='stock_grp'),
    path('stock_cat',views.stock_cat,name='stock_cat'),
    path('groupalter/<int:id>',views.groupalter,name='groupalter'),
    path('editunit',views.editunit,name='editunit'),
    path('editgodown',views.editgodown,name='editgodown'),
    
    path('newgroupemploye',views.newgroupemploye,name='newgroupemploye'),
    path('stockgroup',views.stockgroup,name='stockgroup'),
    path('units',views.units,name='units'),
    path('savegrp/<int:id>',views.savegrp,name='savegrp'),
    path('creategrp',views.creategrp,name='creategrp'),
    path('stock_items',views.stock_items,name='stock_items'),
    path('editcat/<int:id>',views.editcat,name='editcat'),
    path('savecat/<int:id>',views.savecat,name='savecat'),
    path('editunit/<int:id>',views.editunit,name='editunit'),
    path('saveunit/<int:id>',views.saveunit,name='saveunit'),
    path('godwn',views.godwn,name='godwn'),
    path('godwn_alter/<int:id>',views.godwn_alter,name='godwn_alter'),
    path('savegod/<int:id>',views.savegod,name='savegod'),
]