import random
import string
passlen=12
value=string.ascii_letters +string.punctuation +string.digits
print(value)
password=""
for i in range (12):
    password+=random.choice(value)
print("Suggested pass:",password)