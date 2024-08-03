
# #Class and object

# class info:
#     name=input("Name of student")
#     number=int(input("Enter student phone number"))
#     address=input("Enter address of student")
#     skill=input("Enter the skil student have")

# #object

# i=info()
# print(i.name)
# print(i.number)


#init function in python

# class student:
#     # name=input("Enter name of the student:")
#     def __init__ (self,fullname):
#         self.name=fullname
#         print("Adding name of student in database....")

# s1=student("Aayush")
# print(s1.name)
# s2=student("Alish")
# print(s2.name)

# class student:
#     def __init__ (self, name,mark):
#         self.name=name
#         self.mark=mark
# s1=student("Aayush",78)
# print(s1.name)
# print(s1.mark)


# class student:

#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark

#     def hello(self):
#         print("Hello",self.name)

#     def gets_mark(self):
#         return self.mark
    
# s1=student("Aayush", 87)
# s1.hello()
# print(s1.gets_mark())



# #program to write a name of student and store mark of three sub:

# class student:
#     def __init__ (self,name,marks):
#         self.name=name
#         self.mark=marks
#     def avg(self):
#         sum=0
#         for i in self.mark:
#             sum+=i
#         sum=sum/3
#         return sum
# s1=student("Aayush",[87,98,56])
# print(s1.name)
# print(s1.mark)
# print("Avrage mark obtain is",s1.avg())

# class car:
#     def __init__ (self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.acc=True
#         self.brk=True
#         self.clutch=True
#         print("Starting....")
# car1=car()
# car1.start()

# #Banking system

# class account:
#     def __init__(self, account,balance):
#         self.account_no=account
#         self.balance=balance
#     def debit(self,amount):
#         self.balance-=amount
#         print("Rs.",amount,"was debited and you current balance is Rs.",self.balance)
#     def credit(self,amount):
#         self.balance+=amount
#         print("Rs.",amount,"was credited to you acc and you current balance is Rs.",self.balance)


# acc1=account(156374,10000)
# print(acc1.account_no)
# print(acc1.balance)

# num=int(input("Enter 1 for debit and 2 for credit:"))
# if(num==1):
#     acc1.debit(int(input("Enter the amount:")))
# elif(num==2):
#     acc1.credit(int(input("Enter the amount:")))
# else:
#     print("Invalid input")



#private object
# class email:
#     def __init__(self,id,password):
#         self.__password=password
#         self.id=id
#     def get_pass(self):
#         print(self.__password)

# acc1=email (489327429847,123432)
# print(acc1.id)
# #print(acc1.password)
# acc1.get_pass()      


# #properties
# class student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3)+"%"
# s1=student(89,98,89)
# print(s1.phy)
# s1.phy=98
# print(s1.percentage)

# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def shownum(self):
#         print(self.real,"i +",self.img,"j")

#     def __add__(self,num2):
#         newreal=self.real+num2.real
#         newimg=self.img+num2.img
#         return complex(newreal,newimg)
    
#     def __sub__(self,num2):
#         newreal=self.real-num2.real
#         newimg=self.img-num2.img
#         return complex(newreal,newimg)
# n1=complex(7,8)
# n1.shownum()
# n2=complex(9,2)
# n2.shownum()
# n3=n1+n2
# n3.shownum()
# n4=n1-n2
# n4.shownum()


# #prepare the class to find area and perimeter of the cricle
# pi=3.14
# class cricle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         area=pi*self.radius**2
#         return area
#     def parameter(self):
#         para=2*pi*self.radius
#         return para
# c1=cricle(5)
# print(c1.area())
# print(c1.parameter())

# #prepare a class name employes that has post salary and department attriburtes and also has show detail function.
# class employe:
#     def __init__(self,name,post,department):
#         self.name=name
#         self.post=post
#         self.department=department
#     def showdetail(self):
#         print("Name=",self.name)
#         print("Department=",self.department)
#         print("Post=",self.post)

# class engineer(employe):
#     def __init__(self, role,age):
#         self.role=role
#         self.age=age
#         super().__init__("ram","Developer","programming")
#         print("role=",self.role)
#         print("age=",self.age)

    

# e1=engineer("Developer",35)
# e1.showdetail()


# #order and price
# class order:
#     def __init__(self,item,price):
#         self.item=item
#         self.price=price
#     def __gt__(self,ord2):
#         return self.price>ord2.price
   
        
# ord1=order("Bread",75)
# ord2=order("Jam",75)
# print(ord1>ord2)

# n=int(input(""))
# if(n%2!=0):
#     print("Weird")
# else:
#     if n in range(2,5):
#         print("Not Weird")
#     elif n in range(6,20):
#         print("Weird")
#     elif n>20:
#         print("Not Weird")