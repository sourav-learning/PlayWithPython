def transaction(balance, txn_amount, transaction_typ):
    if transaction_typ == 'CREDIT':
        return balance + txn_amount
    elif transaction_typ == 'DEBIT':
        return balance - txn_amount
    

print("SELECT THE NUMBER OF YOUR PREFERRED OPERATION")

balance = int(10000)
while True:
    option = int(input("1. Check Balance \n2. Withdraw Cash \n3. Deposit Cash \n4. End Transaction"))
    if option == 1:
        print("Your account balance is : ", float(balance), "INR")
    elif option == 2:
        txn_amount = int(input("Enter amount to withdraw : "))
        if txn_amount > balance:
            print("Insufficient balance. Please enter correct option : ")
            continue
        balance = transaction(balance, txn_amount, "DEBIT")
        print("Your account balance after debiting ", float(txn_amount), "INR is : ", float(balance), "INR")
    elif option == 3:
        txn_amount = int(input("Enter amount to deposit : "))
        balance = transaction(balance, txn_amount, "CREDIT")
        print("Your account balance after crediting ", float(txn_amount), "INR is : ", float(balance), "INR")
    elif option == 4:
        print("Thanks for using our banking service.")
        break
    else :
        print("Incorrect option selected. Please retry")
