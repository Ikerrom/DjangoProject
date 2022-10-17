from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def sukaldariak(request):
    mysukaldari = Sukaldari.objects.all()
    template = loader.get_template('sukaldariak.html')
    context = {
    'mysukaldari': mysukaldari,
    }
    return HttpResponse(template.render(context, request))

def platerak(request,price):
    total = Total.objects.get(id=1)
    dprice = float(price) + total.totalprice;
    newprice = Total(id = 1, totalprice = dprice)
    newprice.save()
    myplatera = Platera.objects.all()
    template = loader.get_template('platerak.html')
    context = {
    'newprice': newprice,
    'myplatera': myplatera,
    }
    return HttpResponse(template.render(context, request))

def delsukaldari(request,id):
    Sukaldari.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('sukaldariak'))

def delplatera(request,id):
    Platera.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('platerak',kwargs={'price': 0}))

def addsukaldari(request):
    template = loader.get_template('addsukaldari.html')
    return HttpResponse(template.render())

def addplatera(request):
    mysukaldari = Sukaldari.objects.all()
    template = loader.get_template('addplatera.html')
    context = {
    'mysukaldari': mysukaldari,
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def addsukaldaritodb(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    photo = request.POST['photo']
    sukaldari = Sukaldari(firstname = firstname, lastname = lastname, photo = photo)
    sukaldari.save()
    return HttpResponseRedirect(reverse('sukaldariak'))

@csrf_exempt
def addplateratodb(request):
    name = request.POST['name']
    desc = request.POST['desc']
    price = request.POST['price']
    photo = request.POST['photo']
    sukaldariid = request.POST['sukaldari']
    sukaldariobj = Sukaldari.objects.get(id=sukaldariid)
    platera = Platera(name = name, desc = desc, price= price, photo = photo, sukaldari = sukaldariobj)
    platera.save()
    return HttpResponseRedirect(reverse('platerak',kwargs={'price': 0}))   

def updatesukaldari(request,id):
    sukaldaria = Sukaldari.objects.get(id=id)
    template = loader.get_template('updatesukaldari.html')
    context = {
    'sukaldaria': sukaldaria,
    }
    return HttpResponse(template.render(context, request))

def updateplatera(request,id):
    platera = Platera.objects.get(id=id)
    mysukaldari = Sukaldari.objects.all()
    template = loader.get_template('updateplatera.html')
    context = {
    'platera': platera,
    'mysukaldari': mysukaldari,
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def updatesukaldariondb(request,id):
    sukaldariid = Sukaldari.objects.get(id=id)
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    photo = request.POST['photo']
    sukaldari = Sukaldari(id = sukaldariid.id ,firstname = firstname, lastname = lastname, photo = photo)
    sukaldari.save()
    return HttpResponseRedirect(reverse('sukaldariak'))

@csrf_exempt
def updateplateraondb(request,id):
    platera = Platera.objects.get(id=id)
    name = request.POST['name']
    desc = request.POST['desc']
    price = request.POST['price']
    photo = request.POST['photo']
    sukaldariid = request.POST['sukaldari']
    sukaldariobj = Sukaldari.objects.get(id=sukaldariid)
    platera = Platera(id=platera.id ,name = name, desc = desc, price= price, photo = photo, sukaldari = sukaldariobj)
    platera.save()
    return HttpResponseRedirect(reverse('platerak',kwargs={'price': 0}))

@csrf_exempt
def reset(request):
    total = Total.objects.get(id=1)
    newprice = Total(id = 1, totalprice =0)
    newprice.save()
    return HttpResponseRedirect(reverse('platerak',kwargs={'price': 0}))