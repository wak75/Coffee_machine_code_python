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
}

def coin_sum():
    penny=0.01
    nickel=0.05
    dime=0.10
    quater=0.25

    print("Enter the number of coins: ")
    the_penny=int(input("enter the number of penny($0.01): "))
    the_nickel=int(input("enter the number of nickel($0.05): "))
    the_dime=int(input("Enter the number of dime($0.10): "))
    the_quater=int(input("Enter the number of quater($0.25): "))

    final_sum=(the_penny*penny)+(the_nickel*nickel)+(the_dime*dime)+(the_quater*quater)
    return round(final_sum,2)


def check_resources(coffee):
    if coffee=='1':
        if resources['water'] >= MENU['espresso']['ingredients']['water']:
            resources['water']-=MENU['espresso']['ingredients']['water']
        elif resources['water'] < MENU['espresso']['ingredients']['water']:
            return False


        if resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
            resources['coffee']-=MENU['espresso']['ingredients']['coffee']
        elif resources['coffee'] < MENU['espresso']['ingredients']['cofee']:
            return False
        else:
            return False

    if coffee=='2':
        if resources['water'] >= MENU['latte']['ingredients']['water']:
            resources['water']-=MENU['latte']['ingredients']['water']
        elif resources['water'] < MENU['latte']['ingredients']['water']:
            return False
        
        if resources['milk'] >= MENU['latte']['ingredients']['milk']:
            resources['milk']-=MENU['latte']['ingredients']['milk']
        elif resources['milk'] < MENU['latte']['ingredients']['milk']:
            return False

        if resources['coffee'] >= MENU['latte']['ingredients']['coffee']:
            resources['coffee']-=MENU['latte']['ingredients']['coffee']
        
        else:
            return False
    
    if coffee=='3':
        if resources['water'] >= MENU['cappuccino']['ingredients']['water']:
            resources['water']-=MENU['cappuccino']['ingredients']['water']
        elif resources['water'] < MENU['cappuccino']['ingredients']['water']:
            return False

        if resources['milk'] >= MENU['cappuccino']['ingredients']['milk']:
            resources['milk']-=MENU['cappuccino']['ingredients']['milk']
        elif resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
            return False

        if resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']:
            resources['coffee']-=MENU['cappuccino']['ingredients']['coffee']
        else:
            return False
    


def check_money(money_recieved,coffee):
    suf_resources=check_resources(coffee)
    if coffee=='1':
        if (coffee=='1') and (MENU['espresso']['cost']>money_recieved):
            print(f"sorry the money is not enough!! refunding your ${money_recieved}")
            
        elif (coffee=='1') and (MENU['espresso']['cost']<money_recieved):
            return_money=money_recieved-(MENU['espresso']['cost'])
            if suf_resources!=False:
                print(f"Here is you remaining money ${return_money}")
                print("Money recieved!!! Here's your Espresso!!!Enjoy")
            else:
                print("Sorry!! Currently we are out of resources")
                return 0
        else:
            print("Money recieved!!! Here's your Espresso!!!Enjoy")


    if coffee=='2':
        if (coffee=='2') and (MENU['latte']['cost']>money_recieved):
            print(f"sorry the money is not enough!! refunding your ${money_recieved}")
            
        elif (coffee=='2') and (MENU['latte']['cost']<money_recieved):
            return_money=money_recieved-(MENU['latte']['cost'])
            if suf_resources!=False:
                print(f"Here is you remaining money ${return_money}")
                print("Money recieved!!! Here's your latte!!!Enjoy")
            else:
                print("Sorry!! Currently we are out of resources")
                return 0
        else:
            print("Money recieved!!! Here's your latte!!!Enjoy")


    if coffee=='3':
        if (coffee=='3') and (MENU['cappuccino']['cost']>money_recieved):
            print(f"Here is you remaining money ${return_money}")
            
        elif (coffee=='3') and (MENU['cappuccino']['cost']<money_recieved):
            return_money=money_recieved-(MENU['cappuccino']['cost'])
            if suf_resources!=False:
                print(f"Here is you remaining money ${return_money}")
                print("Money recieved!!! Here's your cappuccino!!!Enjoy")
            else:
                print("Sorry!! Currently we are out of resources")
                return 0
        else:
            print("Money recieved!!! Here's your cappuccino!!!Enjoy")







should_continue=True
from art import logo 
print(logo)
while should_continue:
    print('''Here is the menu: 
                1. espresso
                2. latte
                3. cappuccino''')
    coffee=(input("Enter the type of coffee you want, pls type your choice: "))    




    if coffee=='1':
        print(f"You have chooseen 'Espresso',and that would cost you  ${MENU['espresso']['cost']} ")
        
        money_recieved=coin_sum()
        print(money_recieved)
        check_money(money_recieved,coffee)
    elif coffee=='2':
        print(f"You have chooseen 'latte',and that would cost you  ${MENU['latte']['cost']} ")
        
        money_recieved=coin_sum()
        print(money_recieved)
        check_money(money_recieved,coffee)
    elif coffee=='3':
        print(f"You have chooseen 'cappuccino',and that would cost you  ${MENU['cappuccino']['cost']} ")
        
        money_recieved=coin_sum()
        print(money_recieved)
        check_money(money_recieved,coffee)
    elif coffee=='resources':
        print(resources)


    want_more=input("want something more? press 'y' or 'n': ").lower()
    if want_more=='n':
        should_continue=False