password=input("Enter the password:")
uc,lc,dig=False,False,False
if len(password)<8:
        print("Not a strong password")
else:
    for c in password:
        if c.isupper():
            uc=True
        if c.islower():
            lc=True 
        if c.isdigit():
            dig=True 
    if uc and lc and dig:
        print("Is a strong password")