from django.shortcuts import render


def index(request):
    var = "'Teste de passagem de variavel'"
    return render(request,'index.html',{'variavel' : var})