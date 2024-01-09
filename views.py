#!/usr/bin/env python
#coding=utf-8
from django.shortcuts import render
from .recommend import re_model
from .recommend import utils
import time

print('----初始化加载模型----')
global_model = re_model.Model()
global_loaded_graph, global_sess = global_model.loead_sess()

# Create your views here.
def index(request):

    return render(request,'index.html')

def login(request):
    login_re = {"left_img": "/static/img/login.png"}
    return render(request,'login.html',login_re)

def register(request):
    register_re = {"left_img": "/static/img/register.png"}
    return render(request,'register.html',register_re)

def login_admin(request):
    login_adre={"left_img": "/static/img/login.png"}
    return render(request,"login_admin.html",login_adre)

def forget(request):
    forget_re = {"left_img": "/static/img/login.png"}
    return render(request,"forget.html",forget_re)

def movie_detail(request):
    user={"Uname":"用户A","head":"/static/img/头像.png"}
    postcomment={}
    movie={"Mid":"00000001","Mname":"孤注一掷","Type":"剧情/犯罪","Nation":"中国大陆","Date":"2023-08-08",
              "Actor":"张艺兴/金晨/咏梅/王传君/王大陆","score":"69","Sketch":"电影取材自上万起真实诈骗案例，"
            "境外网络诈骗全产业链骇人内幕将在大银幕上首度被揭秘。程序员潘生（张艺兴 饰）、模特安娜（金晨 饰）被海外高薪招聘吸引，出国淘金，"
        "却意外落入境外诈骗工厂的陷阱。为了离开，两人准备向赌徒阿天（王大陆 饰）和其女友小雨（周也 饰）下手，从他们身上套现、"
        "完成业绩……潘生与安娜能否逃过诈骗集团头目陆经理（王传君 饰）和阿才（孙阳 饰）的残暴折磨？面对警察（咏梅 饰）的跨国调查和追捕，他们又会何去何从？",
              "Image":"/static/img/movie_cover.png"}
    star = {"yes": "/static/img/star2.png", "no": "/static/img/star1.png"}
    context={"user":user,"postcomment":postcomment,"movie":movie,"star":star}
    return render(request,"movie_detail.html",context)
def recommend(request):
    movie_id = request.GET.get('movie_id')
    try:
        if((int(movie_id)<0) | (int(movie_id)>3953)):
            return render(request,'index.html')
    except ValueError:
        return render(request, 'index.html')

    global global_model
    model=global_model
    print('-------正在推荐--------',movie_id)


    global_loaded_graph, global_sess


    choice_movie_name,list_same_movies_names,list_pepole_like_movies_names,list_same_movies_ids,list_pepole_like_movies_ids =model.recommend_by_movie(int(movie_id))


    print('选择电影：',choice_movie_name)
    print('相似的电影：',list_same_movies_names)
    print('喜欢这个电影的人还喜欢：',list_pepole_like_movies_names)

    list_dict_choice=[]
    for i in choice_movie_name:
        # time.sleep(0.2)  # 爬虫速度
        list_dict_choice.append(utils.movie_dic(i))
    list_dict_choice[0]['movie_id']=movie_id
    # list_dict_choice[0]['title']=choice_movie_name



    list_dict_same = []
    for i in list_same_movies_names[:4]:
        # time.sleep(0.2)
        list_dict_same.append(utils.movie_dic(i))
    for i in range(len(list_dict_same)):
        list_dict_same[i]['movie_id']=list_same_movies_ids[i]


    list_dict_otherlike = []
    for i in list_pepole_like_movies_names[:4]:
        # time.sleep(0.2)
        list_dict_otherlike.append(utils.movie_dic(i))
    for i in range(len(list_dict_otherlike)):
        list_dict_otherlike[i]['movie_id'] = list_pepole_like_movies_ids[i]
        #list_dict_otherlike[i]['title'] = list_dict_otherlike[i]



    print('返回结果')
    print(list_dict_choice)
    print(len(list_dict_same))
    # print(len(list_dict_otherlike))
    context = {}
    context['list_dict_choice'] = list_dict_choice[:4]
    context['list_dict_same'] = list_dict_same
    context['list_dict_otherlike'] = list_dict_otherlike

    return render(request,'index.html',context)

