# API Facebook groups
 
Выгружает комиксы в группу Facebook с сайта [xkcd](https://xkcd.com/).

### Как установить 
Для начала необходимо создать группу на [Facebook](https://www.facebook.com/groups/feed/). Нажимаем на клавишу [Создать новую группу](https://www.facebook.com/groups/?category=create). После чего в URL будет ID группы, которое необходимо внести в файл `.env`.
Пример:
```
GROUP_ID="649448483222002"
```
___
Для получения FACEBOOK_TOKEN необходимо зайти на [Meta for Developers](https://developers.facebook.com/apps) 
Далее: 
1. Создать новое приложение.
2. Добавить продукт ""Вход через Facebook"". 
3. Зайти на [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
4. Маркер пользователя.
5. Добавить разрешения:
	- pages_messaging
	- publish_to_groups
	- groups_access_member_info
	public_profile
6. Генерируем токен (Данный токен временный (1 час))
7. Переходим на [Отладчик маркеров доступа](https://developers.facebook.com/tools/debug/accesstoken/)
8. Вносим в строку полученный токен и нажимаем ""Отладка"".

Двухмесячный токен сгенерирован.
Вносим его в файл `.env`.
Пример:
```
FACEBOOK_TOKEN="EAAJK5Q1AVZBoBAMnjS4se7dzwAkpvKlt299s7d4ogZC1LDooICCfi7gqElogY0VZBY4WNf0nIzfET"
```
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
___
### Запуск программы

Для ежедневной выгрузки комиксов с их описанием в указанную группу Facebook с сайта [xkcd](https://xkcd.com/), вводим в командной строке следующим образом:
```
..API_Facebook>python3 upload_comics.py
```
Так же принимает на вход часы, с частотой которых буду выгружаться комиксы. Если часы не заданы по стандарту, то программа берёт 24 часа.
Пример внесения 8-ми часового таймаута для выгрузки фото:
```
..API_Facebook>python3 upload_comics.py -t 8
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).