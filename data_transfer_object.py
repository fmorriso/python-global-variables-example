from dataclasses import dataclass


@dataclass
class DTO:
    __number: int | float

    @property
    def number(self) -> int | float:
        return self.__number

    @number.setter
    def number(self, number: int | float):
        self.__number = number

