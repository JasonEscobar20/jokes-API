import requests
from requests.adapters import HTTPAdapter
from requests.sessions import Session
import urllib3

from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ApiListJokes(APIView):
    def get(self, request, *args, **kwargs):

        jokes_list = []
        
        with requests.Session() as session:
            for joke in range(1, 26):
                # joke_api = requests.get('https://api.chucknorris.io/jokes/random')
                with session.get('https://api.chucknorris.io/jokes/random') as response:
                    joke_api_data = response.json()

                    for item in jokes_list:
                        if joke_api_data['id'] == item['id']:
                            joke_api = session.get('https://api.chucknorris.io/jokes/random')
                            joke_api_data = joke_api.json()


                    new_joke = {

                        'id': joke_api_data['id'],
                        'url': joke_api_data['url'],
                        'value': joke_api_data['value'],
                    }


                    jokes_list.append(new_joke)


        return Response(jokes_list, status=status.HTTP_200_OK)
