"""4 пробела!!!"""
import requests
from bs4 import BeautifulSoup
class CinemaParser:
    ''' Этот класс очень нужен'''
    def __init__(self, city='msk'):
        ''' Узнаём город'''
        self.city = city
        self.content = ''
        self.film = []
    def extract_raw_content(self):
        ''' Скачиваем HTML с сайта '''
        url = 'https://msk.subscity.ru'
        self.content = requests.get(url)
    def print_raw_content(self):
        '''Красивый вывод HTML'''
        soup = BeautifulSoup(self.content.text, 'html.parser')
        return soup.prettify()
    def found(self):
        ''' Это фунция ведёт поиск тегов с фильмами'''
        soup = BeautifulSoup(self.content.text, 'html.parser')
        #print(soup.find_all('div', class_="movie-titles"))
        for i in soup.find_all('div', class_="movie-titles"):
            for j in i.find_all('div', class_="movie-title"):
                for key in j.find_all('a', class_="underdashed"):
                    self.film.append(key.text.replace('\xad', ''))
        return self.film
