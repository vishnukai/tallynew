
from django.shortcuts import redirect, render
import datetime
from django.db.models import Q
from tallynewapp.models import StockCategory
from tallynewapp.models import Godowns,StockCategory,Stockgroup,Taxability,Unit,Gst,Type,Unitcode

# Create your views here.

def stock_grp(request):
    today_date=datetime.datetime.now()
    stockgrp=Stockgroup.objects.all()
    return render(request, 'stock_grp.html',{'todaydate':today_date,'stockgrp':stockgrp})
def groupalter(request,id):
    stockgrpi=Stockgroup.objects.get(id=id)
    stockgrp=Stockgroup.objects.filter(~Q(id=id))
    return render(request,'stockgroupalter.html',{'stockgrp':stockgrp,'stockgrpi':stockgrpi})

def editunit(request):
    return render(request,'editunit.html')

def stock_items(request):
    return render(request, 'stock_items.html') 

def units(request):
    today_date=datetime.datetime.now()
    unit=Unit.objects.all()
    return render(request, 'units.html',{'todaydate':today_date,'unit':unit}) 
def stock_cat(request):
    today_date=datetime.datetime.now()
    sc=StockCategory.objects.all()
    return render(request, 'stock_cat.html',{'today_date':today_date,'sc':sc})


def editgodown(request):
    return render(request,'godown.html')

def editcat(request,id):
    sc=StockCategory.objects.get(id=id)
    scat=StockCategory.objects.filter(~Q(id=id))
    return render(request,'editstockcat.html',{'sc':sc,'scat':scat})

def newgroupemploye(request):
    return render(request,'newgroupemployegroup.html')
def home(request):
    return render(request,'base.html')

def stockgroup(request):
    return render(request,'createstockgroup.html')

def savegrp(request,id):
    if request.method=="POST":
        stock=Stockgroup.objects.get(id=id)
        stock.name=request.POST.get('name')
        stock.alias=request.POST.get('alias')
        stock.under=request.POST.get('under')
        stock.gstvalue=request.POST.get('gst')
        stock.quanty=request.POST.get('qty')
        stock.save()

    return redirect(stock_grp)

def creategrp(request,id):
    return render(request,'createstockgroup.html')

def savecat(request,id):  
    if request.method=="POST":
        cat=StockCategory.objects.get(id=id)
        cat.name=request.POST.get('name')
        cat.alias=request.POST.get('alias')
        cat.under=request.POST.get('under')
        cat.save()
    return redirect('stock_cat')

def editunit(request,id):
    unit=Unit.objects.get(id=id)
    type=Type.objects.all()
    unitcode=Unitcode.objects.all()
    return render(request,'editunit.html',{'unit':unit,'type':type,'unitcode':unitcode})


def saveunit(request,id):
    if request.method=="POST":
        unit=Unit.objects.get(id=id)
        type=request.POST.get('type')
        t=Type.objects.get(type=type)
        unitcode=request.POST.get('unitcode')
        uc=Unitcode.objects.get(unitcode=unitcode)
        unit.type=t
        unit.unitcode=uc
        unit.symbol=request.POST.get('symbol')
        unit.decimal=request.POST.get('decimal')
        unit.formalname=request.POST.get('name')
        unit.save()

    return redirect('units')


def godwn(request):
    god=Godowns.objects.all()
    today_date=datetime.datetime.now()
    return render(request, 'godwn.html',{'god':god,'todaydate':today_date})
        

def godwn_alter(request,id):
    god=Godowns.objects.get(id=id)
    godi=Godowns.objects.filter(~Q(id=id))
    return render(request, 'godwn_alter.html',{'god':god,'godi':godi})


def savegod(request,id):
    if request.method=="POST":
        god=Godowns.objects.get(id=id)
        god.name=request.POST.get('name')
        god.godown=request.POST.get('godown')
        god.alias=request.POST.get('alias')
        god.save()
        return redirect('godwn')


