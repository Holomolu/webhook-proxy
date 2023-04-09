import requests
from bs4 import BeautifulSoup as bs
import time
import random


class Anime:
    def __init__(self):
        self.name = ''
        self.genres = ''
        self.link = ''
        self.episodes = ''
        self.description = ''
        self.data = ''
        self.rate = ''

    def parse(self, url):
        proxies = {
            'http': '172.67.255.222:80'
        }
        r = requests.get(url, proxies=proxies)
        html = bs(r.text, 'lxml')
        episodes = html.find('div', class_='anime-info').findAll('dd', class_='col-6 col-sm-8 mb-1')[1].text
        try:
            int(html.find('div', class_='anime-info').findAll('dd', class_='col-6 col-sm-8 mb-1')[1].text)
        except:
            if '/' in html.find('div', class_='anime-info').findAll('dd', class_='col-6 col-sm-8 mb-1')[1].text:
                episodes = html.find('div', class_='anime-info').findAll('dd', class_='col-6 col-sm-8 mb-1')[1].text
            else:
                episodes = 1

        res = requests.get(
            html.find('div', class_='anime-poster position-relative cursor-pointer').find('img').get('src'))
        out = open("img.jpg", "wb")
        self.name = html.find('div', class_='anime-title').find('h1').text
        self.genres = ', '.join([x.text for x in html.find('dd', class_='col-6 col-sm-8 mb-1 overflow-h').findAll('a')])
        self.link = html.find('link', rel='canonical').get('href')
        self.episodes = episodes
        self.description = html.find('div', class_='description pb-3').text
        self.rate = str(html.find('div', class_='pr-2').text)[:3]
        out.write(res.content)
        out.close()

    def get_link(self):
        return self.link

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_episodes(self):
        return self.episodes

    def get_genres(self):
        return self.genres

    def get_rate(self):
        return self.rate

    def get_all(self):
        return f'{self.name}\nЭпизоды: {self.episodes}\nРейтинг: {self.rate}⭐️\nЖанры: {self.genres}'