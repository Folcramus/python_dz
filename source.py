from main import Item, Store, User, Order
import copy
b = [Item("Легенда1", 12, 12, 12, 120), Item("Сигмоид1", 45, 45, 12, 10),  Item("Зигхаиль", 13, 13, 12, 10)]


gh = [Item("Легенда1", 12, 12, 12, 1)]

lj = Store(b, 0)

order = Order("Новый" ,b, "12",  None, None, None, 100)


fgf = User("Sigma", 12, [order])



print(fgf.make_order(gh, lj))
