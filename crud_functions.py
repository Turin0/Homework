import sqlite3

connect = sqlite3.connect('database.db')
cursor = connect.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')


cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Products (title)')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
balance INTEGER NOT NULL
)
''')


# cursor.execute('INSERT INTO Products(title, description, price) VALUES(?,?,?)',
#                ('Витамин A', 'Является одним из важнейших витаминов в нашем организме.', '100'))
# cursor.execute('INSERT INTO Products (title, description, price) VALUES(?,?,?)',
#                ('Витамин В6', 'Участвует во многих биохимических реакциях, необходимых для поддержания жизни.', '200'))
# cursor.execute('INSERT INTO Products (title, description, price) VALUES(?,?,?)',
#                ('Витамин C', 'Это незаменимое питательное вещество, имеющее огромное значение для работы иммунной системы.', '300'))
# cursor.execute('INSERT INTO Products (title, description, price) VALUES(?,?,?)',
#                ('Витамин D3', 'Необходим для правильной работы иммунной, нервной, гармональной и кровеносной систем человека, он участвует в метаболизме кальция и фосфора.', '400'))
# cursor.execute('DELETE FROM Users WHERE id = ?', ('2',))


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    return products


def add_users(username, email, age):
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?,?,?,?)',
                   (username, email, age, '1000'))
    connect.commit()


def is_included(username):
    check_users = cursor.execute('SELECT * FROM Users WHERE username=?', (username,)).fetchone()
    if check_users is None:
        check_users = False
    else:
        check_users = True
    return check_users


connect.commit()

if __name__ == '__main__':
    initiate_db()
