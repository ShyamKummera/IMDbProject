import json

import requests


class IMDbMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        t_list=getIMDbMovie_id()

        list_of_data=[]
        for moviename in t_list:

            url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/"+moviename

            headers = {
                'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
                'x-rapidapi-key': "0ac662495cmsha3ddbe01a85b038p1b0e32jsn0541b2f89aff"
            }

            response = requests.request("GET", url, headers=headers)

            dict_data = json.loads(response.text)
            list_of_data.append(dict_data)
        print("***************************************")
        file = open('AppIMDb/raw/rest.json', 'w')
        print(list_of_data)

        json.dump(list_of_data, file, indent=2)
        print("im constructor")

    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        print("iam call")
        return response


# -------------------------------------------------------------------------------


def getIMDbMovie_id():
    url = "https://imdb8.p.rapidapi.com/title/get-popular-movies-by-genre"

    querystring = {"genre": "%2Fchart%2Fpopular%2Fgenre%2Fadventure"}

    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': "0ac662495cmsha3ddbe01a85b038p1b0e32jsn0541b2f89aff"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)
    resstr=response.text.split('/')
    # print(resstr)
    l=[]
    for x in resstr:
        if x.split('/'):
            if x.startswith('tt'):
                l.append(x)
    # print(l)
    return l
