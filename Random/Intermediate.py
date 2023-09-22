
################################################################
#############################List###############################

#mylist = [ "banana", "cheese", "apple"]
#print(mylist)

#for i in mylist:
#    print(i)
#if "banana" in mylist:
#    print("yes")
#else:
#    print("no")

#print(len(mylist))
#mylist.append("lemeone")
#print(mylist)

#mylist.insert(0,"blueberry")
#print(mylist)

#item =mylist.pop()
#print(item)
#print(mylist)

#item=mylist.remove("cheese")
#print(mylist)

#item=mylist.sort()
#print(mylist)

#mylist=[1]*9
#print(mylist)

#mylist2=[1,2,3,4,5,6,7,8]
#new_list=mylist +mylist2
#print(new_list)

#mylist=[1,2,3,4,5,6,7,8]
#a=mylist[1:5]
#a=mylist[::-1]
#print(a)



################################################################
#########################Tuples#################################

#mytuples =("Max",23,"Min")
#print(mytuples)

#import timeit
#print(timeit.timeit(stmt="[0,1,2,3,4,5,6,7,8]",number=10000000))
#print(timeit.timeit(stmt="[0,1, 2, 3, 4]",number=10000000))


#############################Dictionary###########################

#mydict ={"name":"test","age":"12","city":"New York"}
#print(mydict)

#value = mydict["age"]
#print(value)

#################################Sets################################

#myset = set("Hello, world!")
#print(myset)

#############################Functions##############################


#def hello():
#    print("Hello, world!")

#hello()

#def add_10(x):
#    return x+10

#add_10(100)

#g=lambda x:x*x*x
#print(g(10))

#l1=[27,88,23,45,44,26,64]
#final_l1=list(filter(lambda x:(x%2!=0),l1))
#print(final_l1)


###################################Class##################################

##########################################################################

#class Phone:
#    def sert_color(self,color):
#        self.color=color
#    def set_cost(self,cost):
#        self.cost=cost
#    def show_color(self):
#        return self.color
#    def show_cost(self):
#        return self.cost
#    def make_call(self):
#        print("Calling...")
#    def play_game(self):
#        print("Playing...")

#p1 = Phone()
#p1.sert_color("black")
#p1.set_cost(5900)
#p1.show_color()
#p1.show_cost()
#p1.make_call()





#class Employee:
#    def __init__(self,name,age,salary,gender):
#        self.name = name
#        self.age = age
#        self.salary = salary 
#        self.gender = gender

#    def show_employee_detail(self):
#        print ("Employee",self.name)
#        print ("Employee Age", self.age)
#        print ("EmployeeSalary", self.salary)
#        print ("EmployeeGender", self.gender)

#e1=Employee('Alice',32,50000,'Male')
#e1.show_employee_detail()

###########################Inheritance###################################

#########################################################################

#class Vehicle:
#    def __init__(self,milage,cost):
#        self.milage = milage
#        self.cost = cost

#   def show_vehicle_details(self):
#        print ("Vehicle Milage",self.milage)
#        print ("Vehicle Cost",self.cost)
#        print ("I am a Vehicle")

#v1=Vehicle(200,200)
#v1.show_vehicle_details()

#class Car(Vehicle):
#    def show_car_details(self):
#        print ("I am a Car")

#c1=Car(233,100)
#c1.show_vehicle_details()
#c1.show_car_details()

#############################Numpy#############################
#import numpy as np
#l1=[1,2,3,4,5]
#n1=np.array(l1)
#print(n1)
#print(type(n1))
#n3=np.zeros((2,3))
#print(n3)

#n4=np.full((2,3),69)
#print(n4)

#n5=np.arange(10,20)
#print(n5)

#n6=np.random.randint(0,100,10)
#print(n6)

############################Pandas#####################################
import pandas as pd
s1=pd.Series([1,2,3,4,5])
print(s1)







