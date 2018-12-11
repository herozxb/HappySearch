from django.shortcuts import render

from django.http import HttpResponse

######################################################
# Too slow loading the object

#import pickle
#import sklearn
#clf = pickle.load(open('/home/deep/deepLearning/DeepVision/clf100k', 'rb'))

import os
from forIOS import settings 

def index(request):

    #string = getattr(settings, "kmeans_normal", None)
    kmeans_normal = settings.kmeans_normal
    clf = settings.clf
    if settings.DEBUG:
        print(kmeans_normal)
        print(clf)

    return HttpResponse("Hello, world. You're at the forKmeans index.")

# Create your views here.
