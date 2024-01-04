from django.shortcuts import render
from re_sys.recommend import re_model
from re_sys.recommend import utils
import time

print('----初始化加载模型----')
model = re_model.Model()
global_loaded_graph, global_sess = model.loead_sess()

def recommend(movie_id):
    choice_movie_name,list_same_movies_names,list_pepole_like_movies_names,list_same_movies_ids,list_pepole_like_movies_ids =model.recommend_by_movie(int(movie_id))
    print('选择电影：',choice_movie_name)
    print('相似的电影：',list_same_movies_names)
    print('喜欢这个电影的人还喜欢：',list_pepole_like_movies_names)

recommend(200)