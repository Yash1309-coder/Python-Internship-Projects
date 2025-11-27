def binary_to_gray(binary):
    gray = binary[0]
    for i in range(1,len(binary)) :
        gray += str(int(binary[i-1])^int(binary[i]))
    return gray
    
def gray_to_binary(gray):
    binary = gray[0]
    for i in range(1,len(gray)) :
        binary += str(int(binary[i-1])^int(gray[i]))
    return binary


while True:
        
        
    print("""
    1. Addition 
    2. Substraction
    3. Multiplication
    4. Division
    5. inr to dollar 
    6. degree to fahrenhit
    7. binary to gray conversion
    8. gray to binary conversion
    9. Exit
    
    """)
    
    choice = input("Enter your choise : ")
    if choice == "1" :
        num1 = int(input("Enter Number 1 : "))
        num2 = int(input("Enter Number 2 : "))
        print ("Additioon of number is " , num1 + num2)
    elif choice =="2" :
        num1 = int(input("Enter Number 1 : "))
        num2 = int(input("Enter Number 2 : "))
        print ("Substraction  of number is " , num1 - num2)
    elif choice =="3" :
        num1 = int(input("Enter Number 1 : "))
        num2 = int(input("Enter Number 2 : "))
        print ("Multiplication  of number is " , num1 * num2)
    elif choice == "4":
        num1 = int(input("Enter Number 1 : "))
        num2 = int(input("Enter Number 2 : "))
        if num2 != 0  :
            print("Division of number is" , num1 / num2)
        else :
            print("Numbers are not Divisible")
    elif choice =="5" :
        num1 = int(input("Enter the value in rupee "))
        print("Value in doller is : " , num1*88.46)
    elif choice =="6" :
        num1 = int(input("Value in degree"))
        print("Value in fahrenhit : " , (num1*1.8)+32)
    elif choice =="7" :
        binary = input("Enter your binary code ")
        print("Gray code : " , binary_to_gray(binary))
    elif choice =="8" :
        gray = input("Enter your Gray code ")
        print("Binary code : " , gray_to_binary(gray))
    elif choice =="9" :
        break
    else :
        print ("invalid")
        

