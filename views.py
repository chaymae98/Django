"""from django.shortcuts import render
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Avg
from .forms import Filter
from statistics import mean
# Create your views here.
'''def list_dvf(request):
    data = requests.get("http://api.cquest.org/dvf?section=94068000CQ").json()
    paginator = Paginator(data['resultats'], 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})
'''
def list_houses(request):
    api = "http://api.cquest.org/dvf?"
    val = request.POST
    for k, v in val.items():
        if v and not k == "csrfmiddlewaretoken":
            print(k)
            api=f"{api}{k}={v}&"
    print(api)
    apiUrl = f"http://api.cquest.org/dvf?code_commune=89304"
    data = requests.get(api).json()
    if not data.get("erreur"):
        paginator = Paginator(data['resultats'], 50000000000)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        #return render(request, "index2.html", {'page_obj': page_obj,'form':val.dict()})
   # return render(request, "index2.html")
        # valeur_fonciere * surface_terrain
        moy = []
        for el in data['resultats']:
            if el['valeur_fonciere'] and el['surface_terrain']:
                moy.append(el['valeur_fonciere'] * el['surface_relle_bati'])
        # moy = round(mean(moy),4)
        test = [5, 5, 5, 6, 9]
        moy = mean(moy)
        return render(request, "index2.html", {'page_obj': page_obj, 'moy': moy, 'form': val.dict()})
    return render(request, "index2.html", {'moy': 0})
"""
from django.shortcuts import render
# Create your views here.
import requests
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import Filter
from statistics import mean


def list_houses(request):
    api = "http://api.cquest.org/dvf?"

    val = request.POST
    for k, v in val.items():
        if v and not k == "csrfmiddlewaretoken":
            print(k)
            api = f"{api}{k}={v}&"
    print(api)
    apiUrl = f"http://api.cquest.org/dvf?code_commune=89304"
    data = requests.get(api).json()
    if not data.get("erreur"):
        paginator = Paginator(data['resultats'], 50000000000)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # valeur_fonciere * surface_terrain
        moy = []
        for el in data['resultats']:
            if el['valeur_fonciere'] and el['surface_relle_bati']:
                moy.append(el['valeur_fonciere'] / el['surface_relle_bati'])
        moy = round(mean(moy),4)
        #test = [5, 5, 5, 6, 9]
        #moy = mean(moy)
        return render(request, "index2.html", {'page_obj': page_obj, 'moy': moy, 'form': val.dict()})
    return render(request, "index2.html", {'moy': 0})