# bigDATA project

В new_producer.py генерируются данные в режиме демона, которые имитируют работы датчиков по измерению температуры. Все данные заносятся в kafka, а после в new_consumer.py считываются данные из kafka и записываются в базу данных (postgres/greenplum) в слой сырых данных stg. С помощью airflow раз в минуту эти данные считываются, фильтруются записи с положительной температурой и записываются в слой готовых данных dds.  

# Руководство по запуску
Для работы проекта нужен установленный docker v20.10.24 и выше, docker-compose v2.17.2
1. Скачиваем проект с гита 
2. Далее заходим в папку airflow через терминал или через проводника. В этой папке запускаем команду ```docker-compose up airflow-init``` (эта команда подготовит обрза для локального развертвования apache airflow).
3. Далее в этой же папке запускаем команда ```docker-compose up``` для того, чтобы поднять apache airflow. По адресу http://localhost:8080/ откроета графический интерфейс airflow (логин - airflow, пароль - airflow). 
4. Запускам команду ```docker-compose up``` в папке kafka. После успешного поднятия контейнеров запускаем команду ```docker exec -it kafka /bin/sh```. 
Далее выполняем ряд команд, чтобы сосдать топик: ```cd /opt/kafka_<version>/bin``` где <version> - версия кафки. 
```kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic first_kafka_topic```

# Структура проекта:
    📁 bigDIG/
    ├─📁 Kafak/
    │ ├─📄 conf.py
    │ ├─📄 docker-compose.yml
    │ ├─📄 new_consumer.py
    │ └─📄 new_producer.py
    ├─📁 airflow/
    │ ├─📁 dags/
    │ │ └─📄 project_dag.py
    │ ├─📁 logs/
    │ ├─📁 plugins/
    │ ├─📄 .env
    │ └─📄 docker-compose.yml
    ├─📁 gp/
    │ └─📄 docker-compose.yml
    ├─📁 postgres/
    │ └─📄 docker-compose.yml
    └─📄 README.md

# Архитектура проекта
![Схема](https://github.com/BlackP8/bigDIG/blob/main/ар.jpg)
