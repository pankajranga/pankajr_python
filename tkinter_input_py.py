from tkinter  import *
import sqlite3

def create_conn(dbf):
    conn = None
    try:
        conn = sqlite3.connect(dbf)
    except Error as e:
        print(e)
    return conn
    
def create_table(conn, tname):

    cur = conn.cursor()
    sqlstrng = "create table "+ tname + "(id integer)"
    cur.execute(sqlstrng)

def start(tname):
    dbfile = r"C:\sqllite\sqlite-tools-win32-x86-3380300\testdb.db"

    # Create DB connection
    conn = create_conn(dbfile)
    create_table(conn,tname)    
    
ws = Tk()
ws.title('get text demo')
ws.geometry('210x210')

def startTabCreation():
    tname = name_Tf.get()
    start(tname)

Label(ws, text="Enter Name").pack()
name_Tf = Entry(ws)
name_Tf.pack()

Button(ws, text="Create Table", command=startTabCreation).pack()

ws.mainloop()