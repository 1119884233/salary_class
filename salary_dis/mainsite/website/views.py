from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(requst):
    return HttpResponse("这是让人非常不错的晚上,继续加油")