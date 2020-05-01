import sqlite3
from tkinter import *
from admin import admin
from student import student

def connect(): #establishing connection
    conn=sqlite3.connect("lms.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE if NOT exists user(rollno INTEGER PRIMARY KEY,name text,password text)")
    conn.commit()
    conn.close()

def insert(rollno,name,password):
    conn=sqlite3.connect('lms.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO user VALUES(?,?,?)',(rollno,name,password))
    conn.commit()
    conn.close()

def check(name,password):#checking for valid credentails and  allowing admin to proceed further 
    conn=sqlite3.connect('lms.db')
    cur = conn.cursor()
    if   (cur.execute('SELECT * FROM admin WHERE name =? AND password = ?',(name,password))):
        if cur.fetchone():
            window = Tk()
            window.title('Admin')
            window.geometry('700x450')
            obj=admin(window)
            window.mainloop()
        else:
            messagebox.showinfo('error','Invalid details for admin login')

def checks(name,password):# for student login
    conn=sqlite3.connect('lms.db')
    cur = conn.cursor()
    if   (cur.execute('SELECT * FROM user WHERE name = ? AND password = ?', (name, password))):
        if cur.fetchone():
            window = Tk()
            window.title('Student')
            window.geometry('700x400')
            obj = student(window)
            window.mainloop()
        else:
            messagebox.showinfo('error','Invalid details for student login')


    conn.commit()
    conn.close()

connect()