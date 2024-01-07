import requests
import matplotlib.pyplot as plt
import pickle
import tensorflow as tf
import re

def format_names(list_name):
    list_format_names=[]
    pattern = re.compile(r'^(.*)\((\d+)\)$')
    for name in list_name:
        list_format_names.append(pattern.match(name).group(1))

    return list_format_names


def save_params(params):
    pickle.dump(params, open('params.p', 'wb'))

def load_params():
    return pickle.load(open('params.p', mode='rb'))

def get_batches(Xs, ys, batch_size):
    for start in range(0, len(Xs), batch_size):
        end = min(start + batch_size, len(Xs))
        yield Xs[start:end],ys[start:end]

def display_loss(train_losses,test_losses):
    # train_loss
    plt.plot(train_losses['train'], label='Training loss')
    plt.legend()
    _ = plt.ylim()
    # test_loss
    plt.plot(test_losses['test'], label='Test loss')
    plt.legend()
    _ = plt.ylim()


def place_inputs():
    """
    定义占位符
    :return:
    """
    uid = tf.placeholder(tf.int32, [None, 1], name="uid")   # (-1,1)
    user_gender = tf.placeholder(tf.int32, [None, 1], name="user_gender")
    user_age = tf.placeholder(tf.int32, [None, 1], name="user_age")
    user_job = tf.placeholder(tf.int32, [None, 1], name="user_job")

    movie_id = tf.placeholder(tf.int32, [None, 1], name="movie_id")
    movie_categories = tf.placeholder(tf.int32, [None, 18], name="movie_categories")  #(-1,18)
    movie_titles = tf.placeholder(tf.int32, [None, 15], name="movie_titles")   #(-1,15)

    targets = tf.placeholder(tf.int32, [None, 1], name="targets")
    LearningRate = tf.placeholder(tf.float32, name="LearningRate")
    dropout_keep_prob = tf.placeholder(tf.float32, name="dropout_keep_prob")
    return uid, user_gender, user_age, user_job, movie_id, movie_categories, movie_titles, targets, LearningRate, dropout_keep_prob



def get_tensors(loaded_graph):
    uid = loaded_graph.get_tensor_by_name("uid:0")
    user_gender = loaded_graph.get_tensor_by_name("user_gender:0")
    user_age = loaded_graph.get_tensor_by_name("user_age:0")
    user_job = loaded_graph.get_tensor_by_name("user_job:0")
    movie_id = loaded_graph.get_tensor_by_name("movie_id:0")
    movie_categories = loaded_graph.get_tensor_by_name("movie_categories:0")
    movie_titles = loaded_graph.get_tensor_by_name("movie_titles:0")
    targets = loaded_graph.get_tensor_by_name("targets:0")
    dropout_keep_prob = loaded_graph.get_tensor_by_name("dropout_keep_prob:0")
    lr = loaded_graph.get_tensor_by_name("LearningRate:0")
    inference = loaded_graph.get_tensor_by_name(
        "inference/ExpandDims:0")
    movie_combine_layer_flat = loaded_graph.get_tensor_by_name("movie_fc/Reshape:0")
    user_combine_layer_flat = loaded_graph.get_tensor_by_name("user_fc/Reshape:0")
    return uid, user_gender, user_age, user_job, movie_id, movie_categories, movie_titles, targets, lr, dropout_keep_prob, inference, movie_combine_layer_flat, user_combine_layer_flat

"""
def movie_dic(movie_name):
    movie_dict={}
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML,  like Gecko) Chrome/18.0.1025.166  Safari/535.19'}
    proxies = {'http': '211.137.22.146'}
    url = 'https://api.douban.com/v2/movie/search?q='+movie_name+'&start=0&count=10'
    resp = requests.get(url,headers=headers,proxies=proxies)
    print('请求：'+url)
    resource_movies_dict=dict(resp.json())
    image_url=resource_movies_dict['subjects'][0]['images']['large']
    title = resource_movies_dict['subjects'][0]['title']
    average_rating=resource_movies_dict['subjects'][0]['rating']['average']
    douban_url=resource_movies_dict['subjects'][0]['alt']

    movie_dict['image_url']= image_url
    movie_dict['title']= title
    movie_dict['average_rating']= average_rating
    movie_dict['douban_url']=douban_url
    print(movie_dict)
    return movie_dict
"""
def movie_dic(movie_name):
    movie_dict={}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    proxies = {'http': '192.168.56.1'}
    # url = '
    # search?q='+movie_name+'&start=0&count=10'
    # url = 'https://movie.douban.com/'
    # url = 'https://search.douban.com/movie/subject_search?search_text='+movie_name+'&cat=1002'
    url = 'https://api.wmdb.tv/api/v1/movie/search?q=' + movie_name + '&limit=10&skip=0'
    # resp = requests.get(url,headers=headers,proxies=proxies)
    resp = requests.get(url,headers=headers, proxies=proxies, verify=False)
    # print(resp)
    print('请求：'+url)
    resource_movies_list = []
    resource_movies_list = resp.json()
    """
    print(resource_movies_list[0])
    resource_movies_dict = {}
    for data in resource_movies_list:
        resource_movies_dict.update(data)
    """
    resource_movies_dict = resource_movies_list[0]
    print(resource_movies_dict)
    image_url=resource_movies_dict['data'][0]['poster']
    title = resource_movies_dict['data'][0]['name']
    average_rating=resource_movies_dict['doubanRating']
    # douban_url=resource_movies_dict['subjects'][0]['alt']

    movie_dict['image_url']= image_url
    movie_dict['title']= title
    movie_dict['average_rating']= average_rating
    # movie_dict['douban_url']=douban_url
    print(movie_dict)
    return movie_dict


def movie_top():
    movie_list = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    proxies = {'http': '192.168.56.1'}
    url = 'https://api.wmdb.tv/api/v1/top?type=Douban&skip=0&limit=10'
    resp = requests.get(url,headers=headers, proxies=proxies, verify=False)
    print('请求：'+url)
    resource_movies_list = []
    resource_movies_list = resp.json()
    # print(resource_movies_list)
    # print(len(resource_movies_list))
    for movie in resource_movies_list:
        movie_dict={}
        image_url = movie['data'][0]['poster']
        title = movie['data'][0]['name']
        average_rating = movie['doubanRating']
        movie_dict['image_url']= image_url
        movie_dict['title']= title
        movie_dict['average_rating']= average_rating
        movie_list.append(movie_dict)
    
    print(movie_list)
    resp.close()
    return movie_list


# movie_top()

"""
import time
movie_dic('Dracula: Dead and Loving It')
time.sleep(30)
movie_dic('My Own Private Idaho')
time.sleep(30)
movie_dic('Star Maps')
"""