'''Этот модуль предназначен для тестирования класса CinemaParser фукциивывода html страницы '''
from core import CinemaParser
PR = CinemaParser()
PR.extract_raw_content()
print("Введите название фильма")
i = input()
print("Введите название кинотеатра")
b = input() 
print(PR.get_films_list())
PR.some_cycles(i)
print(PR.get_film_nearest_session())
print(PR.get_nearest_subway_station(b))
