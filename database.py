import sqlite3

CREATE_BEANS_TABLE= "CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT,rating INTEGER);"
INSERT_BEAN = "INSERT INTO beans (name,method,rating) VALUES (?,?,?);"
GET_ALL_BEANS="SELECT * from beans;"
GET_BEANS_BY_NAME="SELECT * from  beans where name=?;"
GET_BEST_PREPARATION_FOR_BEAN = """
SELECT * FROM beans
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;
"""
connection = sqlite3.connect("data.db")

def connect():
    return sqlite3.connect("data.db")


def create_tables(connection):
    with connection:
        connection.execute(CREATE_BEANS_TABLE)


def add_bean(connecton, name,method,rating):
    with connection:
        connecton.execute(INSERT_BEAN, (name,method,rating))
def get_all_beans(connection):
    with connection:
        return connection.execute(GET_ALL_BEANS).fetchall()
def get_beans_name(connection,name):
    with connection:
        return connection.execute(GET_BEANS_BY_NAME,(name,)).fetchall()
def get_best_preparation(connection,name):
    with connection:
        return connection.execute(GET_BEST_PREPARATION_FOR_BEAN,(name,)).fetchone()
import sqlite3


def connect():
    conn = sqlite3.connect("coffee_beans.db")
    return conn


def create_tables(conn):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, method TEXT, rating INTEGER)")
    conn.commit()


def add_bean(conn, name, method, rating):
    c = conn.cursor()
    c.execute("INSERT INTO beans (name, method, rating) VALUES (?, ?, ?)", (name, method, rating))
    conn.commit()


def get_all_beans(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM beans")
    beans = c.fetchall()
    return beans


def get_beans_by_name(conn, name):
    c = conn.cursor()
    c.execute("SELECT * FROM beans WHERE name LIKE ?", ('%' + name + '%',))
    beans = c.fetchall()
    return beans


def get_best_preparation(conn, name):
    c = conn.cursor()
    c.execute("SELECT * FROM beans WHERE name LIKE ? ORDER BY rating DESC LIMIT 1", ('%' + name + '%',))
    best_method = c.fetchone()
    return best_method


def delete_bean(conn, bean_id):
    c = conn.cursor()
    c.execute("DELETE FROM beans WHERE id = ?", (bean_id,))
    conn.commit()


def update_bean(conn, bean_id, name, method, rating):
    c = conn.cursor()
    c.execute("UPDATE beans SET name = ?, method = ?, rating = ? WHERE id = ?", (name, method, rating, bean_id))
    conn.commit()

