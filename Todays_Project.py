khata = {}  

def add_coustomer_name():
    name = input("Add Customer Name : ").strip()  

    if name not in khata:
        khata[name] = []   
        print(f"{name} customer name added successfully")
    else:
        print("Customer already exists")

def give_money():
    name = input("Add Customer Name : ").strip()

    if name not in khata:
        print("Customer name is not in khata book")
        return

    amount = int(input("Enter the amount given : "))
    khata[name].append(("gave", amount))
    print("Transaction recorded successfully")

def got_money():
    name = input("Add Customer Name : ").strip()

    if name not in khata:
        print("Customer not found!")
        return

    amount = int(input("Enter the amount got : "))
    khata[name].append(("got", amount))
    print("Transaction recorded successfully")

def show_khata():
    print(" \n Here is the full khata book till now: \n ")

    for name, transactions in khata.items():
        print(f"Customer: {name}")
        for t, amount in transactions:
            print(f"  {t} : {amount}")
        print("----------------------")

def show_balance():
    name = input("Enter customer name : ").strip()

    if name not in khata:
        print("Customer doesn't exist")
        return

    Total_gave = sum(amount for t, amount in khata[name] if t == "gave")
    Total_got = sum(amount for t, amount in khata[name] if t == "got")

    balance = Total_gave - Total_got

    print(f"Balance for {name}: {balance}")

    if balance > 0:
        print("Esko itna dena hai!")
    elif balance < 0:
        print("Isse itna lena hai!")
    else:
        print("All clear, no balance left 😮‍💨")

# Main Loop
while True:
    print("\n1. Add Customer")
    print("2. Give Money")
    print("3. Got Money")
    print("4. Show Khata")
    print("5. Check Balance")
    print("6. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        add_coustomer_name()
    elif choice == "2":
        give_money()
    elif choice == "3":
        got_money()
    elif choice == "4":
        show_khata()
    elif choice == "5":
        show_balance()
    elif choice == "6":
        break
    else:
        print("Yeh kya daal diya 🤷‍♂️")
