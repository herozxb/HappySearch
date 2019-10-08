# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
import time
import sklearn
from forIOS2 import settings 
import os
import re



#@ensure_csrf_cookie
@csrf_exempt
def index(request):

	if request.method == 'POST':
		json_data = json.loads(request.body.decode('utf-8'))
		print(json_data)
	image_feature = json.loads(json_data["List"])
	print(image_feature)
	kmeans = settings.kmeans
	y_pred = kmeans.predict([image_feature])
	print(y_pred)
	images_dir = '/media/king/DeepVision/kmeans_group_result/' + str(y_pred[0])
	phone_images = [f for f in os.listdir(images_dir) if re.search('jpg|JPG|jpeg|JPEG', f)]
	print(phone_images)
	#dic = dict(zip(range(len(phone_images)),phone_images))
	#dic = dict(zip("name",phone_images))
	row_json = json.dumps(phone_images)
	dict_json = json.dumps(phone_images)
	#row_json = json.dumps(dic)
	print(row_json)
	'''	
	print("=====================================================================")

	clf2 = joblib.load("testSVC.pkl")

	y_pred = clf2.predict([X_image])
	print(y_pred)
'''
	cnx = settings.cnx

	cursor = cnx.cursor()
	query = ("SELECT name FROM IOSresult3 where id = %s" %(y_pred[0]+1))
	print("here 1.0")
	cursor.execute(query)
	print("here 1.1")

	for (ID) in cursor:
    		print(ID)
	print("here 1.2")
	#return JsonResponse(row_json,safe=False)
	return JsonResponse(ID,safe=False)	
	#return HttpResponse("Hello, world. You're at the forKmeans index.")
# Create your views here.
