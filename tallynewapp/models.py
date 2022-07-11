
from django.db import models

class Stockgroup(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    quanty=models.BooleanField(default=False)
    gstvalue=models.BooleanField(default=False)

class Taxability(models.Model):
    name=models.CharField(max_length=225)

class Gst(models.Model):
    taxabiliy=models.ForeignKey(Taxability,on_delete=models.CASCADE)
    groupid=models.ForeignKey(Stockgroup,on_delete=models.CASCADE)
    integratedtax=models.IntegerField()
    Cess=models.IntegerField()


class Unit(models.Model):
    type=models.CharField(max_length=225)
    symbol=models.CharField(max_length=225)
    foramlname=models.CharField(max_length=225)
    unitcode=models.CharField(max_length=225)
    decimal=models.IntegerField()

class Godowns(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    godown=models.CharField(max_length=225)

class StockCategory(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)

