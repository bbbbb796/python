import sqlite3
import random

db = sqlite3.connect('db.db')
sql = db.cursor()

db.commit()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    Login TEXT,
    Password TEXT,
    cash BIGINT
)""")


def reg():
    user_Login = input('Login: ')
    user_Password = input('Password: ')

    sql.execute(f"SELECT Login FROM users WHERE Login = '{user_Login}' ")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?,?,?)", (user_Login,user_Password,0))
        db.commit()

        print('Зарегестрировано!')
    else:
        print('Такая запись уже имеется')
    
    for value in sql.execute("SELECT * FROM users"):
        print(value)
    

def delete_db():
    sql.execute(f"DELETE FROM users WHERE Login = '{user_Login}' ")
    db.commit()
    print('Запись удалена!')


def casino():
    global user_Login
    user_Login = input('Log in: ')
    num = random.randint(1,2)

    for i in sql.execute(f'SELECT cash FROM users WHERE Login = "{user_Login}" '):
        balance = i[0]

    sql.execute(f"SELECT Login FROM users WHERE Login = '{user_Login}' ")
    if sql.fetchone() is None:
        print('такого логина не существует. зарегистрируйтесь')
        reg()
    else:
        if num == 1:
            sql.execute(f"UPDATE users SET cash = {1000 + balance} WHERE Login = '{user_Login}' ")
            print('вы выйграли')
            db.commit()
        else:
            print('вы проиграли')
            delete_db()

def enter():
    for i in sql.execute('SELECT Login,cash FROM users'):
        print(i)    

def main():
    casino()
    enter()

main()