import sqlite3
"""def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title text ,author text,year INTEGER, isbn INTEGER )")
        self.conn.commit()
"""
def connect():
    conn=sqlite3.connect("lms.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE if NOT exists book(id INTEGER PRIMARY KEY,title text,author text,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()

def issue():
    conn=sqlite3.connect("lms.db")
    cur=conn.cursor()
    #cur.execute("drop table issue")
    cur.execute("CREATE TABLE if NOT exists issue(id INTEGER NOT NULL ,title text,author text,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()

def request():
    conn=sqlite3.connect("lms.db")
    cur=conn.cursor()
    #cur.execute("drop table request")
    cur.execute("CREATE TABLE if NOT exists request(id PRIMARY KEY,title text,author text,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()

"""def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT into book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
"""
def insert(title,author,year,isbn):
    conn=sqlite3.connect("lms.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE if NOT exists book(id INTEGER PRIMARY KEY,title text,author text,year INTEGER,isbn INTEGER)")
    
    #conn=sqlite3.connect('booklib.db')
    #cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()
def request_insert(title,author,year,isbn):
    conn=sqlite3.connect('lms.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO request VALUES(NULL,?,?,?,?)',(title,author,year,isbn))
    conn.commit()
    conn.close()

def request_view(title="",author="",year="",isbn=""):
    conn=sqlite3.connect('lms.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM request")
    rows=cur.fetchall()
    conn.close()
    return rows

def request_delete(title):
    conn=sqlite3.connect('lms.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM request WHERE title=?",(title,) )
    conn.commit()
    conn.close()

def issue_delete(id):
    conn=sqlite3.connect('lms.db')
    cur = conn.cuarsor()
    cur.execute("DELETE FROM issue WHERE id=?",(id,) ) #(int(id[0]),) was giving error if only used (id,) as in front end i removed [0] from the next code line<variable_name>[0]
    conn.commit()
    conn.close()

def issue_insert(id):
    conn=sqlite3.connect('lms.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO issue SELECT * FROM book WHERE id=?',(id,))
    conn.commit()
    conn.close()

def issue_view(title="",author="",year="",isbn=""):
    conn=sqlite3.connect('lms.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM issue")
    rows=cur.fetchall()
    conn.close()
    return rows


def view():
    conn=sqlite3.connect('lms.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect('lms.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect('lms.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,) )
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect('lms.db')
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
issue()
request()