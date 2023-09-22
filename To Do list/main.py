import tkinter as tk
import hashlib




# Function to open the registration frame
def open_registration():
    login_frame.pack_forget()
    registration_frame.pack()

# Function to open the login frame
def open_login():
    registration_frame.pack_forget()
    login_frame.pack()

# Function to handle registration
def handle_registration():
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()

    # Implement your registration logic here
    # You can use the new_username and new_password variables
    with open("users.txt", "a") as file:
        file.write(f"{new_username}:{hashlib.sha256(new_password.encode()).hexdigest()}\n")
    registration_message_label.config(text="Registration successful.", fg="green", font=("Helvetica", 12))
    new_username_entry.delete(0, tk.END)
    new_password_entry.delete(0, tk.END)

# Function to handle login
def handle_login():
    global current_user
    username = username_entry.get()
    password = password_entry.get()

    # Implement your login logic here
    # You can use the username and password variables
    with open("users.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and hashlib.sha256(password.encode()).hexdigest() == stored_password:
                login_message_label.config(text="Login successful.", fg="green", font=("Helvetica", 12))
                current_user = username  # Store the current user
                show_todo_menu()
                return
    login_message_label.config(text="Login failed. Please check your credentials.", fg="red", font=("Helvetica", 12))
    password_entry.delete(0, tk.END)

# Function to display the to-do menu
def show_todo_menu():
    login_frame.pack_forget()
    todo_frame.pack()
    load_todo_list()

# Function to load the to-do list for the current user
def load_todo_list():
    todo_listbox.delete(0, tk.END)  # Clear the list
    with open("todos.txt", "r") as file:
        for line in file:
            username, task = line.strip().split(":")
            if username == current_user:
                todo_listbox.insert(tk.END, task)

# Function to add a to-do item
def add_todo():
    todo_item = todo_entry.get()
    if todo_item:
        with open("todos.txt", "a") as file:
            file.write(f"{current_user}:{todo_item}\n")
        todo_entry.delete(0, tk.END)
        load_todo_list()

# Function to delete a selected to-do item
def delete_todo():
    selected_item_index = todo_listbox.curselection()
    if selected_item_index:
        index = selected_item_index[0]
        task = todo_listbox.get(index)
        with open("todos.txt", "r") as file:
            lines = file.readlines()
        with open("todos.txt", "w") as file:
            for line in lines:
                username, todo = line.strip().split(":")
                if username != current_user or todo != task:
                    file.write(line)
        load_todo_list()

# Create the main window
root = tk.Tk()
root.title("Welcome to my Program")
root.geometry("500x400")  # Set window size

# Create frames for registration, login, and to-do list
registration_frame = tk.Frame(root)
login_frame = tk.Frame(root)
todo_frame = tk.Frame(root)

# Create a label at the top
welcome_label = tk.Label(root, text="Welcome to my Program", font=("Helvetica", 20), fg="blue")
welcome_label.pack(pady=20)

# Create buttons to switch between registration and login
register_button = tk.Button(root, text="Register", command=open_registration, font=("Helvetica", 14))
login_button = tk.Button(root, text="Login", command=open_login, font=("Helvetica", 14))
register_button.pack()
login_button.pack()

# Create registration widgets
new_username_label = tk.Label(registration_frame, text="New Username:", font=("Helvetica", 14))
new_username_label.pack()
new_username_entry = tk.Entry(registration_frame, font=("Helvetica", 12))
new_username_entry.pack()

new_password_label = tk.Label(registration_frame, text="New Password:", font=("Helvetica", 14))
new_password_label.pack()
new_password_entry = tk.Entry(registration_frame, show="*", font=("Helvetica", 12))
new_password_entry.pack()

register_button = tk.Button(registration_frame, text="Register", command=handle_registration, font=("Helvetica", 14))
register_button.pack()

registration_message_label = tk.Label(registration_frame, text="", fg="green", font=("Helvetica", 12))
registration_message_label.pack()

# Create login widgets
username_label = tk.Label(login_frame, text="Username:", font=("Helvetica", 14))
username_label.pack()
username_entry = tk.Entry(login_frame, font=("Helvetica", 12))
username_entry.pack()

password_label = tk.Label(login_frame, text="Password:", font=("Helvetica", 14))
password_label.pack()
password_entry = tk.Entry(login_frame, show="*", font=("Helvetica", 12))
password_entry.pack()

login_button = tk.Button(login_frame, text="Login", command=handle_login, font=("Helvetica", 14))
login_button.pack()

login_message_label = tk.Label(login_frame, text="", font=("Helvetica", 12))
login_message_label.pack()

# Create to-do list widgets
todo_label = tk.Label(todo_frame, text="To-Do List", font=("Helvetica", 16))
todo_label.pack()

todo_entry = tk.Entry(todo_frame, font=("Helvetica", 12))
todo_entry.pack()

add_button = tk.Button(todo_frame, text="Add", command=add_todo, font=("Helvetica", 14))
add_button.pack()

delete_button = tk.Button(todo_frame, text="Delete", command=delete_todo, font=("Helvetica", 14))
delete_button.pack()

todo_listbox = tk.Listbox(todo_frame, font=("Helvetica", 12))
todo_listbox.pack()

# Initialize the current user
current_user = None

# Pack the registration frame initially
registration_frame.pack()

# Start the GUI main loop
root.mainloop()
