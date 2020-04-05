import random
import string

#list all possible characters
letters = string.ascii_letters
special_chars = string.punctuation
digits = string.digits
chars = letters + special_chars + digits

#randomizing the password length (final will have 8-16)
length = random.randint(4,13)

#creating a random password
password = ""
for i in range(length):  
    password += random.choice(chars)


#adding minimum requirements (Add of each character type)
a = random.choice(string.ascii_letters.lower())
b = random.choice(string.ascii_letters.upper())
c = random.choice(string.digits)
d = random.choice(string.punctuation)

password = password + a + b + c + d

#randomization of the entire password
final = random.sample(password, length+4)

final_password = ""
for i in final:
    final_password += i
    
print(final_password)