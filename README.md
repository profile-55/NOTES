# Build a REST API with FastAPI, PostgreSQL and SQLAlchemy
FastAPI is a Python framework and set of tools that allow developers to invoke commonly used functions using a REST interface. 

SQLAlchemy is a package that makes it easier for Python programs to communicate with databases. Most of the time, this library is used as an Object Relational Mapper (ORM) tool, which automatically converts function calls to SQL queries and translates Python classes to tables on relational databases.

Many web, mobile, geospatial, and analytics applications use PostgreSQL as their primary data storage or data warehouse.

# 1: Подготовка сервера:

## 1.1: Установа Docker в Ubuntu 20.04:

## 1.2: Установка Docker Compose в Ubuntu 20.04:
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

# GitHub:

## How to run the REST API
Get this project from Github
``` 
git clone https://github.com/profile-55/NOTES.git
 
```



### Setting up the database

* Install PostgreSQL and create your user and database

* Change this line in ` database.py ` to 

``` 
engine=create_engine("postgresql://{YOUR_DATABASE_USER}:{YOUR_DATABASE_PASSWORD}@localhost/{YOUR_DATABASE_NAME}",
    echo=True
)
```

### Create a virtual environment
This can be done with 
``` python -m venv env ```

activate the virtual environment with 

``` 
env/bin/activate
```

or 

```
env\Scripts\activate
```



### Install the requirements 

``` 
pip install -r requirements.txt
```

### Create the database
``` python create_db.py ```

## Run the API
``` python main.py ```

## Author 
[Ssali Jonathan](https://github.com/jod35)
