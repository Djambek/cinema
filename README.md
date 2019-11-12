# cinema
Этот модуль предназначен для парсинга [сайта](https://msk.subscity.ru)
Он написан на python3.7. Так же в я использовал requests и BeautifulSoup4.
***
## Зачем нужна эта библиотека
-----------------------------
Каждый человек хоть раз хотел посмотреть фильм в кинотеатре на исходном языке фильма. Тут и приходит на помощь бибилиотека CinemaParse. Этот модуль парсит сайт [https://msk.subscity.ru](https://msk.subscity.ru). На этом сайте можно найти фильмы на их родном языке, где и во сколько они будут показываться и цена билета.
***
`Пока библиотека не дописана`
***
Чтоб начать использование Вы должны открыть командную строку и написать
```
cd куда хотите скачать библиотеку
git clone https://github.com/Dzambek/cinema.git
```
После этого у Вас скачаеться библиотека
* Зайдите в  директорию, в которую Вы скачали библиотеку
* Откройте папку cinema
* Откройте папку cinemaparse
* Запустите файл test.py
***
# Как использовать библиотеку
Для вызова библиотеки напишите:
```python
from core import CinemaParser
```
Есть 5 функций у этой библиотеки.
1. extract_raw_content
2. print_raw_content
3. get_films_list
4. get_film_nearest_session
5. get_nearest_subway_station
Давайте по порядку разбираться что делаеть каждая функция.
***
## extract_raw_content
----------------------
Эта функция предназначена для скачиваания HTML кода с нашей странички, с помощью библиотеки requests.
Вот так её можно вызвать:
```python
from core import CinemaParser
EXAMPLE = CinemaParser()
EXAMPLE.extract_raw_content()
```
Всё!
***
## print_raw_content
--------------------
Эта функция для *красивого* вывода HTML кода.
Пример её вызова:
```python
from core import CinemaParser
EXAMPLE = CinemaParser()
EXAMPLE.extract_raw_content() # Скачиваем HTLM код для того, чтоб у нас было что выводить.
print(EXAMPLE.print_raw_content)
```
***
## get_films_list
-----------------
Эта функция уже поинтересней. В итоге она должна вывести список из названий фильмов.
Как вызывать:
```python
from core import CinemaParser
EXAMPLE = CinemaParser()
EXAMPLE.extract_raw_content() # Ну нам надо что-то парсить.
print(EXAMPLE.get_films_content())
```
***
## get_film_nearest_session
---------------------------
Эта функция уже более прокачанная чем предыдущие. Она требует на вход фильм, про который вы хотите знать информацию.
Информация: где будте ближайжий сеанс этого фильма, во сколько, и в какое время.
Пример:
```python
from core import CinemaParser
EXAMPLE = CinemaParser()
EXAMPLE.extract_raw_content() 
EXAMPLE.some_cycles('Тут название фильма')
print(EXAMPLE.get_film_nearest_session()
```
***
## get_nearest_subway_station
-----------------------------
Вот Вы узнали во сколько фильм. Но куда ехать? На вход функция принимает название кинотеатра.
Пример:
```python
from core import CinemaParser
EXAMPLE = CinemaParser()
EXAMPLE.extract_raw_content() 
print(EXAMPLE.get_nearest_subway_station('Тут название кинотеатра')
```
***
Надеюсь Вам всё понятно.
