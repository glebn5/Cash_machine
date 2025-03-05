# Cash machine

Пет-проект

## Содержание

- [Описание](#описание)
- [Установка и запуск](#установка-и-запуск)

## Описание

Пет-проект / тестовое задание. Пользователь передает массив:    
```items = [1, 1, 2]```   
который хранит в себе id товаров. Программа считывает количество товаров и создает чек (pdf), в котором хранится дата покупки, товары, количество и их стоимость, итоговая стоимость. При содании чека создается qr-code, в котором хранится ссылка на этот чек.


## Установка и запуск

1. Клонируйте репозиторий:  
   ```git clone https://github.com/glebn5/Cash_machine```

2. Создать виртуальное окружение (для Linux)    
```python3 -m venv venv```    
```source venv/bin/activate```    
```pip install -r requirements.txt```

3. Создать виртуальное окружение (для Windows)    
```python3 -m venv venv```    
```venv\Scripts\activate```    
```pip install -r requirements.txt```

4. Настройте базу данных и выполните миграции:  
    ```python manage.py makemigrations```  
    ```python manage.py migrate```  
5. Измените запустите сервер и введите свой ip (например):  
    ```python manage.py runserver 0.0.0.0:8000```

