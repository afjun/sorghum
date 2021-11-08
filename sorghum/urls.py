"""sorghum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
import sorghum.views.common as commonViews
import sorghum.views.pic as picViews
from django.conf.urls import url
from django.views.static import serve
from django.conf.global_settings import MEDIA_ROOT

urlpatterns = [
    url(r'^$', commonViews.index, name='index'),

    path('admin/', admin.site.urls),
    path(r"echarts/", commonViews.echarts, name='echarts'),
    path(r"detectPic/", picViews.detectPic, name='detectPic'),
    path(r"undetectPic/", picViews.undetectPic, name='undetectPic'),

    path(r"undetectPic/detectOnePic/", picViews.detectOnePic, name='detectOnePic'),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),



    #TEST
    path(r"sidebar/", commonViews.sidebar, name='sidebar'),
    path(r"sb/", commonViews.sb, name='sb'),

]
