# At the moment, the coffee machine has $550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.
# For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
# For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
# And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee beans. It costs $6.

water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
balance = 550

while True:
    action = input("Write action (buy, fill, take, remaining, exit):")
    if action == 'exit':
        break
    elif action == 'remaining':
        print("The coffee machine has:", 
              f"{water} ml of water", 
              f"{milk} ml of milk", 
              f"{coffee_beans} g of coffee beans", 
              f"{disposable_cups} disposable cups", 
              f"${balance} of money",
             sep="\n")
    elif action == 'buy':
        coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if coffee == "back":
            continue
        coffee = int(coffee)
        if coffee == 1:
            if water < 250 or coffee_beans < 16 or disposable_cups < 1:
                missing_item = ""
                if water < 250:
                    missing_item = 'water'
                elif coffee_beans < 16:
                    missing_item = 'coffee beans'
                else:
                    missing_item = 'disposable cups'
                print(f"Sorry, not enough {missing_item}!")
                continue
            water -= 250
            coffee_beans -= 16
            disposable_cups -= 1
            balance += 4
            print("I have enough resources, making you a coffee!")
        if coffee == 2:
            if water < 350 or milk < 75 or coffee_beans < 20 or disposable_cups < 1:
                missing_item = ""
                if water < 350:
                    missing_item = 'water'
                elif milk < 75:
                    missing_item = 'milk'
                elif coffee_beans < 20:
                    missing_item = 'coffee beans'
                else:
                    missing_item = 'disposable cups'
                print(f"Sorry, not enough {missing_item}!")
                continue
            water -= 350
            milk -= 75
            coffee_beans -= 20
            disposable_cups -= 1
            balance += 7
            print("I have enough resources, making you a coffee!")
        if coffee == 3:
            if water < 200 or milk < 100 or coffee_beans < 12 or disposable_cups < 1:
                missing_item = ""
                if water < 200:
                    missing_item = 'water'
                elif milk < 100:
                    missing_item = 'milk'
                elif coffee_beans < 12:
                    missing_item = 'coffee beans'
                else:
                    missing_item = 'disposable cups'
                print(f"Sorry, not enough {missing_item}!")
                continue
            water -= 200
            milk -= 100
            coffee_beans -= 12
            disposable_cups -= 1
            balance += 6
            print("I have enough resources, making you a coffee!")
    elif action == "take":
        print(f"I gave you ${balance}")
        balance -= balance
    else:
        water += int(input("Write how many ml of water you want to add:"))
        milk += int(input("Write how many ml of milk you want to add:"))
        coffee_beans += int(input("Write how many grams of coffee beans you want to add:"))
        disposable_cups += int(input("Write how many disposable cups you want to add:"))


# print(f"""The coffee machine has:
# {water} ml of water
# {milk} ml of milk
# {coffee_beans} g of coffee beans
# {disposable_cups} disposable cups
# ${balance} of money""")
# water = int(input("Write how many ml of water the coffee machine has:"))
# milk = int(input("Write how many ml of milk the coffee machine has:"))
# coffee_beans = int(input("Write how many grams of coffee beans the coffee machine has:"))
# cups_needed = int(input("Write how many cups of coffee you will need:"))

# # 200 ml of water, 50 ml of milk, and 15 g of coffee beans for 1 cup
# cups = min([water // 200, milk // 50, coffee_beans // 15])
# if cups > cups_needed:
#     print(f"Yes, I can make that amount of coffee (and even {cups-cups_needed} more than that)")
# elif cups == cups_needed:
#     print("Yes, I can make that amount of coffee")
# else:
#     print(f"No, I can make only {cups} cups of coffee")