import random
import string

def generate_password(length, level, output=[]):
    chars = string.ascii_letters
    if level > 1:
        chars = "{}{}".format(chars, string.digits)
    if level > 2:
        chars = "{}{}".format(chars, string.punctuation)
    
    for i in range(length):
        output.append(random.choice(chars))
    
    return "".join(output)

print(("-" * 30) + "\n Şifre Oluşturucu\n" + ("-" * 30))

password_length = int (input("Karakter uzunluğu: "))
password_level = int (input("Güvenilirlik: "))

password = generate_password(password_length, password_level)
print("\nYour password is: {}".format(password))

#2.

import random
import string

def generate_password(length, level, output=[]):
    chars = string.ascii_letters
    if level > 1:
        chars = "{}{}".format(chars, string.digits)
    if level > 2:
        chars = "{}{}".format(chars, string.punctuation)
    
    for i in range(length):
        output.append(random.choice(chars))
    
    return "".join(output)

print(("-" * 30) + "\n Şifre Oluşturucu\n" + ("-" * 30))

password_length = int (input("Karakter uzunluğu: "))
password_level = int (input("Güvenilirlik: "))

password = generate_password(password_length, password_level)
print("\nYour password is: {}".format(password))

#3.

import random
import string

def generate_password(length, level, output=[]):
    chars = string.ascii_letters
    if level > 1:
        chars = "{}{}".format(chars, string.digits)
    if level > 2:
        chars = "{}{}".format(chars, string.punctuation)
    
    for i in range(length):
        output.append(random.choice(chars))
    
    return "".join(output)

print(("-" * 30) + "\n Şifre Oluşturucu\n" + ("-" * 30))

password_length = int (input("Karakter uzunluğu: "))
password_level = int (input("Güvenilirlik: "))

password = generate_password(password_length, password_level)
print("\nYour password is: {}".format(password))





