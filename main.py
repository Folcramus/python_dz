from dataclasses import dataclass
import time
from typing import Optional
from datetime import timedelta, datetime
from item_order import Item, Order


class Worker:
    id: id
    name: str
    salary: int | None
    type: str | None
    distance: int | None
    is_empl: bool
    minute_work: int | None
    time_work: int | None

    def get_order(self, type: str, time: float) -> bool:
        if self.type == type and self.is_empl == True and self.minute_work >= time:
            if self.type == "курьер":
                self.minute_work -= time
            else:
                self.minute_work -= time
            if self.minute_work <= 0:
                self.close_work()
            return True

    def __repr__(self):
        return f'имя: {self.name}    должность: {self.type}  на смене {self.is_empl} время работы {self.time_work} оставшиеся время: {self.minute_work} '

    # принять заказ, если возможно

    def get_shift(self, type: str, time: int):
        self.minute_work = self.time_work = time
        self.type = type
        self.is_empl = True

    def close_work(self):
        self.salary = 5 * self.time_work
        self.is_empl = False

    def __init__(self, id: int, name: str, type: str | None, time: int | None):
        self.id = id
        self.name = name
        self.type = type
        self.is_empl = False
        self.minute_work = time
        self.time_work = time


class Store:
    __list_item: list[Item] = [None]
    __work_item: list[Worker] = [None]
    __address: int

    def __init__(self, list_item: list[Item], address: int, worker: list):
        self.__list_item += list_item
        self.address = address
        self.__work_item += worker

    def send_request(self) -> list:
        prov = Provider()
        res_item = prov.send_order(self.__list_item)

        for item in res_item:
            index = 0
            for item in self.__list_item:
                if item.count == 0:
                    self.update_stocks(self.__list_item[index], 100, True)
        return self.__list_item

    def update_stocks(self, item: Item, count: int, flag: bool):
        if flag:
            item.count += count
        else:
            if item.count == 0:
                print(f"товара  {item} нет на складе, хотите отменить заказ? y/n")
                s = input()
                if self.close_order(s):
                    self.send_request()
                    item.count -= count
                else:
                    exit()
            else:
                item.count -= count

    def close_order(self, s: str) -> bool:
        if s in "y":
            return False
        else:
            return True


    # send_request - отправить заказ для провайдера (что привезти)

    def take_order(self, order: Order) -> bool:

        time = len(order.list_items) * 45
        time = time % 3600
        time_res1 = time / 60
        time_res = time_res1
        time_res += (order.address / 2) + 2
        order.time_delivery = time_res

        if self.__work_item[0] is None:
            self.__work_item.pop(0)
        worker = None

        for work in self.__work_item:
            if work.get_order("сборщик", time_res1):
                worker = work
        self.set_storekeeper(order, worker)
        order.status = "Собираем"
        print(order)
        for item in order.list_items:
            id_prov = item.id_prov
            if self.__list_item[0] is None:
                self.__list_item.pop(0)
            for i, obj in enumerate(self.__list_item):
                if obj.id_prov == id_prov:
                    self.update_stocks(self.__list_item[i], item.count, False)

        for couriiers in self.__work_item:

            if couriiers.get_order("курьер", (order.address / 2) + 2.0):
                courier = couriiers
                self.set_courier(order, courier)
                order.status = "Выдан курьеру"
                print(order)
                return True

    # принять заказ и начать его обрабатывать

    def set_courier(self, order: Order, courier: Worker):
        order.courier = courier

    # дать заказу курьера

    def set_storekeeper(self, order: Order, worker: Worker):
        order.collector = worker

    # дать заказу кладовщика

    def get_worker(self, worker: Worker):
        self.__work_item.append(worker)

    def search_item(self, id: int) -> Item:
        if self.__list_item[0] is None:
            self.__list_item.pop(0)
        for item in self.__list_item:
            if item.id == id:
                return item
    def __str__(self):
        return f'список товаров {self.__list_item}'


# Что должно быть? Id внутри системы складов, id внутри системы поставщика, название, себестоимость
class Provider:  # поставщик
    def send_order(self, list_item: list):
        return_item = []
        for item in list_item:
            return_item.append(item)
        return return_item

    # send_order - принять и отправить заказ складу


class User:
    __name: str
    __address: int
    __order: Order | None

    def make_order(self, items: list[Item], store: Store):
        ordering = Order("новый", items, time.strftime("%H:%M:%S", time.localtime()), None, None, None, self.__address)
        self.__order = ordering

        booling = store.take_order(ordering)
        if booling:
            self.take_order()

    # сделать заказ

    def take_order(self):
        self.__order.status = "Выдан"
        print(self.__order)

    # забрать заказ

    def __init__(self, name: str, address: int, order: Order | None):
        self.__name = name
        self.__address = address
        self.__order = order
