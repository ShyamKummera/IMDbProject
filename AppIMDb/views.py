import json

from django.shortcuts import render

def indexpage(request):
    j_d = open('AppIMDb/rest.json','r')
    j_s = j_d.read()
    dic_j = json.loads(j_s)
    l = []
    for x,y in dic_j.items():
        if x == "d":
            for a in y:
                for b,c in a.items():
                    if b == 'i':
                        imag = c['imageUrl']
                        l.append(imag)
    print(l)
    return render(request,'index.html',{"data":l})