# # f=open("sample.txt","r")
# # print(f.read())
# # f.close() 

# # open("sample.txt","w").write("I am writingthis to the file")
# # f=open("sample.txt","r")

# f=open("sample.txt","r")
# print(f.readline())#print first line
# print(f.readline())#print second line
# f.close()


# with open("sample.txt","r")as f:
#     print(f.read())

# import os
# os.remove("sample.txt")


# #program to replace text reading in file.
# with open("practice.txt","r") as f:
#     data=f.read()
# print(data)
# x=data.replace("computer","mobile")
# print(x)
# with open("practice.txt","w") as f:
#     f.write(x)


#program to find text in file.

# def check_for_word():
#     word="work"
#     with open("practice.txt","r") as f:
#         data=f.read()
#         if word in data:
#             print(word,"is present")
#         else:
#              print(word,"is not present in file")
# check_for_word()

# def check_for_line():
#     word="name"
#     count=1
#     data="hello"
#     with open("practice.txt","r")as f:
#         while data:
#             data=f.readline()
#             if word in data:
#                 print(count)
#             count+=1
# check_for_line()

# num=""
# count=0
# with open("practice.txt","r")as f:
#     data=f.read()
#     print(data)
#     for i in range(len(data)):
#         if(data[i]==","):
#             num=int(num)
#             if(num%2==0):
#                 count+=1
#             num=""
#         else:
#             num+=data[i]
# print(count,"number of even data present")

# #another way

# count=0
# with open("practice.txt","r") as f:
#     data=f.read()
#     num=data.split(",")
#     print(num)
# for i in num:
#     if(int(i)%2==0):
#         count+=1
# print(count)

