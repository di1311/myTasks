import requests
from bs4 import BeautifulSoup
from collections import defaultdict


class ParseWiki:
    URL = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    html = requests.get(URL).text
    animals_dict = defaultdict(int)

    def get_content(self) -> dict:
        print('Wait parse...')
        while True:
            soup = BeautifulSoup(self.html, 'html.parser')
            group = soup.find('div', class_='mw-category-group')
            items = group.find_all('a')
            for item in items:
                self.animals_dict[item['title'][0]] += 1
            stop_parse = soup.find('div', id='mw-pages')  # Проверка на последнюю страницу.
            for item in stop_parse:
                if '(Следующая страница)' in item:  # Текст, без тега <a>, означает последнюю страницу.
                    print('Done!')
                    return self.animals_dict
            links = soup.find('div', id='mw-pages').find_all('a')  # Поиск ссылки на след. страницу
            for link in links:
                if link.text == 'Следующая страница':
                    self.URL = 'https://ru.wikipedia.org/' + link['href']
                    self.html = requests.get(self.URL).text


parser = ParseWiki()
print(parser.get_content())

# result:
""" defaultdict(<class 'int'>, {'А': 1090, 'Б': 1396, 'В': 483, 'Ж': 211, 'Г': 820, 
   'П': 1462, 'Д': 530, 'Е': 27, 'Ё': 2, 'О': 618, 'Я': 171, 'З': 395, 'И': 322, 
   'К': 2003, 'С': 1653, 'Л': 469, 'М': 1055, 'Н': 287, 'Р': 390, 'Т': 766, 'У': 197, 
   'Ф': 169, 'Х': 222, 'Ц': 28, 'Ч': 456, 'Ш': 115, 'Щ': 56, 'Э': 51, 'A': 2558, 
   'B': 765, 'C': 2052, 'D': 740, 'E': 794, 'F': 181, 'G': 592, 'H': 878, 'I': 162, 
  'J': 37, 'K': 37, 'L': 723, 'M': 1418, 'N': 528, 'O': 654, 'P': 2144, 'R': 359, 
   'S': 1479, 'T': 903, 'U': 30, 'W': 71, 'Y': 35, 'Z': 45})
"""
