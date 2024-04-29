class Worker:
    id: id
    name: str
    salary: int | None
    type: str | None
    distance: int | None
    is_empl: bool
    minute_work: int | None
    time_work: int | None

    def get_order(self, type: str, time: float) -> bool:
        if self.type == type and self.is_empl == True and self.minute_work >= time:
            if self.type == "курьер":
                self.minute_work -= time
            else:
                self.minute_work -= time
            if self.minute_work <= 0:
                self.close_work()
            return True

    def __repr__(self):
        return f'имя: {self.name}    должность: {self.type}  на смене {self.is_empl} время работы {self.time_work} оставшиеся время: {self.minute_work} '

    # принять заказ, если возможно

    def get_shift(self, type: str, time: int):
        self.minute_work = self.time_work = time
        self.type = type
        self.is_empl = True

    def close_work(self):
        self.salary = 5 * self.time_work
        self.is_empl = False

    def __init__(self, id: int, name: str, type: str | None, time: int | None):
        self.id = id
        self.name = name
        self.type = type
        self.is_empl = False
        self.minute_work = time
        self.time_work = time