import logo
import os
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0,
}


def show_report(resource):
    print(f"Water: {resource['water']}ml")
    print(f"Milk: {resource['milk']}ml")
    print(f"Coffee: {resource['coffee']}ml")
    if resource['Money'] != 0:
        print(f"Money: ${resource['Money']}")


def check_ingredient(order):
    for name in MENU[order]['ingredients']:
        # TODO: 4. If ingredients not enough --> prompt do not enough  ingredients
        if resources[name] < MENU[order]['ingredients'][name]:
            print(f"There is not enough {name}. Please refill")
            return False
    return True


def process_coins(order):
    # TODO: 5. Ask customers what kind of coins they have?
    print("Please insert coins")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many quarters?: "))
    nickles = int(input("how many quarters?: "))
    pennies = int(input("how many quarters?: "))
    received = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if received > MENU[order]['cost']:
        print(f"Here is ${received - MENU[order]['cost']} in change")
        return True
    elif received == MENU[order]['cost']:
        return True
    # TODO: 6. If money does not enough print "Sorry that's not enough money. Money refunded".
    else:
        print(f"Sorry that's not enough money. We need more ${MENU[order]['cost'] - received}. Money refunded.")
        return False


def process():
    turn_off = False
    while not turn_off:
        print(logo.logo)
        print("Welcome To PoPo's coffee")
        # TODO: 1. asking user "What would you like? (espresso/latte/cappuccino/report/fill): "
        customer_want = input("What would you like? (espresso/latte/cappuccino/report/fill/clear(to clear screen)/off: ").lower()
        # TODO: 2. Check what customer wants. If they want some action beside coffee did it
        if customer_want == "report":
            show_report(resources)
        elif customer_want == "fill":
            resources['water'] = 300
            resources['milk'] = 200
            resources['coffee'] = 100
        elif customer_want in ['espresso', 'latte', 'cappuccino']:
            # TODO: 3. if customer want coffee check whether ingredients enough for making the coffee.
            if check_ingredient(customer_want):
                if process_coins(customer_want):
                    # TODO: 7. If money is enough successful and deduct ingredient
                    for resource_use in MENU[customer_want]['ingredients']:
                        resources[resource_use] -= MENU[customer_want]['ingredients'][resource_use]
                    resources['Money'] += MENU[customer_want]['cost']
                    print(f"Here is your {customer_want}. Enjoy!")
        elif customer_want == 'clear':
            os.system('clear')
        elif customer_want == 'off':
            turn_off = True
        # TODO: 8. Miss Typing
        else:
            print("Miss Typing. Please Retype Again")


process()
