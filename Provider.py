from dataclasses import dataclass
import time
from typing import Optional
from datetime import timedelta, datetime
from item_order import Item, Order


# Что должно быть? Id внутри системы складов, id внутри системы поставщика, название, себестоимость
class Provider:  # поставщик
    def send_order(self, list_item: list) -> list:
        return_item = []
        for item in list_item:
            if item.count == 0:
                self.update_stocks(item, 100)
            return_item.append(item)
        return return_item


    def update_stocks(self, item: Item, count: int):
            item.count += count

    # send_order - принять и отправить заказ складу
