'''Этот модуль предназначен для тестирования класса CinemaParser фукциивывода html страницы '''
from core import CinemaParser
PR = CinemaParser()
PR.extract_raw_content()
print(PR.print_raw_content())
print(PR.find())
