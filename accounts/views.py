from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, HttpResponseRedirect
import random
import requests
import json
from firebase_admin import db
# Create your views here.
from crossword_quiz.settings import FIREBASE_API_KEY


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        if firebase_admin._DEFAULT_APP_NAME not in firebase_admin._apps:
            cred = credentials.Certificate(
                'tech-event-nov-21-firebase-adminsdk-52bqf-9b37df2e76.json')
            check = firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://tech-event-nov-21-default-rtdb.firebaseio.com/'
            })

        email = request.data.get('email')
        password = request.data.get('password')
        if firebase_admin._DEFAULT_APP_NAME not in firebase_admin._apps:
            try:
                cred = credentials.Certificate(
                    'tech-event-nov-21-firebase-adminsdk-52bqf-9b37df2e76.json')
                check = firebase_admin.initialize_app(cred)
            except firebase_admin.exceptions.FirebaseError as ex:
                print(f'{ex}')
                pass
        data = {"email": '{}'.format(email),
                "password":  '{}'.format(password),
                "returnSecureToken": "true"
                }
        response = requests.post(
            'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={}'.format(FIREBASE_API_KEY), json=data)
        response_data = dict()
        if (response.status_code == 200):
            response_data = response.json()
            uid = response_data['localId']
            user = auth.get_user(uid)
            data = user._data
            sap = data.get('displayName')

            main_ref = firebase_admin.db.reference('/')
            ref = main_ref.child('responses/')
            ref1 = main_ref.child('score/')

            add_user = {
                '{}'.format(sap): {
                    "entered_quiz": "True"
                }
            }
            ref.update(add_user)
            ref1.update(add_user)

        else:
            response_data = response.json()
            message = response_data['error']['message']
            response_data = {
                "Error": message
            }

        return Response(response_data, status=response.status_code)






