from tkinter import *
import tkinter.messagebox
def doNothing():
    print ("I won't do anything")

root=Tk()

# Message Box
tkinter.messagebox.showinfo("Window Title", "A broken clock is correct two time a day.")
answer=tkinter.messagebox.askquestion("Do You like Silly Clock?")

if answer == 'yes':
    print(" Bo---=D=")


# Creating a Menu Bar
menu=Menu(root)
root.config(menu=menu)

subMenu=Menu(menu)
menu.add_cascade(label="File" , menu=subMenu)
subMenu.add_command(label="New Project", command=doNothing,background="blue")
subMenu.add_command(label="New File", command=doNothing, background="purple")
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.quit, background="red")

editMenu=Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Edit Project", command=doNothing)


# Creating  the Toolbar

toolbar=Frame(root, bg="purple")

insertButton=Button(toolbar, text="Insert Nothing", command=doNothing)
insertButton.pack(side=LEFT,padx=2 , pady=2)
printButton=Button(toolbar, text="Print", command=doNothing)
printButton.pack(side=LEFT,padx=2 , pady=2  )

toolbar.pack(side=TOP,fill=X)


# Creating the Status Bar
status=Label(root, text="Status Bar", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM,fill=X)

root.mainloop() 
