mail = input("mail giriniz: ")
def isitmail(mail):
    if "@" and "." in mail:
        return True
    else:
        return False

print(isitmail(mail))
