from dataclasses import dataclass
import random


@dataclass(init=False)
class Customers:
    _full_name: str
    _id_number: int
    _username: str

    @property
    def username(self) -> str:
        first_name = self._full_name.split(" ")[0]
        last_third = str(self.id_number)[2:]
        self._username = first_name + last_third
        return self._username

    @property
    def id_number(self) -> int:
        self._id_number = random.randint(10000, 99999)
        return self._id_number

    def set_name(self, full_name: str):
        self._full_name = full_name

    @property
    def name(self):
        return self._full_name
