from django.shortcuts import render, redirect


# Create your views here.

def mainpage(request) :
    print('debug >>> mainpage')
    return render(request, 'main/index.html')

def chart_inline(request) :
    print('debug >>> chart_inline')
    return render(request, 'main/chart-inline.html')

def profile(request) :
    print('debug >>> profile')
    return render(request, 'main/profile.html')

def widgets(request) :
    print('debug >>> widgets')
    return render(request, 'main/widgets.html')

def blank(request) :
    print('debug >>> balnk')
    return render(request, 'main/page-blank-ex.html')

def contacts_grid(request) :
    print('debug >>> widgets')
    return render(request, 'main/contacts_grid.html')

def index_h(request):
    print('debug >>> index_h')
    return render(request, 'main/index-horizontal.html')