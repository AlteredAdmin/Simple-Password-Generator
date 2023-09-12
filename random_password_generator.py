import random
import string


def generate_password(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))


password_length = int(input("Enter the desired length of the password: "))
print("Generated password: ", generate_password(password_length))
