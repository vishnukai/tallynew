import imp
from django.shortcuts import render
import datetime

from tallynewapp.models import StockCategory
from tallynewapp.models import Godowns,StockCategory,Stockgroup,Taxability,Unit,Gst

# Create your views here.

def stock_grp(request):
    today_date=datetime.datetime.now()
    stockgrp=Stockgroup.objects.all()
    return render(request, 'stock_grp.html',{'todaydate':today_date,'stockgrp':stockgrp})
def groupalter(request,id):
    stockgrpi=Stockgroup.objects.get(id=id)
    stockgrp=Stockgroup.objects.all()
    return render(request,'stockgroupalter.html',{'stockgrp':stockgrp,'stockgrpi':stockgrpi})

def editunit(request):
    return render(request,'editunit.html')

def editgodown(request):
    return render(request,'godown.html')

def stockcat(request):
    return render(request,'editstockcat.html')

def newgroupemploye(request):
    return render(request,'newgroupemployegroup.html')
def home(request):
    return render(request,'base.html')

def stockgroup(request):
    return render(request,'createstockgroup.html')