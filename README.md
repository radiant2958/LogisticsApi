# Сервис Logistics API


## Описание

Этот сервис представляет собой полноценное RESTful API, созданное с использованием Django REST Framework (DRF). 
Он предназначен для облегчения поиска ближайших доступных машин для транспортировки грузов, а также для управления информацией о грузах и машинах.


## Стек: Python3.11, Django REST Framework, PostgreSQL, Docker, Docker Compose, geopy, Celery.


## Функционал

- **Создание груза**: POST `/cargos/create/`
  Создает новый груз с указанием места погрузки и выгрузки по zip-коду, веса и описания.

- **Список грузов**: GET `/cargos/`
  Возвращает список всех грузов, для каждого груза отображается список ближайших машин в радиусе 450 миль.

- **Детали груза**: GET `/cargos/<int:pk>/`
  Возвращает информацию о конкретном грузе по ID, включая места погрузки и выгрузки, вес, описание и список всех машин с расстоянием до груза.

- **Редактирование машины**: PATCH `/vehicles/<int:pk>/update/`
  Обновляет информацию о машине по ID, включая текущую локацию по zip-коду.

- **Редактирование груза**: PATCH `/cargos/<int:pk>/update/`
  Обновляет информацию о грузе по ID, включая вес и описание.

- **Удаление груза**: DELETE `/cargos/<int:pk>/delete/`
  Удаляет груз по ID.
  
- **Сортировка списка грузов по весу(от меньшего к большему)**: GET `/cargos/filter/`

- **Фильтрации списка грузов по радиусу машин**:  GET `cargos/filter/radius/?radius=500`

- **Aвтоматическое обновление локаций всех машин раз в 3 минуты**: локации всех машин автоматически обновляются каждые 3 минуты, перемещаясь в случайную локацию.


## Инструкция по запуску через Docker Compose

Убедитесь, что Docker и Docker Compose установлены на вашей машине. 

1. Клонируйте репозиторий проекта:

```sh
git clone https://github.com/radiant2958/LogisticsApi.git
```

2. Перейдите в папку проекта:

```sh
cd имя_папки_проекта
```

3. Соберите и запустите контейнеры с помощью Docker Compose:

```sh
docker-compose up --build -d
```

4. После запуска контейнеров приложение будет доступно по адресу http://localhost:8000/ в вашем браузере.

