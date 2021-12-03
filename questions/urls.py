from django.urls import include, path
from .views import QuestionsView, ResponseView, ScoreView, CodeOutputResponseView, CodeOutputCheckView

urlpatterns = [
    path('ques/<ques_id>', QuestionsView.as_view(), name='ques'),
    path('response/<ques_id>', ResponseView.as_view(), name='res'),
    path('score/', ScoreView.as_view(), name='score'),
    path('code_res/<ques_id>', CodeOutputResponseView.as_view(), name='code_res'),
    path('code_res_check/<ques_id>', CodeOutputCheckView.as_view(), name='code_output_check'),
]

