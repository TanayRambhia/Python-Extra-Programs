import tkinter as tk
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('login.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table named "users" with id(auto increment), username and password columns
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT
                )''')
conn.commit()

# Define a function to check if the user exists in the database
def check_user(username, password):
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    if cursor.fetchone() is not None:
        return True
    else:
        return False

# Define a function to handle the login button click event
def login():
    username = username_entry.get()
    password = password_entry.get()
    if check_user(username, password):
        login_status_label.config(text="Login successful!", fg="green")
    else:
        login_status_label.config(text="Invalid username or password", fg="red")

# Create a Tkinter window
window = tk.Tk()
window.title("Login Form")

# Create a label for the username field
username_label = tk.Label(window, text="Username:")
username_label.grid(row=0, column=0)

# Create a text field for the username
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1)

# Create a label for the password field
password_label = tk.Label(window, text="Password:")
password_label.grid(row=1, column=0)

# Create a text field for the password
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1)

# Create a login button
login_button = tk.Button(window, text="Login", command=login)
login_button.grid(row=2, column=1)

# Create a label for the login status
login_status_label = tk.Label(window, text="")
login_status_label.grid(row=3, column=1)

# Set the focus on the username field
username_entry.focus()

# Start the Tkinter event loop
window.mainloop()
