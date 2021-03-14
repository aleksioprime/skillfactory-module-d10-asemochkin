# skillfactory-module-d10-asemochkin
Практика D10

Для разворачивания проекта на локальном сервере:
1. Скачайте репозиторий на локальный диск и разархивируйте
2. Через командную строку перейдите в текущий каталог проекта (куда разархивировали репозиторий)
3. Установите все зависимости:
```
% pip3 install -r requirements.txt
```
4. Запустите локальный сервер:
```
% python3 manage.py runserver
```
5. Перейдите по адресу http://127.0.0.1:8000 для проверки функциональности

Для добавления и редактирования записей перейдите в раздел администрирования:
```
http://127.0.0.1:8000/admin
```
Данны для входа суперпользователя:

login: admin

password: 12345
