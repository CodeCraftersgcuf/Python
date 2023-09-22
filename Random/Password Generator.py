import random 

characters ="abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQ1234567890!@#$%^&*_+"

pass_length=int(input("Enter the length of Password: "))
pass_count=int(input("Enter the amount of password: "))

for i in range(0, pass_length):
    password = ""
    for j in range(0, pass_count):
        pass_char=random.choice(characters)
        password = password+pass_char
    print("The Generated Password is: " ,password)
        
