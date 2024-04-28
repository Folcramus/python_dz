from main import Item, Store, User, Order, Worker
import copy
import time

time.sleep(1)

while True:
    print("запустить систему y/n?")
    if input() == 'y':
        print("введите имя, адрес")
        username = input()
        address = input()
        user = User(username, int(address), None)
        items = [Item("Молоко", 1, 1, 120, 3), Item("Хлеб", 2, 2, 12, 3), Item("Говядина", 3, 3, 12, 2)]
        items2  = [Item("Молоко", 1, 1, 120, 0), Item("Хлеб", 2, 2, 12, 34), Item("Говядина", 3, 3, 12, 230)]

        workers = [Worker(0, "Антон", None, None), Worker(1, "Георгий", None, None),  Worker(2, "Анатолий", None, None)]
        workers[0].get_shift("курьер", 130)
        workers[2].get_shift("сборщик", 100)
        store = Store(items2, 0, workers)
        print(store)
        print("Доступный вам склад: ")
        print(store)
        user.make_order(items, store)
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