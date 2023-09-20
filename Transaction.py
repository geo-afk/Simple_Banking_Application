from Bank import accountFile, dataclass, json


@dataclass
class Transactions:
    customer_name: str

    def login(self) -> bool:
        opened = False
        try:
            with open(accountFile, "r") as f:
                entries = json.load(f)
                opened = True
        except FileNotFoundError as e:
            print("Invalid No Account was found for {}".format(self.customer_name))

        if opened:
            tries = 0
            while True:
                if self.customer_name in entries.keys():
                    username = input("Enter your username: ")
                    pin = int(input("Enter your Pin: "))

                    user = entries[self.customer_name]
                    if tries < 3:
                        tries += 1
                        if user.get("Username") != username and user.get("Pin") != pin:
                            print("\n***Incorrect Username and Password***\n")
                            continue
                        elif user.get("Username") != username:
                            print("\n***Incorrect Username***\n")
                            continue
                        elif user.get("Pin") != pin:
                            print("\n***Incorrect Password**\n")
                            continue
                        else:
                            return True
                    else:
                        print(f"You have Exceeded the amount of tries [{tries}]")
                        return False

    def withdrawal(self, amount):
        try:
            with open(accountFile, "r") as f:
                account_data = json.load(f)

            if self.customer_name in account_data.keys():
                customer = account_data[self.customer_name]

                if customer.get("Balance") > 100:
                    if amount > customer.get("Balance"):
                        print("withdrawal amount cannot be greater than account balance")
                    else:
                        customer["Balance"] = customer.get("Balance") - amount
                        with open(accountFile, "w") as f:
                            json.dump(account_data, f, indent=2)
                        return True
                else:
                    print(f"Insufficient Founds [{customer.get('Balance')}], cannot withdraw ")
                    return False
        except FileNotFoundError as e:
            print(f'{e}')
            print("No user data was found")

    def deposit(self, amount) -> bool:
        try:
            with open(accountFile, "r") as f:
                account_data = json.load(f)
            if self.customer_name in account_data.keys():
                customer = account_data[self.customer_name]
                if amount < 100000:
                    customer["Balance"] = customer.get("Balance") + amount
                    with open(accountFile, "w") as f:
                        json.dump(account_data, f, indent=2)
                    return True

                else:
                    print(f"Cannot deposit such a large amount [{amount}]")
                    return False
        except FileNotFoundError as e:
            print(f'{e}')
            print("No user data was found")

    def check_balance(self):
        try:
            with open(accountFile, "r") as f:
                data = json.load(f)
        except FileNotFoundError as e:
            print("{}".format(e))

        if data.get(self.customer_name):
            info = data.get(self.customer_name)
            print("\t**** Your Balance is ****")
            print(f"\t   ****** {info.get('Balance')} ******")
            print("\t************************")

    def transfer_cash(self, recipient_name, amount):
        try:
            with open(accountFile, "r") as f:
                account_data = json.load(f)
        except FileNotFoundError as e:
            print(f'{e}')
            print("No user data was found")
            return False

        if (
                self.customer_name in account_data
                and recipient_name in account_data
        ):
            sender_account = account_data[self.customer_name]
            recipient_account = account_data[recipient_name]

            if sender_account.get("Balance", 0) >= amount:
                sender_account["Balance"] -= amount
                recipient_account["Balance"] += amount

                with open(accountFile, "w") as f:
                    json.dump(account_data, f, indent=2)

                print(f"Transfer successful: ${amount} sent to {recipient_name}")
                return True
            else:
                print("Insufficient balance for the transfer.")
        elif recipient_name not in account_data:
            print("Recipient Could Not be found, they have no account at bank")
        else:
            print("One or both of the accounts do not exist.")

        return False
