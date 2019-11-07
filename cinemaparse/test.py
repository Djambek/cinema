'''Этот модуль предназначен для тестирования класса CinemaParser фукциивывода html страницы '''
from core import CinemaParser
PR = CinemaParser()
PR.extract_raw_content()
print("Введите название фильма, который Вы хотите посмотреть")
i = input()
print("Введите название кинотеатра")
b = input()
print(PR.found())
print(PR.sesion(i))
print(PR.get_nearest_subway_station(b))
