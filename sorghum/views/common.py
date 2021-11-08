import json
import os

from django.core import serializers
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from sorghum import models
from django.db import connection


# render请求
from sorghum.settings import BASE_DIR


def index(request):
    print("当前BASE_DIR:" + str(BASE_DIR))
    allDetectedSorghumPic = models.SorghumPic.objects.all()
    urlList = []
    for one in allDetectedSorghumPic:
        print("遍历detected图：" + str(one.filename) +"  relativePath： " + str(one.relativepath))
        # oneRealPath = os.path.join(BASE_DIR,one.relativepath)
        # print("realPath:" + str(oneRealPath))
        urlList.append(one.relativepath)

    renderDict = {'urlList':urlList,'BASE_DIR':BASE_DIR}
    return render(request, 'index.html', renderDict)
    # return render(request, 'index.html')


def echarts(request):
    datalist = [5, 20, 36, 10, 10, 20]
    users = models.User.objects.all()
    print(users)
    for one in users:
        print("遍历ing：" + str(one.id) + " " + str(one.name))

    return render(request, 'echarts.html')


def sidebar(request):
    return render(request, 'block/sidebar.html')


def sb(request):
    return render(request, 'sb_admin/index.html')
