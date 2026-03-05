Требуется Python 3.12.3

Установка:
1. создайте директорию на рабочем столе 
- mkdir test_todo
2. зайдите в директорию 
- cd test_todo

Установите вирт. среду в директории test_todo:
1. python3 -m venv venv
2. source venv/bin/activate

Склонируйте проект:
1. git clone git@github.com:l9l9n/todo2.git
2. зайдите в директорию cd todo2
3. выполните след. команды
- pip install -r requirements.txt
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py runserver

Сервер запустится на http://localhost:8000

После запуска сервера откройте новый терминал и вызовите след. API.

Получение всех записей.
- curl http://localhost:8000/todos

первый раз выведет пустой массив!!!


Создание записи.

- curl -i -X POST http://localhost:8000/todos -H "Content-Type: application/json" -d '{"text": "Buy milk"}'






