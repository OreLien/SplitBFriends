# Friend class
class Friend(object):
    """Friend involved into the event"""

    def __init__(self, id, name, paid_amount):
        self.__id = id
        self.__name = name
        self.__paid_amount = float(paid_amount)
        self.__balance_amount = 0

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_paid_amount(self, paid_amount):
        self.__paid_amount = float(paid_amount)

    def get_paid_amount(self):
        return self.__paid_amount

    def set_balance_amount(self, balance_amount):
        self.__balance_amount = float(balance_amount)

    def get_balance_amount(self):
        return self.__balance_amount

    def increase_balance_amount(self, amount):
        self.__balance_amount += amount

    def decrease_balance_amount(self, amount):
        self.__balance_amount -= amount
