# coding:utf-8
#!/usr/bin/python3


import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from colorama import init, Fore
init()

class MovieCollection():

    def __init__(self, movies, options):
        self.movies = movies
        self.options = options
        self.header = '名称 地区 主演 时长 豆瓣评分 备注'.split()

    @property
    def get_movie(self):
        for movie in self.movies:
            title = Fore.GREEN + movie['data-title'] + Fore.RESET
            duration = movie['data-duration']
            region = movie['data-region'].split()
            director = movie['data-director']
            actors = movie['data-actors'].split('/')
            try:
                score = movie['data-score']
                status = Fore.GREEN + '正在上映' + Fore.RESET
                flag = '-n'
            except:
                score = '--'
                status = Fore.RED + '即将上映' + Fore.RESET
                flag = '-c'
            if not self.options or flag in self.options:
                movie = [title, region[0], actors[0], duration, score, status]
                yield movie

    def pretty_print(self):
        pt = PrettyTable(self.header)
        for movie in self.get_movie:
            pt.add_row(movie)
        print(pt)


def query(options):
    movies = get_movie()
    M = MovieCollection(movies, options)
    M.pretty_print()

def get_movie():
    url = 'https://movie.douban.com/cinema/nowplaying/chengdu/'
    headers1 = {'User-Agent': 'ua.random'}
    response = requests.get(url, headers=headers1)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = soup.select('.list-item')
    return movies



