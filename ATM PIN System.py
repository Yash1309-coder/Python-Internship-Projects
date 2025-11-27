balance = 5000
pin = 1234

attempts = 0
while attempts < 3 :
    user_pin = int (input("Enter your pin : "))

    if user_pin == pin :
        print("Your balance is", balance)
        amount = int (input("enter amount to withdrawl : "))
        balance -= amount 
        print("Amount recieved" , "New Balance is : " , balance)
        break

    else :
        attempts += 1
        print ("wrong pin")
        print("no of attampts left", 3 - attempts)
    if (attempts == 0) :
        print("I caugh you , theif")
        print("Exiting ...")
