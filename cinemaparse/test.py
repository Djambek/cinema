'''Этот модуль предназначен для тестирования класса CinemaParser фукциивывода html страницы '''
from core import CinemaParser
PR = CinemaParser()
PR.extract_raw_content()
print("Введите название фильма")
i = input()
print("Введите название кинотеатра")
b = input() 
print(PR.get_films_list())
print(PR.get_film_nearest_session(i))
print(PR.get_nearest_subway_station(b))
