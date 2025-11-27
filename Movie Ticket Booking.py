age = int (input("enter your age : "))
ticket = bool(input("What is the password it 0 or 1 : "))
flag = bool(ticket)
if age >= 18 :
    print("You are 18 +")
    if(ticket == 1):
        print("Identity Verified ! Entry allowed")
    else :
        print("You are not allowed")
elif age <= 15 :
    print("you are a todler")
else :
    print("you are just a child")
