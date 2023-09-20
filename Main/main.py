from Operations.Transaction import Transactions, accountFile, Customers, Banks

# Transaction Fee
# except (ValueError, AttributeError):
# Set Constants
# format floats :.2f
# ?🤔 Loan
# Add staff Functionalities

def do_transactions() -> None:
    output = """
        1. Check Balance
        2. Withdrawal 
        3. Deposit
        4. Transfer Cash 
        ==> 
        """

    print("\nTo login First => ")
    full_name: str = input("Enter your name : ")
    transaction = Transactions(full_name)
    if transaction.login():
        while True:
            choice = int(input(output))
            if choice == 1:
                transaction.check_balance()
            elif choice > 1 or choice < 5:
                amount = int(input("Enter amount for transaction: "))
                if choice == 2:
                    transaction.withdrawal(amount)
                if choice == 3:
                    transaction.deposit(amount)
                else:
                    recipient = input(
                        "Enter the recipient's Name to transfer founds to: ")
                    transaction.transfer_cash(recipient, amount)

            again = input("Would you like to go again[Y/N]:")
            if again.upper() == 'Y':
                continue
            else:
                break

        else:
            print("Invalid Input")


def create_account() -> None:
    choice = input("Would you like to add account[Y/N]: ")

    if choice.upper() == "Y":
        full_name: str = input("Enter your name: ")
        pin = int(input("Set a secure pin: "))
        # pin = getpass.getpass(prompt="Set a secure pin: ")
        customer = Customers()
        customer.set_name(full_name)

        bank = Banks()
        bank.set_pin(pin)
        bank.create_account(customer)

        account_details = f"""
        ********** {customer.name} **********
           Your Username is {customer.username}
           Your ID Number is {customer.id_number}
           Your Account Number is {bank.account_num}
           Your Pin is       ****
        **************************************
        """
        print(account_details)
    else:
        exit(0)


def main() -> None:
    exists = False
    try:
        with open(accountFile, "r") as f:
            exists = True
    except IOError:
        print("Error No User data found!!\n")

    if exists:
        do_transactions()
    else:
        create_account()
        choice = input("Would you like to do another transaction[Y/N]: ")
        if choice.upper() == 'Y':
            main()


if __name__ == "__main__":
    main()
