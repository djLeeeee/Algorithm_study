#!/bin/python3

import math
import os
import random
import re
import sys



from urllib import request
import json

def get_movie_data(genre, page_num):
    req = request.Request(f"https://jsonmock.hackerrank.com/api/tvseries?page={page_num}")
    res = request.urlopen(req)
    data = json.loads(res.read().decode('utf-8'))
    movies = data["data"]
    if page_num > data["total_pages"]:
        raise Exception("최대 페이지에 도달했습니다.")
    print(page_num, movies[0]["name"])
    return [movie for movie in movies if genre in movie["genre"]]

def get_genre_movie(genre):
    genre_movies = []
    page_num = 1
    while (True):
        try:
            movies = get_movie_data(genre, page_num)
            genre_movies.extend(movies)
            page_num += 1
        except:
            break
    return genre_movies
    
def bestInGenre(genre):
    genre_movies = get_genre_movie(genre)
    genre_movies.sort(key = lambda x: (-x["imdb_rating"], x["name"]))
    return genre_movies[0]["name"]
    

if __name__ == '__main__':


    genre = "Animation"

    result = bestInGenre(genre)
    print(result)


