# bigDATA project

В new_producer.py генерируются данные в режиме демона, которые имитируют работы датчиков по измерению температуры. Все данные заносятся в kafka, а после в new_consumer.py считываются данные из kafka и записываются в базу данных (postgres/greenplum) в слой сырых данных stg. С помощью airflow раз в минуту эти данные считываются, фильтруются записи с положительной температурой и записываются в слой готовых данных dds.  

# Руководство по запуску
1. Скачиваем проект с гита 
2. Далее заходим в папку airflow через терминал или через проводника. В этой папке запускаем команду ``` docker-compose up airflow-init```

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
