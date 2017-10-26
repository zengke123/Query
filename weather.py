# coding:utf-8
#!/usr/bin/python3

import requests
import json
from prettytable import PrettyTable
from colorama import init, Fore
init()

class WeatherCollection():

    def __init__(self, location):
        self.KEY = '314b9c10fadce8dadcf7bb6aa756f49e'
        self.WEATHER_API = 'http://restapi.amap.com/v3/weather/weatherInfo?'
        self.ADCODE_API = 'http://restapi.amap.com/v3/geocode/geo?'
        self.OPTION = 'all'
        self.location = location
        self.header = '地区 日期 星期 白天天气 白天温度 白天风向 白天风速 夜间天气 夜间温度 夜间风向 夜间风速'.split()

    def _get_adcode(self):
        result = requests.get(self.ADCODE_API, params={
            'key': self.KEY,
            'address': self.location
        }, timeout=1)
        result = json.loads(result.text)
        try:
            geocode = result.get('geocodes')[0]
            adcode = geocode.get('adcode')
            return adcode
        except:
            print('请输入正确地址')


    @property
    def get_weather(self):
        adcode = self._get_adcode()
        if adcode:
            result = requests.get(self.WEATHER_API, params={
                'key': self.KEY,
                'city': adcode,
                'extensions': self.OPTION
            }, timeout=1)
            result = json.loads(result.text)
            forecasts = result.get('forecasts')[0]
            city = forecasts.get('province') + ',' + forecasts.get('city')
            # 获取3天的天气信息
            casts = forecasts.get('casts')
            for weather in casts:
                date = weather.get('date')
                week = weather.get('week')
                dayweather = weather.get('dayweather')
                daytemp = Fore.GREEN + weather.get('daytemp') + Fore.RESET
                daywind = weather.get('daywind')
                daypower = weather.get('daypower')
                nightweather = weather.get('nightweather')
                nighttemp = Fore.GREEN + weather.get('nighttemp') + Fore.RESET
                nightwind = weather.get('nightwind')
                nightpower = weather.get('nightpower')
                # 地区 日期 星期 白天天气 白天温度 白天风向 白天风速 夜间天气 夜间温度 夜间风向 夜间风速
                weather = [city, date, week, dayweather, daytemp, daywind, daypower, nightweather, nighttemp, nightwind,
                           nightpower]
                yield weather

    def pretty_print(self):
        pt = PrettyTable(self.header)
        for weather in self.get_weather:
            pt.add_row(weather)
        print(pt)


def query(city):
    W = WeatherCollection(city)
    W.pretty_print()




