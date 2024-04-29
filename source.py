import copy
from datetime import datetime

import time

from Store import Store
from User import User
from Worker import Worker
from item_order import Item

time.sleep(1)


def findClosestValue(storeList, target):
    def difference(storeList):
        return abs(storeList - target)

    result = min(storeList, key=difference)

    return result
def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    else:  # Over midnight
        return nowTime >= startTime or nowTime <= endTime

while True:
    print("запустить систему y/n?")
    if input() == 'y':
        print("введите имя, адрес")
        username = input()
        address = input()
        user = User(username, int(address), None)
        items = [Item("Молоко", 1, 1, 120, 3), Item("Хлеб", 2, 2, 12, 3), Item("Говядина", 3, 3, 12, 2)]
        items2 = [Item("Молоко", 1, 1, 120, 0), Item("Хлеб", 2, 2, 12, 34), Item("Говядина", 3, 3, 12, 230)]

        workers = [Worker(0, "Антон", None, None), Worker(1, "Георгий", None, None), Worker(2, "Анатолий", None, None)]
        workers[0].get_shift("курьер", 130)
        workers[2].get_shift("сборщик", 100)
        time1 = '3:00AM'
        store = [Store(1, items2, 0, workers, '3:00AM', '11:00PM', isNowInTimePeriod(datetime.strptime('3:00AM', "%I:%M%p"), datetime.strptime('11:00PM', "%I:%M%p"), datetime.strptime('2:00PM', "%I:%M%p"))), Store(2, items2, 10, workers, '7:00AM', '11:00PM', isNowInTimePeriod(datetime.strptime('8:00AM', "%I:%M%p"), datetime.strptime('10:00PM', "%I:%M%p"), datetime.strptime('2:00AM', "%I:%M%p"))), Store(3, items2, 45, workers, '1:00AM', '11:00PM', isNowInTimePeriod(datetime.strptime('1:00AM', "%I:%M%p"), datetime.strptime('11:00PM', "%I:%M%p"), datetime.strptime('2:00AM', "%I:%M%p")))]
        store_addr = []
        for store_ind in store:
            if store_ind.store_time_work():
                store_addr.append(store_ind.store_address())
        res = findClosestValue(store_addr, user.user_address())
        res_store = None
        for store_ind in store:
            if store_ind.store_address() == res:
                res_store = store_ind
                break

        print("Доступный вам склад: ")
        print(res_store)
        user.make_order(items, res_store)
        print(store)
    else:
        break

'''
b = [Item("Легенда1", 12, 12, 12, 120), Item("Сигмоид1", 45, 45, 12, 10),  Item("Зигхаиль", 13, 13, 12, 10)]


gh = [Item("Легенда1", 12, 12, 12, 1)]



order = Order("Новый" ,b, "12",  None, None, None, 100)


fgf = User("Sigma", 12, [order])



print(fgf.make_order(gh,  Store(b, 0, [Worker(0, "Антон", "курьер", 120), Worker(1, "Георгий", "сборщик", 120)])))



'''
