# #Write a program using functions to find greatest of three numbers
# def check(a,b,c):
#     if(a>b and a>c):
#         print(a,"is the gretest")
#     elif(b>c):
#         print(b,"Is the gretest")
#     else:
#         print(c,"is the gretest")
# n1=int(input("Enter first number:"))
# n2=int(input("Enter second number:"))
# n3=int(input("Enter third number:"))
# check(n1,n2,n3)




# # Write a python program using function to convert Celsius to Fahrenheit.
# def ctof(c):
#     print(c,"celsius=",(1.8*c)+32,"Fahrenheit")
# cel=int(input("Enter the degree in celsius:"))
# ctof(cel)



#How do you prevent a python print() function to print a new line at the end
#By writing syntax print("Text to print",end="")end function prevent from printing new line.




# #Write a recursive function to calculate the sum of first n natural numbers
# def tsum(n):
#      if n==1:
#         return 1
#      else:
#          return n+tsum(n-1)
# n=int(input("Enter the last number:"))
# total=tsum(n)
# print(total)
            



# '''Write a python function to print first n lines of the following pattern: 
# *** 
# **               - for n = 3 
# * '''
# def pattern(n):
#     i=n
#     while(i>=1):
#         print("*"*(i))
#         i-=1
# #          OR
# #def pattern(n):
# # for i in range(n):
# #     print(("*")*(n-i))

# n=int(input("Enter the value of n:"))
# pattern(n)




# # Write a python function which converts inches to cms
# def convert(inch):
#     print(inch,"inch=",inch*2.54,"cm")
# inch=int(input("Enter inches:"))
# convert(inch)



# Write a python function to remove a given word from a list ad strip it at the same time. 





# # Write a python function to print multiplication table of a given number.
# def mult(n):
#     for i in range(1,11):
#         print(n,"*",i,"=",n*i)
# n=int(input("Enter the number to find table of:"))
# mult(n)