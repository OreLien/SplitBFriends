# Balance class
class Balance(object):
    """Balance between two friends"""

    def __init__(self, from_friend, to_friend, amount):
        self.__from_friend = from_friend
        self.__to_friend = to_friend
        self.__amount = float(amount)

    def set_from_friend(self, from_friend):
        self.__from_friend = from_friend

    def get_from_friend(self):
        return self.__from_friend

    def set_to_friend(self, to_friend):
        self.__to_friend = to_friend

    def get_to_friend(self):
        return self.__to_friend

    def set_amount(self, amount):
        self.__amount = float(amount)

    def get_amount(self):
        return self.__amount
