import sqlite3

# Функция для создания таблицы Products, если она не существует
def initiate_db():
    conn = sqlite3.connect('products.db')  # Подключение к базе данных
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Products (
                 id INTEGER PRIMARY KEY,
                 title TEXT NOT NULL,
                 description TEXT,
                 price INTEGER NOT NULL
                 )''')
    conn.commit()
    conn.close()

# Функция для получения всех продуктов из таблицы Products
def get_all_products():
    conn = sqlite3.connect('products.db')  # Подключение к базе данных
    c = conn.cursor()
    c.execute("SELECT * FROM Products")
    products=c.fetchall()
#   print(products)
    conn.close()
    return products

# Вызов функции initiate_db() для создания таблицы
initiate_db()
#get_all_products()
print(get_all_products())