# Django сайт с динамическими страницами

Сайт с использованием шаблонов и динамических маршрутов.

Сайт демонстрирует базовые возможности Django, включая использование переменных в URL и шаблоны.

## О сайте

Сайт включает 5 страниц:
1. **Home** — содержит приветственное сообщение.
2. **About** — описание (без текста).
3. **Contact** — контактная информация и форма для отправки сообщения.
4. **Page 1** — страница с параметром в URL (пример: `/page1/param`).
5. **Page 2** — страница с двумя параметрами в URL (пример: `/page2/param1/param2`).
   

## Установка

1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/MosZsa/DjangoLab2.git
   cd your repository

2. Запустите сервер:
   ```bash
   python manage.py runserver
   
3. Откройте проект в браузере по адресу http://127.0.0.1:8000/.