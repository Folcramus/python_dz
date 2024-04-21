from dataclasses import dataclass


@dataclass
class Item:
    name: str
    id: int
    id_prov: int
    price: int
    count: int


@dataclass
class Order:
    status: str
    list_items: list
    time_create: str
    time_delivery: str | None
    collector: str | None
    courier: str | None
    address: int