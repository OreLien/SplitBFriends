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


# Return true of false if balance is over or not
def is_balance_over(list_of_friends):
    for i, friend in enumerate(list_of_friends):
        # we use 0.1 in case of fraction
        if abs(friend.get_balance_amount()) > 0.1:
            return False
    return True


# Pick a friend having a positive balance (= should receive money)
def pick_positive_balance_friend(list_of_friends):
    for i, friend in enumerate(list_of_friends):
        if friend.get_balance_amount() > 0:
            return friend
    return None


# Pick a friend having a negative balance (= should give money)
def pick_negative_balance_friend(list_of_friends):
    for i, friend in enumerate(list_of_friends):
        if friend.get_balance_amount() < 0:
            return friend
    return None


# Create a balance between two friends
def create_balance(list_of_balances, positive_balance_friend, negative_balance_friend):
    positive_balance_amount = positive_balance_friend.get_balance_amount()
    negative_balance_amount = negative_balance_friend.get_balance_amount()
    amount = min(positive_balance_amount, abs(negative_balance_amount))
    positive_balance_friend.decrease_balance_amount(amount)
    negative_balance_friend.increase_balance_amount(amount)
    balance = Balance(negative_balance_friend, positive_balance_friend, amount)
    list_of_balances.append(balance)