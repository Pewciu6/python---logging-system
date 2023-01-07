import mysql.connector
import tkinter

połączenie = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "password",
    database = "system_logowania",

)
cursor = połączenie.cursor()

def tworzenie_konta():

    nazwa_użytkownika = username_entry.get()
    hasło = password_entry.get()
    query = "INSERT INTO user (username, password) values(%s, %s)"
    values = (nazwa_użytkownika, hasło)
    cursor.execute(query,values)
    print(f'Konto zostało utworzone')
    połączenie.commit()
    połączenie.close()
    cursor.close()

def logowanie():

    nazwa_użytkownika = username_entry.get()
    hasło = password_entry.get()

    cursor.execute('SELECT * FROM user WHERE username=%s and password=%s', (nazwa_użytkownika,hasło))
    
    if cursor.fetchone():

        print(f'Zalogowano jako {nazwa_użytkownika}')
        
    else:

        print('Logowanie nie udane')
    połączenie.close()
    cursor.close()

root = tkinter.Tk()
root.geometry('250x175')

nazwa_gui = tkinter.Label(root, text = 'System logowania do bazy danych')
nazwa_gui.place(x = 35, y = 10)

User = tkinter.Label(root, text='Username: ')
User.place(x=10, y=50)

Password = tkinter.Label(root, text="Password: ")
Password.place(x=10, y = 90)

username_entry = tkinter.Entry(root, width=20)
username_entry.place(x = 100, y = 50)

password_entry = tkinter.Entry(root, width= 20)
password_entry.place(x = 100, y = 90)

Zaloguj = tkinter.Button(root, text = 'Zaloguj się', width=13, command= logowanie)
Zaloguj.place(x = 15, y = 130)

Zarejestruj = tkinter.Button(root, text = "Zarejestruj się", width=13, command = tworzenie_konta)
Zarejestruj.place(x = 140, y = 130)

tkinter.mainloop()