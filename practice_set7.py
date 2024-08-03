# # 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector. 
# class TwoDVector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
#     def show(self):
#         print(f"Vector is {self.i}i + {self.j}j")
# class ThreeDVector(TwoDVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
#     def show(self):
#         print(f"Vector is {self.i}i + {self.j}j + {self.k}k")
# a=TwoDVector(5,6)
# b=ThreeDVector(8,9,3)
# a.show()
# b.show()





# # 2. Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'. Add a method 'bark' to class 'Dog'. 
# class Animal:
#     pass
# class Pets(Animal):
#     pass
# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print("It Barks")




# '''3. Create a class 'Employee' and add salary and increment properties to it. 
# Write a method 'salaryAfterIncrement' method with a @property decorator with a setter 
# which changes the value of increment based on the salary. '''
# class Employee:
#     salary=10000
#     increment=20
#     @property
#     def salaryAfterIncrement(self):
#         return self.salary+(self.salary*self.increment/100)
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,salary):
#         self.incper= ((salary-self.salary)/self.salary)*100
# e=Employee()
# print(e.salaryAfterIncrement)
# e.salaryAfterIncrement=12000
# print(e.incper)










# # 4. Write a class 'Complex' to represent complex numbers, along with overloaded operators '+' and '*' which adds and multiplies them.
# class Complex:
#     def __init__(self,r,i):
#         self.r=r
#         self.i=i
#     def __add__(self,c2):
#         return Complex(self.r+c2.r, self.i+c2.i)
#     def __str__(self):
#         return f"{self.r} + {self.i}i"
#     def __mul__(self, c2):
#         real = self.r * c2.r - self.i * c2.i
#         imag = self.r * c2.i + self.i * c2.r
#         return Complex(real, imag)
# c1=Complex(1,3)
# c2=Complex(6,7)
# print(c1+c2)
# print(c1*c2)
        




'''5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which 
calculates the sum and the dot(.)product of them. '''
class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __add__(self,other):
        return vector(self.i+other.i,self.j+other.j)
    def __str__(self):
        return f"{self.i}i + {self.j}j"
v1=vector(5,4)
v2=vector(6,4)
print(v1+v2)

# 6. Write __str__() method to print the vector as follows:  7i + 8j +10k  Assume vector of dimension 3 for this problem. 
# 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.