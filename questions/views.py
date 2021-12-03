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
        if firebase_admin._DEFAULT_APP_NAME not in firebase_admin._apps:
            cred = credentials.Certificate(
                'tech-event-nov-21-firebase-adminsdk-52bqf-9b37df2e76.json')
            check = firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://tech-event-nov-21-default-rtdb.firebaseio.com/'
            })
        data = requests.get('https://tech-event-nov-21-default-rtdb.firebaseio.com/Questions/%s.json' %ques_id)
        data = data.json()

        question = data['question']
        response_data = {
            "Question": question,
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



class CodeOutputCheckView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, ques_id, format=None):
        if firebase_admin._DEFAULT_APP_NAME not in firebase_admin._apps:
            cred = credentials.Certificate(
                'tech-event-nov-21-firebase-adminsdk-52bqf-9b37df2e76.json')
            check = firebase_admin.initialize_app(cred, {
                'https://tech-event-nov-21-default-rtdb.firebaseio.com/'
            })

        uid = request.data.get("uid")
        user = auth.get_user(uid)
        data = user._data
        sap = data.get('displayName')
        main_ref = firebase_admin.db.reference('/')

        my_code_res = main_ref.child('code_response/{}/{}/code_output_res'.format(sap, ques_id)).get()
        code_ans = main_ref.child('Questions/{}/code_ans'.format(ques_id)).get()

        if my_code_res==code_ans:
            response_data = {
                "Right Answer"
            }
        else:
            response_data = {
                "Wrong Answer Try Again"
            }

        if my_code_res==None or code_ans==None:
            response_data = "Invalid"

        return Response(response_data)


class ScoreView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        if firebase_admin._DEFAULT_APP_NAME not in firebase_admin._apps:
            cred = credentials.Certificate(
                'tech-event-nov-21-firebase-adminsdk-52bqf-9b37df2e76.json')
            check = firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://tech-event-nov-21-default-rtdb.firebaseio.com/'
            })

        uid = request.data.get("uid")
        user = auth.get_user(uid)
        data = user._data
        sap = data.get('displayName')

        main_ref = firebase_admin.db.reference('/')

        score=0
        for i in range(0, 7):
            print(i)
            correct_ans = main_ref.child('Questions/{}/correct_ans'.format(i)).get()
            selected_ans = main_ref.child('responses/{}/{}/response'.format(sap, i)).get()

            print(correct_ans, selected_ans)

            if correct_ans==selected_ans:
                score = score + 1
                print(score)
            else:
                score = score

        score_data = {
            "Score": score
        }

        ref = main_ref.child('score/{}'.format(sap))
        ref.update(score_data)

        return Response(score_data)

