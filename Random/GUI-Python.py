from  tkinter import *
#root=Tk()

#root.geometry("655x655")
#Ali_root=Tk()

#GUI Logic
#Ali_root.geometry("644x344")
#width,height
#Ali_root.minsize(200,100)
#Ali_root.maxsize(900,1000)

#label
#Ahmad=Label(text="Ali is a  good programer")
#Ahmad.pack()

#Ali_root.mainloop()

#################Picture#################################

#Img_root=Tk()
#Img_root.geometry("888x888")
#photo=PhotoImage(file="1.png")
#Abu_label=Label(image=photo)
#Abu_label.pack()
#Img_root.mainloop()


#root.geometry("443x233")
#root.title("Note")
#Important Label Options
#text -add the text
#bd - background 
#fg- Foreground
#font - Sets the font
#padx - x padding
#pady - y padding
#relif - border styling

#title_label = Label(text="lorem ipms      ad",bg="red", fg="blue",padx=33,pady=34,font="bold")
#title_label.pack()



#Important Pack Option

#anchor=nw
# side= top, bottom, left, right
#fill
#padx
#pady

###########################Frame####################################
#title_label.pack(side=BOTTOM,  anchor="se",fill=X)

#root.geometry("655x333")
#f1=Frame(root,bg="red",borderwidth=10,relief=SUNKEN)
#f1.pack(side=LEFT,fill=Y)
#f2=Frame(root,bg="red",borderwidth=10,relief=SUNKEN)
#f2.pack(side=TOP,fill=X)

#l=Label(f1,text="Press")
#l.pack(pady=142)

#l=Label(f2,text="Welcome...")
#l.pack()



##############################Buttons##############################

#frame=Frame(root, borderwidth=6, bg="black")
#frame.pack(side=LEFT, anchor="nw")
#def  hello():
#    print ("Hello")
#b1=Button(frame, fg="black",text="Do Not Click", command=hello)
#b1.pack()


####################### Widget & Grid ###################################
#def getValue():
#    print(uservalue.get())
#    print(passvalue.get())
#user=Label(root, text="UserName")
#password=Label(root, text="Password")
#user.grid()
#password.grid(row=1)

#uservalue=StringVar()
#passvalue=StringVar()

#userentry=Entry(root, textvariable=uservalue)
#passentry=Entry(root, textvariable=passvalue)

#userentry.grid(row=0,column=1)
#passentry.grid(row=1, column=1)

#Button(text="Submit",command=getValue).grid()

############################CheckButtons#################################

#Label(root,text="Welcome to Tkinter").grid()
#name= Label(root,text="Name").grid()
#phone= Label(root,text="Phone").grid()
#gender= Label(root,text="Gender").grid()


#root.mainloop()

#########################################################################


window=Tk()
window.title ("Hello World")


window.mainloop()