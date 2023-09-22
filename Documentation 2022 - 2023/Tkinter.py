from tkinter import *
import tkinter
import time

# ASCII art for the first half of names
ascii_art1 = """



'  ..######..........######........##.....##.......########...
'  .##....##........##....##.......##.....##.......##.........
'  .##..............##.............##.....##.......##.........
'  .##...####.......##.............##.....##.......######.....
'  .##....##........##.............##.....##.......##.........
'  .##....##........##....##.......##.....##.......##.........
'  ..######..........######.........#######........##.........
    
                                                             
                                                                                
"""

# ASCII art for "Thank you"
thank_you_ascii = """   



'  .########....##.....##.......###.......##....##....##....##.....######.
'  ....##.......##.....##......##.##......###...##....##...##.....##....##
'  ....##.......##.....##.....##...##.....####..##....##..##......##......
'  ....##.......#########....##.....##....##.##.##....#####........######.
'  ....##.......##.....##....#########....##..####....##..##............##
'  ....##.......##.....##....##.....##....##...###....##...##.....##....##
'  ....##.......##.....##....##.....##....##....##....##....##.....######.



"""

names = [
    "222038 - Mohsin ALi", "222039 - Ayesha Shahid", "222040 - Nida Ashiq","222041 - Sawaira Jahangir", "222042 - Sana Aqeel","222043 - Muhammad Ahmad Shahid","222044 - Rubab Ashraf","222045 - Talha Maalik","222046 - Hassan Raza","222047 - Muhammad Junaid","222049 - Sahar Javed","222050 - Shqaib Ahmad","222051 - Noman Azhar","222052 - Saba Zaheer","222053 - Sumiyya Fatima", "222054 - Abu Herera","222055 - Areej Shahzadi","222056 - Aqib Noor","222057 - Muhammad Azeem","222058 - Muhammad Mathar","222059 - Saboor ", "222061 - Amna Zukhruf","222062 - Mishal Chaudhary","222063 - Wajeeha","222065 - Muntaha","222066 - Zain-Ul-Abidin","222067 - Muhammad Arslan","222068 - Minahil","222069 - Ahmad Mustafa","222070 - Malaika Iman","222071 - Shahid Shabbir","222072 - Majid Ali","222073 - Noman Fazal","222074 - Ayesha Khizar","222075 - Misbah Riaz","222076 - Suleman Zulfiqar","222077 - Zunair Imtiaz","222078 - Tasnim","222079 - Azeem Khalid","222080 - Abubakar Sajjad","222081 - Saad Waseem","222082 - Ahmad Ejaz","222083 - Jahanzaib Azhar","222084 -Ali Haider"
    ]

def type_name(name):
    time.sleep(1)
    name_label.config(text="")
    for char in name:
        name_label.config(text=name_label.cget("text") + char)
        root.update()
        time.sleep(0.07)
    name_label.config(text=name_label.cget("text") + "\n")  # Move to the next line
    root.after(800, clear_name)

def clear_name():
    name_label.config(text="")
    if not names:
        end_program()
    else:
        root.after(1000, update_name)

def update_name():
    global names
    if names:
        name = names.pop(0)
        type_name(name)

def blink_underscore():
    underscore_label.config(fg="black" if underscore_label.cget("fg") == "white" else "yellow")
    root.after(500, blink_underscore)

def end_program():
    # Remove the first ASCII art
    ascii_label.config(text="")
    
    # Create a frame for green dots


    thank_you_label = tkinter.Label(root, text=thank_you_ascii, fg="Purple", bg="black", font=("Courier", 12))
    thank_you_label.pack(pady=10)
    
    root.update()
    time.sleep(3)  # Pause for 3 seconds
    root.quit()  # Terminate the program

root = Tk()
root.title("Name Animation")
root.geometry("1920x1080")  # Larger size
root.configure(bg="black")

# Create a top frame to hold the "List of Names" label
top_frame = Frame(root, bg="black")
top_frame.pack(fill=BOTH)

# Create a label for ASCII art on the right with padding
ascii_label = tkinter.Label(root, text=ascii_art1, fg="Salmon", bg="black", font=("Courier", 12))
ascii_label.pack(side=tkinter.RIGHT, padx=20, pady=20)

# Create a label for displaying names on the left with padding
name_label = tkinter.Label(root, text="", fg="mint cream", bg="black", font=("Courier", 40))
name_label.pack(side=tkinter.LEFT, padx=60, pady=20)

# Create a label for blinking underscore
underscore_label = tkinter.Label(root, text="_", fg="green", bg="black", font=("Courier", 12))
underscore_label.pack(side=tkinter.LEFT, padx=15, pady=20)
blink_underscore()  # Start blinking underscore

# Start updating names
update_name()

# Create a label for "List of Names" at the top center
list_of_names_label = tkinter.Label(top_frame, text="List of Students From 2022-23:", fg="yellow", bg="black", font=("Courier", 40))
list_of_names_label.pack(pady=100)

# Start the main loop
root.mainloop()
