import copy
from datetime import datetime
import asyncio
import time

from Store import Store
from User import User
from Worker import Worker, Courier, Storekeeper
from item_order import Item

time.sleep(1)


# вычисление нужного склада
def findClosestValue(storeList, target):
    def difference(storeList):
        return abs(storeList - target)

    result = min(storeList, key=difference)

    return result


# работа склада
def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < endTime:
        return startTime <= nowTime <= endTime
    else:  # Over midnight
        return nowTime >= startTime or nowTime <= endTime


order = [Item("Молоко", 1, 1, 120, 3), Item("Хлеб", 2, 2, 12, 3), Item("Говядина", 3, 3, 12, 2)]
items_store = [Item("Молоко", 1, 1, 120, 0), Item("Хлеб", 2, 2, 12, 34), Item("Говядина", 3, 3, 12, 230)]

workers = [Courier(0, "Антон", None, None), Courier(1, "Георгий", None, None),
           Storekeeper(2, "Анатолий", None, None)]
workers[0].get_shift(120)
workers[2].get_shift(678)
time1 = datetime.now()
curr_time = time1.strftime("%I:%M%p")

#создание списка складов
store = [Store(1, items_store, 0, workers, '3:00AM', '11:00AM',
               isNowInTimePeriod(datetime.strptime('3:00AM', "%I:%M%p"),
                                 datetime.strptime('11:00AM', "%I:%M%p"),
                                 datetime.strptime(curr_time, "%I:%M%p"))),
         Store(2, items_store, 10, workers, '7:00AM', '11:00PM',
               isNowInTimePeriod(datetime.strptime('8:00AM', "%I:%M%p"),
                                 datetime.strptime('10:00PM', "%I:%M%p"),
                                 datetime.strptime(curr_time, "%I:%M%p"))),
         Store(3, items_store, 45, workers, '1:00AM', '11:00AM',
               isNowInTimePeriod(datetime.strptime('1:00AM', "%I:%M%p"),
                                 datetime.strptime('11:00AM', "%I:%M%p"),
                                 datetime.strptime(curr_time, "%I:%M%p")))]
store_addr = []
for store_ind in store:
    if store_ind.store_time_work():
        store_addr.append(store_ind.store_address())
while True:

    print("запустить систему y/n?")
    if input() == 'y':
        print("введите имя, адрес")
        username = input()
        address = input()

        user = User(username, int(address), None)
        print(f'пользователь {user}')

        res = findClosestValue(store_addr, user.user_address())
        res_store = None
        for store_ind in store:
            if store_ind.store_address() == res:
                res_store = store_ind
                break

        print("Доступный вам склад: ")
        print(res_store.store_id())
        user.make_order(order, res_store)
        print(workers)


    else:
        break
