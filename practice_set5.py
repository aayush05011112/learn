# # f=open("poem.txt","w")
# # f.write("Hello, form the other side \n I must have called thousand time\n To say you I am sorry \n I can say atleast I tried \n hello form the other side.")
# # . Write a program to read the text from a given file ‘poems.txt'' and find out whether it contains the word ‘twinkle''.
# f=open("poem.txt","r")
# twinkle=f.read()
# if "twinkle" in twinkle:
#     print("Word is present in file.")
# else:
#     print("Word is not present.")



# '''The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file 'Hi-score.txt' which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi-
# score whenever the game() function breaks the Hi-score'''
# import random
# print("You are playing a game:")
# score=random.randint(1,69)
# print("Your score =",score)
# with open ("highscore.txt","r") as f:
#     hiscore=f.read()
# print(hiscore)
# if hiscore=="":
#     hiscore=0
# else:
#     hiscore=int(hiscore)
# if hiscore < score:
#     with open("highscore.txt","w") as f:
#         f.write(str(score))



    

# '''Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13  year old.'''
# def gentable(n):
#     table=''
#     for i in range(1,101):
#         table+=f'{n}*{i}={n*i}\n'
#     with open (f'tables/table_of_{n}.txt',"w") as f:
#         f.write(table)
# for i in range (1,22):
#     gentable(i)




# #A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.
# word="donkey"
# with open ("file.txt","r") as f:
#     contend=f.read()
# newcontend=contend.lower()
# newcontend=newcontend.replace("donkey","####")
# with open ("file.txt","w") as f:
#     f.write(newcontend)



# # Repeat program 4 for a list of such words to be censored
# words=["which","type","when"]
# with open ("file.txt","r") as f:
#     contend=f.read()
# for word in words:
#     contend=contend.replace(word,"*"*len(word))
# with open ("file.txt","w") as f:
#     f.write(contend)


# # Write a program to mine a log file and find out whether it contains ‘python’.
# with open ("bits.txt","r") as f:
#     context=f.read()
# if "python" in context.lower():
#     print("Python is present in the text.")
# else:
#     print("Python is not present in the file.")


# # Write a program to mine a log file and find out whether it contains ‘python’ and in which line.
# linenum=1  
# with open("bits.txt","r")as f:
#     lines=f.readlines()
# for line in lines:
#     if "python" in line:
#         print(f"python in line no.{linenum}")
#         break
#     linenum+=1
# else:
#     print("Python is not present.")




# # Write a program to make a copy of a text file “this. txt”
# with open ("this.txt","r") as f:
#     context=f.read()
# with open("this_copy.txt","w") as f:
#     f.write(context)




# # Write a program to find out whether a file is identical & matches the content of another file
# file1=input("Enter first file name.")
# file2=input("Enter second file name.")
# with open(file1,"r") as f:
#     context=f.read()
# with open(file2,"r") as f:
#     context1=f.read()
# if context1==context:
#     print("Both file are identical.")
# else:
#     print("Files are not identical.")




# # Write a program to wipe out the content of a file using python
# with open ("this.txt","w") as f:
#     f.write("")



# # Write a python program to rename a file to “renamed_by_ python.txt
# import os
# with open("this_copy.txt","r") as f:
#     context=f.read()
# print(context)
# with open ("rename_by_python.txt","w") as f:
#     f.write(context)
# os.remove("this_copy.txt")



