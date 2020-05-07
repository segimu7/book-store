import sqlite3

def connect():  # funcion setup de la coneccion de la base de datos
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(Id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbbn): #funcion para insertar valores
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbbn))
    conn.commit()
    conn.close()
    
def view():                            #funcion para ver los valores ingresados
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbbn=""): #funcion de busqueda
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbbn=?",(title,author,year,isbbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):                                #funcion para borrar datos
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?",(id,))
    conn.commit()
    conn.close()
    
def update(id,title,author,year,isbbn):       #funcion para hacer el update de los valores
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbbn=? WHERE id=?",(title,author,year,isbbn,id))
    conn.commit()
    conn.close()
    
connect()

