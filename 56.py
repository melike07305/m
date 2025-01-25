while True:
    password = input("please type new password: ")
    if len(password) >= 8:
        print("Accepted password")
        break
    else:
        print("password length must be at least 8 symbols")

#please type new password: 123456
#password length must be at least 8 symbols
#please type new password: 196189287789
#Accepted password
