Домашнее задание из модуля D10
Для запуска:

1.Скопировать в локальную папку на компьютере
2.Создать виртуальное окружение (например: virtualenv venv)
    Активировать: source venv/bin/activate
    Установить нужные пакеты: pip install -r requirements.txt
3.Перейти в папку с проектом произветси миграции: 
    python3 manage.py makemigrations
    python3 manage.py migrate
4.Запустить сервер: python3 manage.py runserver
