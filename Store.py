from Worker import Worker
from item_order import Item, Order
from main import Provider
from datetime import time


class Store:
    __id: int
    __list_item: list[Item] = [None]
    __work_item: list[Worker] = [None]
    __address: int
    __time_open: str
    __time_close: str
    __time_work: bool | None

    def __init__(self, id: int, list_item: list[Item], address: int, worker: list, open: str, close: str,
                 time_work: bool | None):
        self.__id = id
        self.__list_item = list_item
        self.__address = address
        self.__work_item = worker
        self.__time_open = open
        self.__time_close = close
        self.__time_work = time_work

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
                if courier.fine_worker():
                    self.set_courier(order, courier)
                    order.status = "Выдан курьеру"
                    print(order)
                    return True
                else:
                    print(f'курьеру {courier.name} назначен штраф')

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

    def store_id(self) -> int:
        return self.__id

    def store_open(self) -> str:
        return self.__time_open

    def store_close(self) -> str:
        return self.__time_close

    def store_address(self) -> int:
        return self.__address

    def store_time_work(self) -> bool:
        return self.__time_work

    def __str__(self):
        return f'список товаров {self.__list_item}'
