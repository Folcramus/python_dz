from datetime import time
import time

from Store import Store
from item_order import Order, Item

#класс пользователя
class User:
    __name: str
    __address: int
    __order: Order | None
      # сделать заказ
    def make_order(self, items: list[Item], store: Store):
        #создание объекта заказа
        order = Order("новый", items, time.strftime("%I:%M%p", time.localtime()), None, None, None, self.__address)
        self.__order = order
        #выполнение заказа
        booling = store.take_order(order)
        if booling:
            self.take_order()
        else:
            print(f'Заказ отменен из за занятости работников')


  # забрать заказ
    def take_order(self):
        print(f'{self.__name} вы получили заказ? y/n')
        s = input()
        if s == 'y':
            self.__order.status = "Выдан"
            print(self.__order)
            self.__order.courier.worker_is_working()
            self.__order.collector.worker_is_working()
        else:
            self.__order.status = "Заказ не выдан"


    #адрес юзера
    def user_address(self):
        return self.__address

    def __init__(self, name: str, address: int, order: Order | None):
        self.__name = name
        self.__address = address
        self.__order = order

    def __str__(self):
        return f'Имя: {self.__name}, адрес: {self.__address}, магазин: {self.__order}'
