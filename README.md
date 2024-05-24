# Решение технических заданий

## Оглавление:
- [Задание 1.](#Задание-1)
- [Задание 2.](#Задание-2)
  - [Стек основных технологий.](#Стек-основных-технологий)
  - [Краткое описание и комментарии.](#Краткое-описание-и-комментарии)
  - [Документация API.](#Документация-API)
  - [Как запустить проект.](#Как-запустить-проект)
  - [Как создать суперпользователя.](#Как-создать-суперпользователя)

## Задание 1.
В папке task1 содержится файл task1.py. В нем я написал саму программу, для ее тестирования необходимо подставить конкретные значения в функцию и вывести их значение.

Например:
```
print(repetitive_n_str(10))
```
В терминале выйдет значение: 122333444455555666666777777788888888999999999.

Я не стал включать print в саму программу и я не стал использовать вариант с input, потому что не был уверен, что это добавит какую-то ценность решению.

В то же время, я постарался максимально сократить время работы программы, оптимизировав алгоритм выполнения.

## Задание 2.
Решение содержится в папке task2.

### Стек основных технологий:
- Python
- Django
- DRF
- JWT токены
- Проект написан на Linux

### Краткое описание и комментарии:
Проект магазина продуктов реализовал в соответствии с вводными в техническом задании. Вижу потенциал для улучшения, но своим приоритетом сделал максимальное соответствие реализации проекта указанным требованиям, старался не делать ничего лишнего.

### Документация API:
С документацией API можно подробно ознакомиться после развертывания проекта по адресу:
```
http://127.0.0.1:8000/swagger/
```

### Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:gaifut/Test_Django_Alfa_Ecosystem.git
```
2. Перейти в склонированную папку:
```
cd Test_Django_Alfa_Ecosystem/task2/product_store
```

3. Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
. venv/bin/activate
```

4. Установить зависимости из файла requirements.txt:

```
pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Как создать суперпользователя:
Для удобства в проекте можно создать суперпользователя, у которого будут все права. Для этого в bash терминале в директории с файлом manage.py (по умолчанию это Test_Django_Alfa_Ecosystem/task2/product_store) необходимо ввести команду:
```
python manage.py createsuperuser

```
Далее необходимо следовать инструкциям:
1) Указать имя пользователя (username), напечатав его. Если оставить поле пустым, суперпользователю будет присвоено имя по умолчанию (указано в скобках).
2) Указать адрес электронной почты, поле можно не заполнять и просто нажать enter.
3) Указать пароль, поле обязательное. Имейте в виду, что символы не будут отображаться на экране, просто напечатайте пароль и нажмите enter.
4) Указать пароль повторно, если пароли не совпадут, вернуться в пункт 3 и повторить.
http://127.0.0.1:8000/admin/
После успешного создания суперпользователя его username и password можно использовать для захода в админку по адресу ```http://127.0.0.1:8000/admin/```
