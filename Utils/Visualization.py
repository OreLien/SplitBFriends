import matplotlib.pyplot as plt

# Generate visualization
def show_visualization(list_of_friends, event, translator):
    fig = plt.figure(translator.trans("balance_summary"))
    ax = fig.add_subplot(1, 1, 1)
    bars = [i + 1 for i in range(len(list_of_friends))]
    paid_amounts = [val.get_paid_amount() for i, val in enumerate(list_of_friends)]
    bar_width = 0.5
    ax.bar(left=bars,
           height=paid_amounts,
           width=bar_width,
           label=translator.trans("paid_amount"),
           color="#258BFF")
    subbars_debit = []
    balance_amounts_debit = []
    bottom_amounts_debit = []
    subbars_credit = []
    balance_amounts_credit = []
    bottom_amounts_credit = []
    for i in range(len(list_of_friends)):
        if list_of_friends[i].get_paid_amount() > event.get_average_amount():
            balance_amount_credit = list_of_friends[i].get_paid_amount() - event.get_average_amount()
            subbars_credit.append(i + 1)
            balance_amounts_credit.append(balance_amount_credit)
            bottom_amounts_credit.append(event.get_average_amount())
        elif list_of_friends[i].get_paid_amount() < event.get_average_amount():
            balance_amount_debit = event.get_average_amount() - list_of_friends[i].get_paid_amount()
            subbars_debit.append(i + 1)
            balance_amounts_debit.append(balance_amount_debit)
            bottom_amounts_debit.append(list_of_friends[i].get_paid_amount())

    if subbars_debit and balance_amounts_debit and bottom_amounts_debit:
        ax.bar(left=subbars_debit,
               height=balance_amounts_debit,
               width=bar_width,
               bottom=bottom_amounts_debit,
               label=translator.trans("debit_amount"),
               color="r")

    if subbars_credit and balance_amounts_credit and bottom_amounts_credit:
        ax.bar(left=subbars_credit,
               height=balance_amounts_credit,
               width=bar_width,
               bottom=bottom_amounts_credit,
               label=translator.trans("credit_amount"),
               color="g")

    names = [val.get_name() for i, val in enumerate(list_of_friends)]
    plt.xticks(bars, names)
    ax.set_xlabel(translator.trans("friend"))
    ax.set_ylabel(translator.trans("amount") + " (" + translator.trans("in") + " €)")
    plt.legend(loc="upper right")
    plt.xlim([min(bars) - bar_width, max(bars) + bar_width])
    plt.show()
