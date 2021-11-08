import os

from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render
from sorghum import models
from pathlib import Path
import json
import sorghum.tools.sorghumDetect as sorghumDetect

BASE_DIR = Path(__file__).resolve().parent.parent.parent


# 显示已经检测的结果
def detectPic(request):
    print("BASE_DIR" + str(BASE_DIR))
    allDetectedSorghumPic = models.SorghumPic.objects.filter(detect=2)  # 查询已经检测过的图
    urlList = []
    for one in allDetectedSorghumPic:
        print("遍历detected图：" + str(one.filename) + "  relativePath： " + str(one.relativepath))
        # oneRealPath = os.path.join(BASE_DIR, one.relativepath)
        # print("realPath:" + str(oneRealPath))
        urlList.append(
            {"path": one.relativepath, "num": one.num, "id": one.id, "filename": one.filename, "time": one.time})

    renderDict = {'urlList': urlList}

    return render(request, 'detectPic.html', renderDict)
    # return render(request, 'pic.html')


# 显示未检测的图片结果
def undetectPic(request):
    print("BASE_DIR" + str(BASE_DIR))
    allDetectedSorghumPic = models.SorghumPic.objects.filter(detect=0)  # 查询未检测过的图
    urlList = []
    for one in allDetectedSorghumPic:
        print("遍历detected图：" + str(one.filename) + "  relativePath： " + str(one.relativepath))
        # oneRealPath = os.path.join(BASE_DIR, one.relativepath)
        # print("realPath:" + str(oneRealPath))
        urlList.append(
            {"path": one.relativepath, "num": one.num, "id": one.id, "filename": one.filename, "time": one.time})

    renderDict = {'urlList': urlList}

    return render(request, 'undetectPic.html', renderDict)


def detectOnePic(request):
    id = request.GET.get('id')  # 获取图片的id
    responseDict = {"id": id}
    sorghumPic = models.SorghumPic.objects.filter(id=id)  # 从数据库拿出数据
    print("回传的相对路径：" + str(sorghumPic[0].relativepath))

    return_dict = {}
    # 看看有没有已经检测的结果 :filename detect == 2
    oldSorghumPic = models.SorghumPic.objects.filter(filename=sorghumPic[0].filename, detect=2)
    print("oldSorghumPic:" + str(oldSorghumPic))
    if len(oldSorghumPic) == 0:  # 还没有检测过
        # 模型检测
        return_dict = sorghumDetect.detect_one_pic(
            str(sorghumPic[0].relativepath))  # 输入图片的相对路径，返回filename： ... num:... 还是字典
        # 新建一条数据插入到数据库表中
        models.SorghumPic.objects.create(
            num=return_dict["num"],
            filename=return_dict["filename"],
            relativepath=return_dict["relativePath"],
            detect=2
        )

    else:  # 已经检测过的，重写return_dict
        print(str(sorghumPic[0].filename) + "已经检测过了！")
        return_dict["num"] = oldSorghumPic[0].num
        return_dict["filename"] = oldSorghumPic[0].filename

    # update detect where id=id
    # detect:0-原图未测 1-原图已测 2-结果图
    models.SorghumPic.objects.filter(id=id).update(detect=1)
    print(return_dict)
    print("图片的id:" + id)

    responseDict["num"] = return_dict["num"]
    responseDict["filename"] = return_dict["filename"]

    str_json = json.dumps(responseDict)  # 字典转换为json
    response = HttpResponse(str_json, content_type='application/json; charset=utf-8')  # 将数据返回到前端
    return response
    # return HttpResponse("检测成功！")
