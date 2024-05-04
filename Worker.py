import random

from abc import ABC, abstractmethod


# класс работника
class Worker(ABC):
    __id: id
    __name: str
    __salary: float
    __type: str | None
    __distance: int | None
    __is_empl: bool
    __minute_work: int | None
    __time_work: int | None
    __is_working: bool

    @abstractmethod
    def get_order(self, type: str, time: float, is_empl: bool) -> bool:
        pass

    @abstractmethod
    def get_shift(self, time: int):
        pass

    @abstractmethod
    def close_work(self, time: float):
        pass

    @abstractmethod
    def fine_worker(self) -> bool:
        pass

    @abstractmethod
    def worker_name(self) -> str:
        pass

    @abstractmethod
    def worker_is_empl(self) -> bool:
        pass


class Courier(Worker):

    def __repr__(self):
        return f'имя: {self.__name}    должность: {self.__type}  на смене {self.__is_empl} время работы {self.__time_work} оставшиеся время: {self.__minute_work}'

    # принять заказ, если возможно
    def get_order(self, type: str, time: float, is_empl: bool) -> bool:
        if self.__type == type and is_empl == True:
            if not self.__is_working and self.__time_work >= time:
                self.__minute_work -= time
                self.__is_working = True
                if self.__minute_work < time:
                    self.close_work(time)
                return True
            else:
                return False
        else:

            return False

    def get_shift(self, time: int):
        self.__minute_work = self.__time_work = time
        self.__type = "курьер"
        self.__is_empl = True

    def fine_worker(self) -> bool:
        rand = random.randint(0, 100)
        if rand >= 1:
            self.__salary -= 300
            return True
        else:
            return False

    def close_work(self, time: float):
        if self.__is_empl:
            self.__salary = 5 * self.__time_work * (time / 60)
            self.__is_empl = False
            print(f'Работник {self.__name} Зарплата {self.__salary}')

    def worker_name(self) -> str:
        return f'{self.__name}'

    def worker_is_empl(self) -> bool:
        return self.__is_empl

    def worker_is_working(self):
        if self.__is_working:
            self.__is_working = False
        else:
            self.__is_working = True

    def courier_name(self):
        return self.__name

    def courier_salary(self):
        return self.__salary
    def __init__(self, id: int, name: str, type: str | None, time=1):
        self.__id = id
        self.__name = name
        self.__is_empl = False
        self.__salary = 0
        self.__type = type
        self.__minute_work = time
        self.__time_work = time
        self.__is_working = False


class Storekeeper(Worker):
    __type: str | None

    def get_order(self, type: str, time: float, is_empl: bool) -> bool:
        if self.__type == type and is_empl == True:
            if not self.__is_working and self.__time_work >= time:
                self.__minute_work -= time
                self.__is_working = True
                if self.__minute_work < time:
                    self.close_work(time)
                return True
            else:
                return False

    def __repr__(self):
        return f'имя: {self.__name}    должность: {self.__type}  на смене {self.__is_empl} время работы {self.__time_work} оставшиеся время: {self.__minute_work} '

    # принять заказ, если возможно

    def get_shift(self, time: int):
        self.__minute_work = self.__time_work = time
        self.__type = "сборщик"
        self.__is_empl = True

    def fine_worker(self) -> bool:
        rand = random.randint(0, 100)
        if rand >= 98:
            self.__salary -= 300
            return True
        else:
            return False

    def close_work(self, time: float):
        self.__salary = 5 * self.__time_work * (time / 60)
        self.__is_empl = False

    def worker_name(self) -> str:
        return f'{self.__name}'

    def worker_is_empl(self) -> bool:
        return self.__is_empl


    def worker_is_working(self):
        if self.__is_working:
            self.__is_working = False
        else:
            self.__is_working = True

    def __init__(self, id: int, name: str, type: str | None, time: int | None):
        self.__id = id
        self.__name = name
        self.__is_empl = False
        self.__salary = 0
        self.__type = type
        self.__minute_work = time
        self.__time_work = time
        self.__is_working = False
