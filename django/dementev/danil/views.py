from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fio(request, **kwargs):
    return HttpResponse(kwargs['fio'])

def about(request):
    return HttpResponse('kzn <br> 4,5 <br> i dont like')

def contacts(request):
    return HttpResponse('+79178946463, tg:@Danya_Dem, github:DanyaDem')