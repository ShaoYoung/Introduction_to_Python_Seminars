# Семинар 6
# 3. Дан файл jack.txt (https://disk.yandex.ru/d/orFlUSXkcA600w)
# по аналогии с предыдущим заданием составить аналогичный словарь.


# попробовать получить файл с yandex через requests

import requests
import pprint
from urllib.parse import urlencode

base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
public_key = 'https://disk.yandex.ru/d/orFlUSXkcA600w'  # Ссылка на файл

# Получаем загрузочную ссылку
final_url = base_url + urlencode(dict(public_key=public_key))
response = requests.get(final_url)
# response.json() - вернёт словарь полученный из нужного JSON, ключ HREF ???
download_url = response.json()['href']
print(download_url)

# Загружаем файл и сохраняем его
download_response = requests.get(download_url)
# статус выполнения запроса, если 200, то всё хорошо
print(response.status_code)
file_name_1 = 'jack_requests.txt'
with open(file_name_1, 'wb') as f:   # Путь к файлу
    f.write(download_response.content)

# file_name_2 = 'jack.txt'
# with open(file_name_2, 'r', encoding="utf-8") as data:
#     text_string = data.read()

file_name_2 = file_name_1
# открываем файл и определяем кодировку utf-8
with open(file_name_2, 'r', encoding="utf-8") as data:
    text_string = data.read()

text_string = text_string.lower()
text_string = text_string.strip()
text_string = text_string.replace('.', '').replace(',', '').replace('!', '').replace('?', '')
text_list = text_string.split()
finded_words = []
words_dict = {}
for item in text_list:
    if not item in finded_words:
        words_dict[item] = text_list.count(item)
        finded_words.append(item)
# Печать словаря через pprint.pprint(obj)
pprint.pprint(words_dict)
# for i in words_dict:
#     print(f'{i}: {words_dict[i]}')
