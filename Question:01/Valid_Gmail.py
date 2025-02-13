def isValid(e):
    sp = e.split('@')
    if(len(sp) != 2):
        return "Not an valid email format"
    username = sp[0]
    for x in username:
        if x == " " or "&" or "=" or "_" or "'" or "-" or "+" or "," or "<" or ">":
            return "There are invalid characters in this email address"
        if x.isupper():
            return "There are capital letters in the mail"
    
    mail = sp[1]
    if(mail != "gmail.com"):
        return "Mail shoud end with @gmail.com"
    
    return "Valid mail format"
mail = input("Enter gmail: ")
print(isValid(mail))