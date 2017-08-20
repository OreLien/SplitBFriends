# Event class
class Event(object):
    """Event taking place"""

    def __init__(self, nb_of_friends=0, title="Crazy party", total_amount=0):
        self.__title = title
        self.__nb_of_friends = int(nb_of_friends)
        self.__total_amount = float(total_amount)
        self.__average_amount = 0

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_nb_of_friends(self, nb_of_friends):
        self.__nb_of_friends = nb_of_friends

    def get_nb_of_friends(self):
        return self.__nb_of_friends

    def set_total_amount(self, total_amount):
        self.__total_amount = total_amount

    def get_total_amount(self):
        return self.__total_amount

    def set_average_amount(self, average_amount):
        self.__average_amount = average_amount

    def get_average_amount(self):
        return self.__average_amount


# Compute total amount from each paid amount
def compute_total_amount(list_of_friends):
    total_amount = 0
    for i, friend in enumerate(list_of_friends):
        total_amount += friend.get_paid_amount()
    return total_amount


# Compute amount each friend should pay
def compute_amount_to_pay(total_amount, nb_of_friends):
    return total_amount / nb_of_friends
