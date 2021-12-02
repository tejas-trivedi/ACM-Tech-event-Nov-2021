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


class QuestionsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, ques_id, format=None):

        data = request.get('https://tech-event-nov-21-default-rtdb.firebaseio.com/')
        data = data.json()
        question = data['question']
        options = dict()

        for i in range(1, len(data['choices'])):
            options[i] = data['choices'][i]

        response_data = {
            "Question": question,
            "Choices": options,
        }
        return Response(response_data)


class ResponseView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, ques_id, format=None):
        if firebase_admin._DEFAULT_APP_NAME not in firebase_admin._apps:
            cred = credentials.Certificate(
                'tech-event-nov-21-firebase-adminsdk-52bqf-9b37df2e76.json')
            check = firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://tech-event-nov-21-default-rtdb.firebaseio.com/'
            })
        main_ref = firebase_admin.db.reference('/')

        uid = request.data.get("uid")
        selected_option = request.data.get("selected_option")
        user = auth.get_user(uid)
        data = user._data
        sap = data.get('displayName')

        ref = main_ref.child('responses/{}'.format(sap))
        ref1 = main_ref.child('responses/{}/{}'.format(sap, ques_id)).get()

        if(ref1==None):
            options_data = {
                '{}'.format(ques_id):{
                    "response": selected_option
                }
            }
            response_data = "Answer submitted successfully"
            ref.update(options_data)

        else:
            response_data = "This question is already submitted."

        return Response(response_data)


class CodeOutputResponseView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, ques_id, format=None):
        if firebase_admin._DEFAULT_APP_NAME not in firebase_admin._apps:
            cred = credentials.Certificate(
                'tech-event-nov-21-firebase-adminsdk-52bqf-9b37df2e76.json')
            check = firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://tech-event-nov-21-default-rtdb.firebaseio.com/'
            })
        main_ref = firebase_admin.db.reference('/')

        uid = request.data.get("uid")
        code_output = request.data.get("code_output")
        user = auth.get_user(uid)
        data = user._data
        sap = data.get('displayName')

        ref = main_ref.child('code_response/{}'.format(sap))

        code_data = {
            '{}'.format(ques_id):{
                "code_output_res": code_output
            }
        }
        ref.update(code_data)

        return Response("Code output submitted")
