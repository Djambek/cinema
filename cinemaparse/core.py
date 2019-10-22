"""4 пробела!!!"""
import requests
from bs4 import BeautifulSoup
class CinemaParser:
    ''' Этот класс очень нужен'''
    def __init__(self, city='msk'):
        ''' Узнаём город'''
        self.city = city
        self.content = ''
    def extract_raw_content(self):
        ''' Скачиваем HTML с сайта '''
        url = 'https://msk.subscity.ru'
        self.content = requests.get(url)
    def print_raw_content(self):
        '''Красивый вывод HTML'''
        soup = BeautifulSoup(self.content.text, 'html.parser')
        return soup.prettify()

