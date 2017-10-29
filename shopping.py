# coding:utf-8
#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from colorama import init, Fore

init()

class ShopCollection():

    def __init__(self, page):
        self.header = '序号 优惠精选 商城 时间'.split()
        self.domain = 'http://www.huihui.cn/all?ajax=true&page='
        self.url = self.domain + str(page)

    @property
    def get_shop(self):
        headers1 = {'User-Agent': 'ua.random'}
        response = requests.get(self.url, headers=headers1)
        soup = BeautifulSoup(response.text, 'html.parser')
        shops = soup.select(".list-simple")
        for index, shop in enumerate(shops):
            shop_msg = shop.select('.ctn a')
            if index%2 == 0:
                shop_title = Fore.CYAN + shop_msg[0].text.strip() + Fore.RESET
                shop_mall = Fore.CYAN + shop_msg[5].text.strip() + Fore.RESET
                time = Fore.CYAN + shop.select('.time')[0].text + Fore.RESET
                index = Fore.CYAN + str(index) + Fore.RESET
            else:
                shop_title = shop_msg[0].text.strip()
                shop_mall = shop_msg[5].text.strip()
                time = shop.select('.time')[0].text
            shop_list = [index, shop_title, shop_mall, time]
            yield shop_list

    def pretty_print(self):
        pt = PrettyTable(self.header)
        pt.align = "l"
        pt.valign = "m"
        for shop in self.get_shop:
            pt.add_row(shop)
        print(pt)

def query(page=3):
    for i in range(page):
        B = ShopCollection(i+1)
        B.pretty_print()
        if (i+1) < page:
            print('第{}页'.format(str(i+1)))
            option = input('继续按N，其他退出：')
            if option.upper() == 'N':
                continue
            else:
                break

if __name__ == '__main__':
    query()