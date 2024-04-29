from datetime import time
import time

from Store import Store
from item_order import Order, Item


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