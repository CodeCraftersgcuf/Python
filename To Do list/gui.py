from tkinter import *

def login():
  """
  This function logs in the user.
  """

  username = username_entry.get()
  password = password_entry.get()

  if authentication.login(username, password):
    main_menu()
  else:
    print("Invalid username or password.")

def main_menu():
  """
  This function displays the main menu.
  """

  root.destroy()
  import main

def register():
  """
  This function registers a new user.
  """

  username = username_entry.get()
  password = password_entry.get()

  registration.register(username, password)

  print("Successfully registered.")

root = Tk()

username_label = Label(root, text="Username:")
username_entry = Entry(root)
password_label = Label(root, text="Password:")
password_entry = Entry(root, show="*")
login_button = Button(root, text="Login", command=login)
register_button = Button(root, text="Register", command=register)

username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_button.pack()
register_button.pack()

root.mainloop()