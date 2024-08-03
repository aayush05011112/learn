# # Write a program to print multiplication table of a given number using for loop.
# num=int(input("Enter the number you want to find multiplication table of:"))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)



# # Write a program to greet all the person names stored in a list ‘l’ and which starts  with S.  l = ["Harry", "Soham", "Sachin", "Rahul"]
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for name in l:
#     if name.startswith("S"):
#         print(f"Hello {name}")



# # Attempt problem 1 using while loop.
# num=int(input("Enter the number you want:"))
# i=1
# while i<=10:
#     print(num,"X",i,"=",i*num)
#     i+=1



# # Check if the given number is prime or not
# num=int(input("Enter the number:"))
# count=0
# if num==1 and num==2:
#     print(num,"is prime")
# for i in range (3,num):
#     if num%i==0:
#         count+=1
# if count==0:
#     print(num,"is a prime number")
# else:
#     print(num,"is not a prime number")



# # Write a program to find the sum of first n natural numbers using while loop
# num=int(input("Enter the last number till which you want sum of: "))
# sum=0
# for i in range(1,num+1):
#     sum+=i
# print(sum)



# # Write a program to calculate the factorial of a given number using for loop
# n=int(input("Enter the number you want factorial of:"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)



# '''
#  . Write a program to print the following star pattern. 
#    * 
#   *** 
#  *****  for n = 3
#  '''

# n=int(input("Enterthe value of n:"))
# for i in range(1,n+1):
#     print(" "*(n-i), end=" ")
#     print ("*"*(2*i-1))




# '''
# Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3
# '''

# n=int(input("Enter the value of n:"))
# for i in range(1,n+1):
#     print("*"*(i))




# '''
# Write a program to print the following star pattern. 
# * * * 
# *   *    for n = 3 
# * * * 
# '''
# n=int(input("Enter the value of n:"))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*(n),end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")





# #Write a program to print multiplication table of n using for loops in reversed order
# n=int(input("Enter the number you want to find the table of:"))
# i=10
# while(i>=1):
#     print(i,"X",n,"=",i*n)
#     i-=1