**Stack:**

-mongodb
-mongoengine
-marhsmallow
-Telebot
-flask
-flask-restful
-google cloud
-linux
-nginx
-gunicorn

**Modules**
-Бд
-Бот
-REST API

**DB**
-Category
(title, description, subcategories, parent)
-Product
(title, description, parameters,  in_stock, is_available, price, discount, category)
-Cart
-Customer
(telegram_id, name, address)
-Text
(title, body)

**Tasks Lesson1**
1) Заполнить бд тестовыми данными
2) Реализовать в боте ответ на комманду /start, бот должен отвечать Inline клавиатурой из
всех доступных категорий (root (верхнего уровня)).
3) Подумать о применении колекции Text (Тянуть текст привествия оттуда).


**Tasks Lesson2**
1) Организовать навигационную клавиатуру (из кнопок шаблонов). Следующие кнопки:
1. Категории
2. Товары со скидкой
3. Новости

2) Предусмотреть логику нажатия на каждую кнопку
1. Кнопка "Категории" - бот должен отвечать Inline клавиатурой из
всех доступных категорий (root (верхнего уровня))
2. "Товары со скидкой" - инлайн клавиатура из товаров со скидкой
3. Выводить сообщение с последними тремя новостями (создать и описать колекцию новостей)

**Tasks lesson 3**
1) Предусмотреть поле картинки у модели продуктов
2) Для каждого продукта писать в чат:
1. Картинка
2. Описание позиции
3. Кнопка с приявзкой к айди товара

3) При клике на кнопку "категории" выводить список всех досупных категорий.
3.1) При клике на категорию у которой нету подкатегорий выводить все продукты из неё.

1 сообщение с продуктом = Картинка + Описание + Кнопка

**Tasks lesson 4**
1) Зарегистровать аккаунт на гугл клауде. Создать экземпляр виртуальной машины (VPS) (пункт compute engine).
1.1) ОС - Ubuntu 18.04 Server
1.2) Ресурсы:
 - ЦПУ - 1 ядра
 - ОЗУ - 1.5 - 2
 - диск 40
1.3) Регион европа
 
 *При создании ВМ разрешить HTTP и HTTPS трафик (установить флажок)
 
2) Описать методы сервиса для работы с продуктами
3) Описать модель юзера (предусмотреть максимально информативную сущность) (см message)
4) Подумать над моделью заказа/корзины


** Tasks lesson 5 **

1) Реализовать модель корзины / заказа
2) В боте предоставить возможность добавлять товары в корзину и осуществлять заказы
2.1) В процессе оформления заказа запрашивать у юзера его номер телефона и имя 
3) В боте добавить возможность просматривать историю заказов

***КНОПКА НАЗАД***

** Tasks lesson 6 **
1) Реализовать REST API для манипуляций с юзерами, заказами, продуктами и категориями (использовать BluePrint)
2) Реализовать кнопку назад в навигации меню работы с категориями.
3) Обязательное условие сдачи проекта - он должен быть запущен на сервере через вебхук.