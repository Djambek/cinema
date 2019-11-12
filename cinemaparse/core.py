"""4 пробела!!!"""
import requests
from bs4 import BeautifulSoup

class CinemaParser:
    ''' Этот класс очень нужен'''

    def __init__(self, city='msk'):
        ''' Узнаём город'''
        self.city = city
        self.content = ''
        self.number = 0
        self.station = []
        self.name = []
        self.film = []
        self.site = []
        self.name = []
    def extract_raw_content(self):
        ''' Скачиваем HTML с сайта '''
        url = 'https://{}.subscity.ru'.format(self.city)
        self.content = requests.get(url)

    def print_raw_content(self):
        '''Красивый вывод HTML'''
        soup = BeautifulSoup(self.content.text, 'html.parser')
        return soup.prettify()

    def get_films_list(self):
        ''' Это фунция ведёт поиск тегов с фильмами'''
        soup = BeautifulSoup(self.content.text, 'html.parser')
        for i in soup.find_all("div", class_='movie-plate'):
            self.film.append(i["attr-title"])
            # print(i["attr-title"])
        return self.film

    def some_cycles(self, name):
        '''Просто так'''
        b_0 = 0
        for name_film in range(len(self.film)):
            if str(self.film[name_film]).upper() == str(name).upper():
                self.number = name_film
                b_0 = 1
        if b_0 == 0:
            raise TypeError("Нет такого фильма")
        print(len(self.film))
        print(self.number)
        url = 'https://{}.subscity.ru'.format(self.city)
        self.content = requests.get(url)
        soup = BeautifulSoup(self.content.text, 'html.parser')
        for film in soup.find_all('div', class_="movie-title"):
            for text_film in film.find_all("a", class_="underdashed"):
                self.site.append(url + text_film['href'])

    def get_film_nearest_session(self):
        '''Эта функции выдаёт поиск по фильму'''

        day = []
        t_str = ''
        time = []
        cinema_name = []
        self.content = requests.get(self.site[self.number])
        print(self.site[self.number])
        soup = BeautifulSoup(self.content.text, 'html.parser')
        for day_of_film in soup.find_all('h3', class_='header-day text-center'):
            day.append(day_of_film.text)
        t_str = "table table-bordered table-condensed table-curved table-striped table-no-inside-"
        for cinema_time in soup.find('table', class_=t_str+'borders'):
            for time_ in cinema_time.find_all("td", class_="text-center cell-screenings"):

                time.append(str(time_.text)[:5].replace(':', '.'))

        for list_cinema_name in soup.find_all('div', class_='cinema-name'):
            for name_text in list_cinema_name.find_all('a', class_="underdashed"):
                cinema_name.append(name_text.text)

        val, idx = min((val, idx) for (idx, val) in enumerate(time))
        return val, day[idx], cinema_name[idx]

    def get_nearest_subway_station(self, name_cinema):
        '''Возвращает ближайшие метро к кинотеатру'''

        url = 'https://{}.subscity.ru/cinemas'.format(self.city)
        self.content = requests.get(url)
        soup = BeautifulSoup(self.content.text, 'html.parser')
        for div_1 in soup.find_all('div', class_="cinema-name"):
            for a_0 in div_1.find_all('a', class_="underdashed"):
                self.name.append(a_0.text)
                # print(a_0.text)
        for span_1 in soup.find_all('span', class_="medium-font location"):
            self.station.append(span_1.text)
        self.number = 0
        for i in range(len(self.name)):
            if name_cinema == self.name[i]:
                self.number = 1
                return self.station[i]

        if self.number == 0:
            raise TypeError('Вы неправельно ввели название кинотеатра')
        return None
