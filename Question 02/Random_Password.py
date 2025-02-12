import random

def gen_Random():
    upperCase = "ABCDEFGHIJKLMNOPQRSTVUWXYZ"
    lowerCase = "abcdefghijklmnopqrstuvwxyz"
    digits = "1234567890"
    specialChar = "!@#$%^&*"

    pass_least = [
        random.choice(upperCase),
        random.choice(lowerCase),
        random.choice(digits),
        random.choice(digits),
        random.choice(specialChar)
    ]

    collection = upperCase + lowerCase + digits + specialChar
    while(len(pass_least) < 16):
        new = random.choice(collection)
        if new  not in pass_least:
            pass_least.append(new)
    random.shuffle(pass_least)
    return "".join(pass_least)

print(gen_Random())