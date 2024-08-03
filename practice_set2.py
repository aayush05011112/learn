# #1. Write a program to find the greatest of four numbers entered by the user. 
# nums=[]
# for i in range(4):
#     num=int(input("Enter the number:"))
#     nums.append(num)
# if nums[0]>nums[1] and nums[0]>nums[2] and nums[0]>nums[3]:
#     print(nums[0],"Is the greatest")
# elif nums[1]>nums[2] and nums[1]>nums[3]:
#     print(nums[1],"Is the greatest")
# elif nums[2]>nums[3]:
#      print(nums[2],"Is the greatest")
# else:
#     print(nums[3],"Is the greatest")


# #2. Write a program to find out whether a student has passed or failed if it requires a 
# # total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
# mark1=float(input("Enter the mark of the Math:"))
# mark2=float(input("Enter the mark of the Science:"))
# mark3=float(input("Enter the mark of the English:"))
# total=mark1+mark2+mark3
# p1=mark1
# p2=mark2
# p3=mark3
# totalper=((total)/300)*100
# if totalper>=40 and p1>=33 and p2>=33 and p3>=33:
#     print("The student has passed with total percent of ",totalper,"%")
# else:
#     print("The student has failed with total percent of ",totalper,"%")



# # 3.A spam comment is defined as a text containing following keywords: 
# # "Make a lot of money"and, "buy now"and, "subscribe this"and, "click this"and. Write a program to detect these spams.
# p1="make a lot of money"
# p2="buy now"
# p3="subscribe this"
# p4="click this"
# comment=input("Enter your comment:")
# if p1 in comment or p2 in comment or p3 in comment or p4 in comment:
#     print("This is a spam comment")
# else:
#     print("This is not a spam comment")

#                OR

# spam=["Make a lot of money", "buy now", "subscribe this", "click this"]
# count=0
# com=input("Enter your comment:")
# for i in range(len(spam)):
#      if spam[i].lower() in com.lower():
#          count+=1
# if count>0:
#      print("This is spam comment")
# else:
#     print("Not spam")





# # 4. Write a program to find whether a given username contains less than 10 characters or not. 
# username=input("Enter username:")
# if len(username)<10:
#     print("Username contain less than 10 character")
# else:
#     print("Username contain more than 10 character")





# # 5. Write a program which finds out whether a given name is present in a list or not. 
# list=["Aayush","Alish","Ram","Shyam"]
# name=input("Enter your name:")
# if name in list:
#     print("Your name is present in the list")
# else:
#     print("Your name is not present in the list")




# # 6. Write a program to calculate the grade of a student from his marks from the  following scheme: 
# # 90 – 100 => Ex 
# # 80 – 90 => A 
# # 70 – 80 => B 
# # 60 – 70  =>C 
# # 50 – 60 => D 
# # <50        => F 

# mark=float(input("Enter your mark:"))
# if mark>=90:
#     print("Your grade is Ex")
# elif mark>=80 and mark<90:
#     print("Your grade is A")
# elif mark>=70 and mark<80:
#     print("Your grade is B")
# elif mark>=60 and mark<70:
#     print("Your grade is C")
# elif mark>=50 and mark<60:
#     print("Your grade is D")
# else:
#     print("Your grade is F")




# # 7. Write a program to find out whether a given post is talking about "Harry"and or not.
# post=input("Enter the article:")
# if "Harry".lower() in post.lower():
#     print("The article is talking about Harry")
# else:
#     print("The article is not talking about Harry")

