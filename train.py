# coding:utf-8
#!/usr/bin/python3

import requests
from prettytable import PrettyTable
from colorama import init, Fore
import urllib3

init()
urllib3.disable_warnings()
def get_station():
    import re
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9028'
    response = requests.get(url, verify=False)
    stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
    stations = dict(stations)
    return stations

def query(from_station, to_station, train_date, options):
    stations = get_station()
    #获取中文车站名称的对应编号
    from_station_code = stations.get(from_station)
    to_station_code = stations.get(to_station)
    #车站编号判定，不存在返回错误，存在则进行查询解析
    if from_station_code and to_station_code:
        query_url= 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&' \
                   'leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'
        url = query_url.format(train_date, from_station_code, to_station_code)
        response = requests.get(url, verify=False)
        #若12306接口更换，需获取response重新解析
        #查询结果，list
        try:
            available_trains = response.json()['data']['result']
            #车站代码与车站名称映射字典
            map_stations = response.json()['data']['map']
            T = TrainsCollection(available_trains, map_stations, options)
            T.pretty_print()
        except:
            print('未查询到任何结果.请检查输入的车站及日期是否正确.\n -h 查看帮助')
    else:
        print('车站名称【{}】不存在'.format(from_station)) \
            if not from_station else print('车站名称【{}】不存在'.format(to_station))

class TrainsCollection:

    header = '车次 出发站 到达站 出发时间 到达时间 历时 日期 商务座 一等 二等 软卧 硬卧 硬座 无座 预订状态'.split()

    def __init__(self, available_trains, stations, options):
        """查询到的火车班次集合
        :param available_trains: 一个列表, 包含可获得的火车班次, 每个火车班次是一个list
        :param stations: 车站代码与车站名称的对应关系，字典
        :param options: 查询的选项, 如高铁, 动车
        """
        self.available_trains = available_trains
        #self.stations = {value:key for key,value in stations.items()}
        self.stations = stations
        self.options = options

    @property
    def trains(self):
        for raw_train in self.available_trains:
            raw_train = raw_train.split('|')
            station_train_code = raw_train[3]
            train_type = station_train_code[0].lower()
            if not self.options or train_type in self.options:
                from_station = Fore.GREEN + self.stations.get(raw_train[6]) + Fore.RESET
                to_station = Fore.RED + self.stations.get(raw_train[7]) + Fore.RESET
                start_time = raw_train[8]
                arrive_time = raw_train[9]
                lishi = raw_train[10]
                start_train_date = raw_train[13]
                swz_num = raw_train[32] if raw_train[32] else '--'
                zy_num = raw_train[31] if raw_train[31] else '--'
                ze_num = raw_train[30] if raw_train[30] else '--'
                rw_num = raw_train[23] if raw_train[23] else '--'
                yw_num = raw_train[28] if raw_train[28] else '--'
                yz_num = raw_train[29] if raw_train[29] else '--'
                wz_num = raw_train[26] if raw_train[26] else '--'
                canWebBuy = Fore.RED + raw_train[11] + Fore.RESET
                train=[station_train_code,from_station,to_station,start_time,arrive_time,lishi,start_train_date,swz_num,zy_num,ze_num,rw_num,yw_num,yz_num,wz_num,canWebBuy]
                yield train

    def pretty_print(self):
        pt = PrettyTable(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)


