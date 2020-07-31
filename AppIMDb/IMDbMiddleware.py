import json

import requests


class IMDbMiddleware:
    def __init__(self,response):
        self.get_response = response
        print("im constructor")

        url = "https://imdb8.p.rapidapi.com/title/auto-complete"

        querystring = {"q": "game of thr"}

        headers = {
            'x-rapidapi-host': "imdb8.p.rapidapi.com",
            'x-rapidapi-key': "03bd3e49e7msh65497cbb3e82939p1a131djsne7c88de63efb"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)



        file = open('AppIMDb/rest.json','w')
        j_data = json.loads(response.text)
        dict = json.dump(j_data,file)
        print("data is written")


    def __call__(self,request, *args, **kwargs):
        response = self.get_response(request)
        print("im call")
        return response

