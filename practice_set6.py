# # Create a class “Programmer” for storing information of few programmers working at Microsoft. 
# class programmer:
#     def __init__(self,name,id,sal):
#         self.name=name
#         self.id=id
#         self.salary=sal
#     def show(self):
#         print(f"Name={self.name}\nCompany={self.id}\nSalary={self.salary}")
# p1=programmer("Ram",183738,90000)
# p1.show()






# # Write a class “Calculator” capable of finding square, cube and square root of a number. 
# class calculator:
#     def __init__(self,n):
#         self.num=n
#     def square(self):
#         print(self.num**2)
#     def cube(self):
#         print(self.num**3)
#     def squareroot(self):
#         print(self.num**(1/2))
# n=int(input("Enter the number:"))
# n1=calculator(n)
# choice=input("Enter s to find square,c to find cube ,r to find root\n")
# if (choice=="c"):
#     n1.cube()
# elif(choice=="s"):
#     n1.square()
# else:
#     n1.squareroot()




# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
# from random import randint
# class Train:
#     def __init__(self,n):
#         self.trainno=n
#         print("Welcome to world railways:")
#     def fare(self,fro,to):
#         self.fro=fro
#         self.to=to
#         print(f"Ticket price of trainno:{self.trainno} from {self.fro} To {self.to} is {randint(100,10000)} ")
#     def book(self):
#         print(f"Ticket is in trainno:{self.trainno} booked from {self.fro} To {self.to}")
#     def getstatus(self):
#         c=randint(1,3)
#         if c==1:
#             print(f"Trainno:{self.trainno} from {self.fro} To {self.to} is running safely.")
#         else:
#             print(f"Trainno:{self.trainno} from {self.fro} To {self.to} has stopped due to some problem.")
# tn=input("Enter the train no of the train You want to book in:")
# c1=Train(tn)
# ser=input("If you want to book to ticket enter (Y): ")
# if ser=="Y":
#     loc=input("Enter your location:")
#     des=input("Enter your destination:")
#     c1.fare(loc,des)
#     fb=input("For booking enter (b):")
#     if fb=="b":
#         c1.book()
#         c1.getstatus()
#     else:
#         print("Thanks for your inquary.")
# else:
#     print("Thanks for your visits.")


    
    



