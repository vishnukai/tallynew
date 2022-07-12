
from django.db import models

class Stockgroup(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    quanty=models.CharField(max_length=225)
    gstvalue=models.CharField(max_length=225)

class Taxability(models.Model):
    name=models.CharField(max_length=225)

class Gst(models.Model):
    taxabiliy=models.ForeignKey(Taxability,on_delete=models.CASCADE)
    groupid=models.ForeignKey(Stockgroup,on_delete=models.CASCADE)
    integratedtax=models.IntegerField()
    Cess=models.IntegerField()

class Unitcode(models.Model):
    unitcode=models.CharField(max_length=225)

class Type(models.Model):
    type=models.CharField(max_length=225)


class Unit(models.Model):
    type=models.ForeignKey(Type,on_delete=models.CASCADE)
    symbol=models.CharField(max_length=225)
    formalname=models.CharField(max_length=225)
    unitcode=models.ForeignKey(Unitcode,on_delete=models.CASCADE)
    decimal=models.IntegerField()

class Godowns(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    godown=models.CharField(max_length=225)

class StockCategory(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)

