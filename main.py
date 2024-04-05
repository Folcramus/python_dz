from dataclasses import dataclass
import time
from typing import Optional


@dataclass
class Item:
    name: str
    id: int
    id_prov: int
    price: int
    count: int


@dataclass
class Order:
    status: str
    list_items: list[Item]
    time_create: str
    time_delivery: str | None
    collector: str | None
    courier: str | None


class Worker:
    __id: id
    __name: str
    __salary: int | None
    __type: str
    __is_empl: bool

    def get_order(self, type: str) -> bool:
        if self.__type == type:
            return True

    # принять заказ, если возможно

    def get_shift(self, type: str):
        self.__type = type

    def __init__(self, id: int, name: str, salary: int | None, type: str):
        self.__id = id
        self.__name = name
        self.__salary = salary
        self.__type = type


class Store:
    __list_item: list[Item] = [None]

    def __init__(self, list_item: list[Item]):
        self.__list_item += list_item

    def send_request(self, request_item: list):
        prov = Provider()
        res_item = prov.send_order(request_item)
        self.__list_item.pop(0)
        for item in res_item:
            id_prov = item[0]
            index_prov = False
            for i, obj in enumerate(self.__list_item):
                if obj.id_prov == id_prov:
                    self.update_stocks(self.__list_item[i], item[1], True)
                    index_prov = True
                    break

            if not index_prov:
                self.__list_item.append(Item(item[2], 10, item[0], 1200, item[1]))
        return self.__list_item

    def update_stocks(self, item: Item, count: int, flag: bool):
        if flag:
            item.count += count
        else:
            item.count -=count
    # send_request - отправить заказ для провайдера (что привезти)

    def take_order(self, order: Order) -> bool:
        order.status = "Собираем"
        print(order)
        working = [Worker(1, "SIGMA", None, "sigm"), Worker(1, "SIGMA", None, "nosigm")]
        worker = None
        for work in working:
            if work.get_order("sigm"):
                worker = work
        self.set_storekeeper(order, worker)
        for item in order.list_items:
            id_prov = item.id_prov
            index_prov = False
            if self.__list_item[0] is None:
                self.__list_item.pop(0)
            for i, obj in enumerate(self.__list_item):
                if obj.id_prov == id_prov:
                    self.update_stocks(self.__list_item[i], item.count, False)
        "time.sleep(45)"

        courier = None
        for couriiers in working:
            if couriiers.get_order("nosigm"):
                courier = couriiers
        self.set_courier(order, courier)
        order.status = "Выдан курьеру"
        print(order)
        "time.sleep(45)"
        return True

    # принять заказ и начать его обрабатывать

    def set_courier(self, order: Order, courier: Worker):
        order.courier = courier

    # дать заказу курьера

    def set_storekeeper(self, order: Order, worker: Worker):
        order.collector = worker

    # дать заказу кладовщика

    def get_worker(self):
        pass


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
    __order: list[Order]

    def make_order(self, items: list[Item], store: Store):
        ordering = Order("новый", items, time.strftime("%H.%M.%S", time.localtime()), None, None, None)
        self.__order.append(ordering)

        booling = store.take_order(ordering)
        if booling:
            self.take_order()

    # сделать заказ

    def take_order(self):
        self.__order[-1].status = "Выдан"
        print(self.__order[-1])

    # забрать заказ

    def __init__(self, name: str, address: int, order: list[Order]):
        self.__name = name
        self.__address = address
        self.__order = order
