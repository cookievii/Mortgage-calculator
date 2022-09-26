## Проект "Калькулятор ипотечных предложений". :bank:

### Стэк технологий:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

---

# Техническое задание

Необходимо разработать калькулятор ипотечных предложений на основе [примера](https://www.sravni.ru/ipoteka/?mortgagePurpose=1&creditAmount=11849421&initialAmount=1500000&mortgageTerm=120).

[Пример API](https://documenter.getpostman.com/view/6802079/UVeAvonG) c образцами запросов который нужно реализовать

----

### Пользовательский сценарий
Клиент вводит следующие данные:
1. Стоимость объекта недвижимости, в рублях без копеек. Тип данных: integer
2. Первоначальный взнос, в рублях без копеек. Тип данных: integer
3. Срок, в годах. Тип данных: integer

В ответ ему приходит массив с объектами ипотечных предложений. В каждом объекте есть следующие данные:
1. Наименование банка. Тип данных: string
2. Ипотечная ставка, в процентах. Тип данных: float
3. Платеж по ипотеке, в рублях без копеек.  Тип данных: integer

----

### Технические требования
Исходя из выше описанного пользовательского сценария, нужно:
1. Написать модель для хранения ипотечных предложений.
2. Написать ViewSet для реализации функционала CRUD ипотечных предложений.
3. Фильтрацию ипотечных предложений, по введенным параметрам.
4. Реализовать функционал, который будет рассчитывать платеж у всех валидных ипотечных предложений.

Следущие пункты не обязательны, но мы будем рады увидеть их:
1. Сортировка ипотечных предложений по ставке(процент по ипотеке) и по платежу. 
2. Тесты для всего вышеперечилсенного.

----

### Используемый стек
1) Django. Обязательно
2) [DRF](https://www.django-rest-framework.org/). Обязательно
3) [django-filters](https://django-filter.readthedocs.io/en/stable/guide/usage.html). По желанию

----

#### Для начала работы, сделайте форк репозитория (и сделайте его приватным), склонируйте его и начинайте разработку.

----
### Локальный запуск приложения
```shell
# - Cкачайте:
git clone git@github.com:cookievii/Foodgram.git

# - Запустите приложения в контейнерах:
docker-compose up -d --build

# - Создайте суперпользователя Django:
docker-compose exec backend python manage.py createsuperuser
```
Сервис будет доступен по ссылке [http://localhost:8000/admin/login/?next=/admin/](http://localhost:8000/admin/login/?next=/admin/)

