from dataclasses import dataclass

from Worker import Courier, Storekeeper


@dataclass
class Item:
    name: str
    id: int
    id_prov: int
    price: int
    count: int

    def __str__(self):
        return f'номер: {self.id}, название: {self.name}, количество: {self.count}, цена: {self.price}   '


@dataclass
class Order:
    status: str
    list_items: list
    time_create: str
    time_delivery: str | None
    collector: Storekeeper | None
    courier: Courier | None
    address: int

    def __str__(self):
        return f'статус: {self.status}, список: {self.list_items}, время создания: {self.time_create}, время доставки: {self.time_delivery}, сборщик: {self.collector} , курьер: {self.courier}, адрес доставки {self.address} '

