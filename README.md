# Miner

Задача
------

* В соответствии с данной [спецификацией](https://minesweeper-test.studiotg.ru/swagger/) нужно реализовать веб-сервер с REST API.
Проверить работу данного сервера можно прямо в [этой](https://minesweeper-test.studiotg.ru/) же форме, просто заменив URL API на свой локальный

Основные технологии
-------------------

```
* Python 3.12.0
* Django 5.0.1
* Django REST Framework 3.14.0
```

Установка и запуск
------------------

* Переходим в директорию проекта

```cd backend```

* Создаем файл .env такой же, как .env.example (меняем настройки при необходимости)

```touch .env```

* Создаем виртуальное окружение

```python3 -m venv venv```

* Активируем виртуальное окружение

```source venv/bin/activate```

* Устанавливаем зависимости

```pip install -r requirements.txt```

* Выполняем миграции

```python3 manage.py migrate```

* Собираем статику

```python3 manage.py collectstatic```

* Запуск

```python3 manage.py runserver```
