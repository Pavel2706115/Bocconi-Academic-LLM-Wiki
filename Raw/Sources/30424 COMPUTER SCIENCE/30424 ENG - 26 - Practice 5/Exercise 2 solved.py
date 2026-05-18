import random


def generate_password(num):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_char = "!#$%&_*+-^?"

    num = max(num, 8)

    final_pwd = random.choice(letters) + random.choice(numbers)+ random.choice(special_char)

    all_chars = letters + numbers + special_char

    for i in range(num - 3):
        final_pwd = final_pwd + random.choice(all_chars)

    return final_pwd


        







    
