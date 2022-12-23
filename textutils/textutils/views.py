from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("About me")

def Login(request):
    return HttpResponse ("<a href='https://Amazon.com/' >1- Go TO Amazon </a>")

def analyse(request):
    djtext=request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc',"off")
    print(removepunc)
    print(djtext)
    analysed=""
    punctuation='''!@#$%^&*(){}""[]:;.*?<>'''
    if removepunc=="on":
        for char in djtext:
            if char not in punctuation:
                analysed=analysed + char
        params={'purpose':'Remove Punctuations','analysed_text':analysed}
        return render(request, 'analyse.html', params)
    else:
        return HttpResponse("Error")
