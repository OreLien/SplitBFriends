# Python program to make balance between friends expenses
import sys
import argparse
import Utils.Friend as Friend
import Utils.Event as Event
import Utils.Balance as Balance
import Utils.Visualization as Visualization

# Argument parser configuration
parser = argparse.ArgumentParser(
    description="Split expenses between friends, let's Split and Be Friends !"
)
parser.add_argument('-v', '--visualization', help='Generate visualization of balances', action='store_true')
args = parser.parse_args()

# Event configuration
print("\n############")
print("## Event : ")
print("############\n")

try:
    nb_of_friends = float(input("\t● Number of friends ? > "))
except Exception as e:
    print("\nError : number of friends should be a number")
    sys.exit()

event = Event.Event(nb_of_friends)
list_of_friends = []

# Retrieve friend details
for i in range(event.get_nb_of_friends()):
    print("\n############")
    print("## Friend n° : " + str(i + 1))
    print("############\n")
    try:
        name = str(input("\t● Name ? > "))
    except Exception as e:
        print("\nError : invalid name")
        sys.exit()
    try:
        paid_amount = float(input("\t● Paid amount ? > "))
    except Exception as e:
        print("\nError : paid amount should be a number")
        sys.exit()
    friend = Friend.Friend(i, name, float(paid_amount))
    list_of_friends.append(friend)

# Set total amount
total_amount = Event.compute_total_amount(list_of_friends)
event.set_total_amount(total_amount)

# Amount to pay for each friend
amount_to_pay = Event.compute_amount_to_pay(event.get_total_amount(), event.get_nb_of_friends())
event.set_average_amount(amount_to_pay)

# Set balance amount
for i, friend in enumerate(list_of_friends):
    balance_amount = friend.get_paid_amount() - event.get_average_amount()
    friend.set_balance_amount(balance_amount)

list_of_balances = []

while not Balance.is_balance_over(list_of_friends):
    positive_balance_friend = Balance.pick_positive_balance_friend(list_of_friends)
    negative_balance_friend = Balance.pick_negative_balance_friend(list_of_friends)
    if positive_balance_friend is not None and negative_balance_friend is not None:
        Balance.create_balance(list_of_balances, positive_balance_friend, negative_balance_friend)

print("\n############")
print("## Balance summary : ")
print("############\n")

print("\t● Total amount > " + "{0:.2f}".format(event.get_total_amount()) + "€")
print("\t● Amount by friend > " + "{0:.2f}".format(event.get_average_amount()) + "€")

for i, balance in enumerate(list_of_balances):
    print("\t● Friend [" + balance.get_from_friend().get_name() + "] should pay " + "{0:.2f}".format(
        balance.get_amount()) + "€ to [" + balance.get_to_friend().get_name() + "]")

if args.visualization is True:
    Visualization.show_visualization(list_of_friends, event)
