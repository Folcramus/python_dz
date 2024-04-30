from datetime import time
import time

from Store import Store
from item_order import Order, Item


class User:
    __name: str
    __address: int
    __order: Order | None

    def make_order(self, items: list[Item], store: Store):
        order = Order("новый", items, time.strftime("%I:%M%p", time.localtime()), None, None, None, self.__address)
        self.__order = order

        booling = store.take_order(order)
        if booling:
            self.take_order()

    # сделать заказ

    def take_order(self):
        print(f'{self.__name} вы получили заказ? y/n')
        s = input()
        if s == 'y':
            self.__order.status = "Выдан"
            print(self.__order)
        else:
            self.__order.status = "Заказ не выдан"

    # забрать заказ

    def user_address(self):
        return self.__address

    def __init__(self, name: str, address: int, order: Order | None):
        self.__name = name
        self.__address = address
        self.__order = order
