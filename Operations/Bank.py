from Customer import Customers, dataclass, random
import json

accountFile = "accountData.json"


@dataclass(init=False)
class Banks:
    _account_number: int
    _pin: int
    _balance: int = 0

    @property
    def account_num(self) -> int:
        self._account_number = random.randint(1000000, 9999999)
        return self._account_number

    def set_pin(self, pin: int):
        self._pin = pin

    def create_account(self, customer: Customers):

        data = {customer.name: {"Username": customer.username,
                                "Balance": self._balance,
                                "Account Number": self.account_num,
                                "ID#": customer.id_number,
                                'Pin': self._pin
                                }
                }
        try:
            with open(accountFile, "r") as f:
                existing_records = json.load(f)
        except FileNotFoundError:
            existing_records = {}

        existing_records.update(data)
        with open(accountFile, "w") as f:
            json.dump(existing_records, f, indent=2)
