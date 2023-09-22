from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"   

        scvalue.set(value)
        screen.update()   

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("400x600")
root.title("Calculator")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="lucida 40 bold", bg="light grey")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

button_frame = Frame(root, bg="grey")

buttons = [
    '9', '8', '7',
    '6', '5', '4',
    '3', '2', '1',
    '0', '+', '-',
    '*', '/', '=', 
        'C'
]

row_val = 1
col_val = 0

for button_text in buttons:
    b = Button(button_frame, text=button_text, padx=25, pady=15, font="lucida 20 bold", bg="light blue")
    b.grid(row=row_val, column=col_val, padx=10, pady=10)
    b.bind("<Button-1>", click)
    
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

button_frame.pack()

root.mainloop()
