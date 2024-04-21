from main import Item, Store, User, Order, Worker
import copy
b = [Item("Легенда1", 12, 12, 12, 120), Item("Сигмоид1", 45, 45, 12, 10),  Item("Зигхаиль", 13, 13, 12, 10)]


gh = [Item("Легенда1", 12, 12, 12, 1)]



order = Order("Новый" ,b, "12",  None, None, None, 100)


fgf = User("Sigma", 12, [order])



print(fgf.make_order(gh,  Store(b, 0, [Worker(0, "Антон", "курьер", 120), Worker(1, "Георгий", "сборщик", 120)])))
