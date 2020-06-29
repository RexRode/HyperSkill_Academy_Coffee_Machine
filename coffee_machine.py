print("""Write action (buy, fill, take, remaining, exit):""")
buy_fill_take = input()
espressos_bought = 0
lattes_bought = 0
cappuccinos_bought = 0
water_added = 0
milk_added = 0
coffee_beans_added = 0
cups_added = 0
take_amount = 0


def buy(a):
    global counter
    counter = 0
    while counter < 1:

        if a == "back":
            break
        elif "1" in a or "2" in a or "3" in a or "4" in a or "5" in a or "6" in a or "7" in a or "8" in a or "9" in a or "0" in a:
            b = int(a)

        global espressos_bought
        global lattes_bought
        global cappuccinos_bought
        global water
        global milk
        global coffee_beans
        global cups
        global money
        money = 550 + 4 * espressos_bought + 7 * lattes_bought + 6 * cappuccinos_bought
        water = 400 - 250 * espressos_bought - 350 * lattes_bought - 200 * cappuccinos_bought + water_added
        milk = 540 - lattes_bought * 75 - 100 * cappuccinos_bought + milk_added
        coffee_beans = 120 - 16 * espressos_bought - 20 * lattes_bought - 12 * cappuccinos_bought + coffee_beans_added
        cups = 9 - espressos_bought - lattes_bought - cappuccinos_bought + cups_added
        if b == 1 and water >= 250 and coffee_beans >= 16 and cups >= 1:
            espressos_bought += 1
            print("I have enough resources, making you a coffee!")
        if b == 1 and water < 250:
            print("Sorry, not enough water!")
        if b == 2 and water >= 350 and milk >= 75 and coffee_beans >= 20 and cups >= 1:
            lattes_bought += 1
            print("I have enough resources, making you a coffee!")
        if b == 2 and water < 350:
            print("Sorry, not enough water!")
        if b == 3 and water >= 200 and milk >= 100 and coffee_beans >= 12 and cups >= 1:
            cappuccinos_bought += 1
            print("I have enough resources, making you a coffee!")
        if b == 3 and water < 200:
            print("Sorry, not enough water!")

        counter += 1


def remaining():
    global water
    global milk
    global coffee_beans
    global cups
    global money
    global espressos_bought
    global lattes_bought
    global cappuccinos_bought
    money = (550 + 4 * espressos_bought + 7 * lattes_bought + 6 * cappuccinos_bought) * (1 - take_amount)
    water = 400 - 250 * espressos_bought - 350 * lattes_bought - 200 * cappuccinos_bought + water_added
    milk = 540 - lattes_bought * 75 - 100 * cappuccinos_bought + milk_added
    coffee_beans = 120 - 16 * espressos_bought - 20 * lattes_bought - 12 * cappuccinos_bought + coffee_beans_added
    cups = 9 - espressos_bought - lattes_bought - cappuccinos_bought + cups_added
    print(f"""
The coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{cups} of disposable cups
{money} of money""")


def take():
    global money
    global take_amount
    print(f"I gave you ${money}")
    money = 0
    take_amount = 1


def fill(a, b, c, d):
    global water_added
    global milk_added
    global coffee_beans_added
    global cups_added
    water_added = a
    milk_added = b
    coffee_beans_added = c
    cups_added = d


def coffee_machine_function():
    global buy_fill_take
    if buy_fill_take == "exit":
        exit()
    while True:
        if buy_fill_take == "buy":
            input_thing = input()
            buy(input_thing)
            buy_fill_take = input()
        elif buy_fill_take == "take":
            take()
            buy_fill_take = input()
        elif buy_fill_take == "remaining":
            remaining()
            buy_fill_take = input()
        elif buy_fill_take == "fill":
            fill(int(input()), int(input()), int(input()), int(input()))
            buy_fill_take = input()
        if buy_fill_take == "exit":
            exit()


coffee_machine_function()
