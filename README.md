# REST API приложение с испольлзование FastAPI, PostgreSQL и SQLAlchemy
FastAPI is a Python framework and set of tools that allow developers to invoke commonly used functions using a REST interface. 

SQLAlchemy is a package that makes it easier for Python programs to communicate with databases. Most of the time, this library is used as an Object Relational Mapper (ORM) tool, which automatically converts function calls to SQL queries and translates Python classes to tables on relational databases.

# 1 Подготовка сервера

### 1.1 Установа Docker в Ubuntu 20.04

### 1.2 Установка Docker Compose в Ubuntu 20.04
Установить Docker Compose можно из официального репозитория Ubuntu, однако тогда вы получите не самую свежую версию, потому лучше установить программу из GitHub-репозитория Docker.

Найдите ссылку на свежий релиз на этой странице. На данный момент это версия 1.26.0.

Следующая команда загрузит эту версию и сохранит исполняемый файл в /usr/local/bin/docker-compose, что сделает его глобально доступным как docker-compose:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

Теперь установите права и сделайте файл исполняемым:
```
sudo chmod +x /usr/local/bin/docker-compose
```

Запросите версию программы, чтобы убедиться, что установка прошла успешно:
```
docker-compose --version
```

Команда должна вернуть что-то вроде:
```
docker-compose version 1.26.0, build 8a1c60f6
```

# 2 Запуск проекта на сервере

### 2.1 Счачиваем проект с GitHub
Клонируем проект в локальную директорию:
``` 
git clone https://github.com/profile-55/NOTES.git
 
```

### 2.2 Устанавливаем виртульное окружение для проекта
Добавляем виртуальное окружение в папку проекта:
```
python -m venv path/to/project/venv
```
Активируем его:
```
cd path/to/project/
venv/Sctipts/activate.bat (для Windows)
venv/bin/activate (для Linux)
```
Устанавливаем зависимости в виртуальное окружение:
```
pip install -r requirements.txt
```

### 2.3 Запускаем контейнер для Postgres:
```
sudo docker run -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=newp55! -e POSTGRES_DB=tasks_base -d -p 5432:5432 postgres:latest
```

### 2.4 Создаём базу данных
```
python create_db.py
```

### 2.5 Запускаем uvicorn-сервер
Для запуска выполняем следующую команду:
```
uvicorn main:app --reload
```

# 3 Тестрирование API
### 3.1 Встроенный инструментарий FastAPI
Для тестирования API удобно пользоваться
инструментами, которые предоставляет
сам фреймворк FastAPI. Они доступны по следующей
ссылке:
```
http://locahost:8000/docs
```

