# REST API приложение с испольлзование FastAPI, PostgreSQL и SQLAlchemy
FastAPI is a Python framework and set of tools that allow developers to invoke commonly used functions using a REST interface. 

SQLAlchemy is a package that makes it easier for Python programs to communicate with databases. Most of the time, this library is used as an Object Relational Mapper (ORM) tool, which automatically converts function calls to SQL queries and translates Python classes to tables on relational databases.

# 1 Подготовка сервера

## 1.1 Установа Docker в Ubuntu 20.04

## 1.2 Установка Docker Compose в Ubuntu 20.04
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

## Как запустить проект
Клонируем проект в локальную директорию:
``` 
git clone https://github.com/profile-55/NOTES.git
 
```

### Запускаем базу данных Postgres в Docker
```
sudo docker run -e POSTGRES_PASSWORD=newp55! -e POSTGRES_DB=tasks_base -d -p 5432:5432 postgres:latest
```

### Собираем Docker-образ для python и uvicorn
Для того чтобы собрать Docker-образ переходим в каталог, содержащий Dockerfile, и выполняем следующую команду:
```
sudo docker build .
```

### Запускаем uvicorn-сервер
```
sudo docker run -p 8000:8000 ...
```


# 3 Тесты
### Переходим в контейнер

### Тестируем приложение

