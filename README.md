# ElectronicsStore

# Используемые языки и фреймворки
- Python 3.10
- Django 4.0.1

# Используемые технологии
- Docker 20.10.17

# Используемые базы данных
- PostgreSQL 2.9.3
# Запуск проекта
Для начала необходимо сделать клон проекта 
```
git clone https://github.com/ipesotskiiy/Django_Shop
```
После чего необходимо установить библиотеки 
````pip install -r requirements.txt````
Создать .env файл в котором будут указаны данные для бд
Создать дирректорию log и файл log.log

![image](https://github.com/ipesotskiiy/Django_Shop/assets/82309024/10247509-f2e6-41a1-8044-304960991b22)

Сделать миграции ```python manage.py migrate```

### Для локального запуска

```python manage.py runserver```

# Функции API
- http://127.0.0.1:8000/user/registration/ - регистрация пользователя
- http://127.0.0.1:8000/user/confirm_email/ - подтверждение адреса электронной почты
- http://127.0.0.1:8000/user/verify_email/<uidb64>/<token>/ - проверка адреса эектронной почты
- http://127.0.0.1:8000/user/profile - показать профиль пользователя
- http://127.0.0.1:8000/orders/basket - показать корзину пользователя
- http://127.0.0.1:8000/orders/add-to-basket/<str:ct_model>/<str:slug>/ - добавить товар в корзину
- http://127.0.0.1:8000/orders/remove-from-basket/<str:ct_model>/<str:slug>/ - удалить товар в корзину
- http://127.0.0.1:8000/orders/change-quantity/<str:ct_model>/<str:slug>/ - изменить количество товара в корзине
- http://127.0.0.1:8000/orders/checkout/ - проверить заказ
- http://127.0.0.1:8000/orders/make-order/ - создать заказ
- http://127.0.0.1:8000/product/products/<str:ct_model>/<str:slug>/ - страница продукта
- http://127.0.0.1:8000/product/category/<str:slug>/ - показать все товары категории

