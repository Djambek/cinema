'''Этот модуль предназначен для тестирования класса CinemaParser '''
from core import CinemaParser
pr = CinemaParser()
pr.extract_raw_content()
print(pr.print_raw_content())

