# import random
# comp=random.randint(1,4)
# # print(comp)
# # comp=1
# youstr=input(" s for scissor \n r for rock and \n p for papper:\n Enter:")
# mydict={
#     "s":1,
#     "r":2,
#     "p":3
# }
# revdict={
#     1:"Scissor",
#     2:"Rock",
#     3:"Paper"
# }
# you=mydict[youstr]
# if (comp==you):
#     print(f"Computer have chosen {revdict[comp]}\n Game has been draw")
    
# else:
#     if you==1 and comp==2:
#         print(f"Computer have chosen {revdict[comp]}\n You loose.")
#     elif you==1 and comp==3:
#         print(f"Computer have chosen {revdict[comp]}\n You win.")
#     elif you==2 and comp==3:
#         print(f"Computer have chosen {revdict[comp]}\n You loose.")
#     elif you==2 and comp==1:
#         print(f"Computer have chosen {revdict[comp]}\n You win.")
#     elif you==3 and comp==2:
#         print(f"Computer have chosen {revdict[comp]}\n You win.")
#     elif you==3 and comp==1:
#         print(f"Computer have chosen {revdict[comp]}\n You loose.")
#     else:
#         print("Error in game")
# print("------------Game Over------------")