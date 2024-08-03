# # 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up! 

# words={
#     "Shau":"Apple",
#     "Kela":"Banana",
#     "Aap":"Mango"
# }
# print("Welcome to dictionary")
# word=input("Enter the word you want meaning of:")
# if word in words:
#     print(words[word])
# else:
#     print("Words not avaliable in dictnory")


# # 2. Write a program to input eight numbers from the user and display all the unique numbers (once). 
# num=set()
# for i in range(8):
#     el=int(input("Enter the number:",i+1))
#     num.add(el)
# print(num)


# # 3. Can we have a set with 18 (int) and '18' (str) as a value in it? 
# num=set()
# num.add(18)
# num.add("18")
# num.add(18.0000)
# print(num)
# len(num)
# #Yes we can have 18(int) and '18'(str) as value in set


# # 4. What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations? 
# print(len(s))
# # Ans will be 2


# # 5. s = {} 
# # What is the type of 's'? 
# # Ans will be dict


# # 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. 
# friends={}
# for i in range(4):
#     name=input("Enter the name of the friend:")
#     lang=input("Enter the language of the friend:")
#     friends[name]=lang  
# print(friends)


## 7. If the names of 2 friends are same; what will happen to the program in problem 6? 
##Ans will be the second language value will replace the language of first friend in the dictionary


## 8. If languages of two friends are same; what will happen to the program in problem 6? 
## Nothing will change the dictionary remains normal with the two same language of two different friends.


# # 9. Can you change the values inside a list which is contained in set S? 
# # s = {8, 7, 12, "Harry", [1,2]} 
## No we cannot change the value inside a list which is contaied in set s because list is no hashable(changable) so this set cant be created.
## we can change if tupel is given insted of list.
# # s = {8, 7, 12, "Harry", (1,2)} 
# # s.add(19)
# # print(s)