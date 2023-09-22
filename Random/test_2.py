#numcomplex= 2+3j
#num= complex(2,3)

#print(num.real,num.imag)#

# from enum import Enum

# class State(Enum):
#     INACTIVE=0
#     ACTIVE=1
#     double_inactive=0.1
#     double_active=2
# print(list(State)) 
# print(State.ACTIVE.value)
# print (len(State))  

# print("What is Your Age?")
# age = input()
# print("Your Age is :" +age)

# condition=False
# if  condition==True:
#     print("The Condition")
#     print("was True")
# else:
#     print("The Condition")
#     print("was False")

# dogs =["Roger",1,"Syd",True,"Yolo",7]

# dogs[2]="Beau"
# dogs.append("Juddah")
# dogs.extend(["double",5])
# dogs.remove("Juddah")
# print("Beau" in dogs)
# print("Roger" in dogs)
# print(dogs[1])
# print(dogs)
# print(dogs[2:4])
# print(len(dogs))
# cats=["catie","Abc","dcx"]
# catscopy=cats[:]
# cats.sort(key=str.lower)
# print(cats)
# print(catscopy)


# Tuples
# names=("Rogers","Syd")
# names[0]
# print(names.index("Rogers"))

#Dictionaries

# dog = {"name": "Roger","age":8, "color":"green"}
# dog["name"]="Syd"
# print(dog['name'])
# print(dog.get("color","brown"))
# print(dog)
# print("color" in dog)
# print(list(dog.keys()))
# print(len(dog))

# Sets

# set1={"Roger","Syd"}
# set2={"Roger"}

# intersect=set1 & set2
# print(intersect)
# mod=set1|set2
# #>  <  -
# print(mod)

#Functions

def hello(name):
    print("Hello "+ name + " !")

hello("Beau")
hello("Beau_2")
