from menu import MENU, resources

profit = 0


def report(profit):
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {profit}")


def is_resources_sufficient(order_ingredients):
    """Return True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins(drink_cost):
    """Return the total calculated from coins inserted"""
    print(f"Please insert coins for ${drink_cost}")
    total = int(input("Quarters?: ")) * 0.25
    total += int(input("Dimes?: ")) * 0.1
    total += int(input("Nickles?: ")) * 0.05
    total += int(input("Pennies?: ")) * 0.01
    print(f"Received Total Money ${total}")
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False of Money is insufficient"""
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        return True
    else:
        print(f"Sorry that's not enough money. Required ${drink_cost}, "
              f"Money Received ${money_received}. Money Returned")
    return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        report(profit)
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins(drink["cost"])
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
