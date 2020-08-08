import json

from django.contrib import messages
from django.shortcuts import render

def indexpage(request):
    calling = jsondata()
    return render(request, 'index.html', {'data': calling})


def jsondata():
    read_data = open('AppIMDb/raw/rest.json', 'r')
    aft_read = read_data.read()
    dic_data = json.loads(aft_read)
    titles = [x['title'][0:len(x['title']) - 1] for x in dic_data if
              x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                  'plot'] != '']
    posters = [x['poster'] for x in dic_data if
               x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                   'plot'] != '']
    trailer = [x['trailer']['link'] for x in dic_data if
               x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                   'plot'] != '']
    rating = [x['rating'] for x in dic_data if
              x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                  'plot'] != '']
    plot = [x['plot'] for x in dic_data if
            x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                'plot'] != '']
    print(titles)

    loop = [{"title": a, "poster": b, "trailers": c,"ratings":d,"plots": e} for a, b, c, d, e in
            zip(titles, posters, trailer, rating, plot)]

    return loop




def searchMovie(request):
    m_search = request.POST.get("searchMovie")
    c_jd = jsondata()

    for x in c_jd:
        if x['title'] == m_search:
            print(x)
            return render(request,'searchMovie.html',{"sear_mov":x})
        else:
            messages.error(request,"Movie name You searched not available")
            return render(request, 'searchMovie.html')


