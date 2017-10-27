# coding:utf-8
#!/usr/bin/python3
"""命令行查看工具

Usage:
    query [-TgdtkzMncpW]  ((<from>  <to>  <date>)|()| (<city>))

Options:
    -h,--help   显示帮助菜单
    -T          火车票查询
        -g      高铁
        -d      动车
        -t      特快
        -k      快速
        -z      直达

    -M          电影查询
        -n      正在上映
        -c      即将上映
        -p      实时票房

    -W          天气查询

Example:
    query -T 北京 上海 2017-10-24
    query -T 成都 南京 2017-10-24 -dg
    query -M
    query -W 四川大学
"""

import train
import movie
import weather
from docopt import docopt

def query():
    arguments = docopt(__doc__)
    options = ''.join([key for key, value in arguments.items() if value is True])
    from_station = arguments['<from>']
    to_station = arguments['<to>']
    train_date = arguments['<date>']
    args = [arg for arg in options if arg.isupper()]
    if len(args) == 1:
        if arguments.get('-T'):
            options = options.replace('-T', '')
            train.query(from_station, to_station, train_date, options)
        elif arguments.get('-M'):
            options = options.replace('-M', '')
            movie.query(options)
        elif arguments.get('-W'):
            city = arguments['<city>']
            weather.query(city)

    else:
        print('请输入正确的参数.\n -h 查看帮助')

if __name__ == '__main__':
    query()
