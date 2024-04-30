import random

from abc import ABC, abstractmethod


class Worker(ABC):
    id: id
    name: str
    salary: float
    type: str | None
    distance: int | None
    is_empl: bool
    minute_work: int | None
    time_work: int | None

    @abstractmethod
    def get_order(self, type: str,  time: float) -> bool:
        pass

    @abstractmethod
    def get_shift(self,  time: int):
        pass

    @abstractmethod
    def close_work(self, time: float):
        pass

    @abstractmethod
    def fine_worker(self) -> bool:
        pass

    def __init__(self, id: int, name: str, type: str | None, time: int | None):
        self.id = id
        self.name = name
        self.type = type
        self.is_empl = False
        self.salary = 0
        self.minute_work = time
        self.time_work = time


class Courier(Worker):
    def get_order(self, type: str, time: float) -> bool:
        if self.type == type and self.is_empl == True and self.minute_work >= time:

            self.minute_work -= time

            if self.minute_work < time:
                self.close_work(time)
            return True

    def __repr__(self):
        return f'имя: {self.name}    должность: {self.type}  на смене {self.is_empl} время работы {self.time_work} оставшиеся время: {self.minute_work} '

    # принять заказ, если возможно

    def get_shift(self,  time: int):
        self.minute_work = self.time_work = time
        self.type = "курьер"
        self.is_empl = True

    def fine_worker(self) -> bool:
        rand = random.randint(0, 100)
        if rand >= 98:
            self.salary -= 300
            return True
        else:
            return False

    def close_work(self, time: float):
        self.salary = 5 * self.time_work * (time / 60)
        self.is_empl = False


class Storekeeper(Worker):
    def get_order(self, type: str, time: float) -> bool:
        if self.type == type and self.is_empl == True and self.minute_work >= time:

            self.minute_work -= time
            if self.minute_work < time:
                self.close_work(time)
            return True

    def __repr__(self):
        return f'имя: {self.name}    должность: {self.type}  на смене {self.is_empl} время работы {self.time_work} оставшиеся время: {self.minute_work} '

    # принять заказ, если возможно

    def get_shift(self,  time: int):
        self.minute_work = self.time_work = time
        self.type = "сборщик"
        self.is_empl = True

    def fine_worker(self) -> bool:
        rand = random.randint(0, 100)
        if rand >= 98:
            self.salary -= 300
            return True
        else:
            return False

    def close_work(self, time: float):
        self.salary = 5 * self.time_work * (time / 60)
        self.is_empl = False
