# water = 400
# milk = 540
# beans = 120
# cups = 9
# money = 550
#
#
# def buy():
#     print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
#     coffee_type = input()
#     if coffee_type == 'back':
#         return
#     else:
#         coffee_type = int(coffee_type)
#     global water
#     global beans
#     global money
#     global milk
#     global cups
#     if cups < 1:
#         print("Sorry, not enough cups")
#         return
#     if coffee_type == 1:
#         if water >= 250 and beans >= 16:
#             print("I have enough resources, making you a coffee!")
#             water -= 250
#             beans -= 16
#             cups -= 1
#             money += 4
#             return
#     elif coffee_type == 2:
#         if water >= 350 and milk >= 75 and beans >= 20:
#             print("I have enough resources, making you a coffee!")
#             water -= 350
#             milk -= 75
#             beans -= 20
#             cups -= 1
#             money += 7
#             return
#     else:
#         if water >= 200 and milk >= 100 and beans >= 12:
#             print("I have enough resources, making you a coffee!")
#             water -= 200
#             milk -= 100
#             beans -= 12
#             cups -= 1
#             money += 6
#             return
#     print("Sorry, cant make you coffee")
#
#
# def fill():
#     global water
#     global beans
#     global milk
#     global cups
#     water += int(input("Write how many ml of water do you want to add:\n"))
#     milk += int(input("Write how many ml of milk do you want to add:\n"))
#     beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
#     cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
#
#
# def take():
#     global money
#     print("I gave you $" + str(money))
#     money = 0
#
#
# def remaining():
#     print("The coffee machine has:\n", water, "of water\n", milk, "of milk\n", beans, "of coffee beans\n", cups,
#           "of disposable cups\n", '$' + str(money) + " of money\n")
#
#
# def main():
#     while True:
#         action = input("Write action (buy, fill, take, remaining, exit):\n")
#         print()
#         if action == 'buy':
#             buy()
#         elif action == 'fill':
#             fill()
#         elif action == 'take':
#             take()
#         elif action == 'remaining':
#             remaining()
#         else:
#             break
#
#
# main()


class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.state = "choosing an action"
        print("Write action (buy, fill, take, remaining, exit):")

    def state_update(self, new_state):  # states can be: choosing an action, choosing a type of coffee, giving money,
        # filling water, milk, beans, cup, off
        self.state = new_state

    def process(self, user_input):
        print()
        if self.state == "choosing an action":
            if user_input == "buy":
                self.state = "choosing a type of coffee"
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                return
            elif user_input == "fill":
                print("Write how many ml of water do you want to add:")
                self.state = "filling water"
                return
            elif user_input == "take":
                self.take()
                self.state = "choosing an action"
                print("Write action (buy, fill, take, remaining, exit):")
                return
            elif user_input == "remaining":
                self.remaining()
                self.state = "choosing an action"
                print("Write action (buy, fill, take, remaining, exit):")
                return
            elif user_input == "exit":
                self.state = "off"
                return
        if self.state == "choosing a type of coffee":
            self.buy(user_input)
            self.state = "choosing an action"
            print("Write action (buy, fill, take, remaining, exit):")
            return
        if self.state == "filling water":
            self.fill(user_input)
            self.state = "filling milk"
            return
        if self.state == "filling milk":
            self.fill(user_input)
            self.state = "filling beans"
            return
        if self.state == "filling beans":
            self.fill(user_input)
            self.state = "filling cups"
            return
        if self.state == "filling cups":
            self.fill(user_input)
            self.state = "choosing an action"  # better to have additional state before choosing an action to avoid printings
            print("Write action (buy, fill, take, remaining, exit):")

    def what_lucks(self, coffee_type):
        lucks = []
        if coffee_type == 1:
            if self.water < 250:
                lucks.append("water")
            if self.beans < 16:
                lucks.append("beans")
        elif coffee_type == 2:
            if self.water < 350:
                lucks.append("water")
            if self.milk < 75:
                lucks.append("milk")
            if self.beans < 20:
                lucks.append("beans")
        elif coffee_type == 3:
            if self.water < 200:
                lucks.append("water")
            if self.milk < 100:
                lucks.append("milk")
            if self.beans < 12:
                lucks.append("beans")
        return lucks

    def buy(self, coffee_type):
        if coffee_type == "back":
            self.state = "choosing an action"
            return
        else:
            coffee_type = int(coffee_type)
        if self.cups < 1:
            print("Sorry, not enough cups")
            return
        if coffee_type == 1:
            if self.water >= 250 and self.beans >= 16:
                print("I have enough resources, making you a coffee!\n")
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
                return
            else:
                lucks = self.what_lucks(1)
        elif coffee_type == 2:
            if self.water >= 350 and self.milk >= 75 and self.beans >= 20:
                print("I have enough resources, making you a coffee!\n")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
                return
            else:
                lucks = self.what_lucks(2)
        else:
            if self.water >= 200 and self.milk >= 100 and self.beans >= 12:
                print("I have enough resources, making you a coffee!\n")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
                return
            else:
                lucks = self.what_lucks(3)
        print("Sorry, not enough", end=' ')
        print_lucks = ""
        for i in lucks:
            print_lucks += "{}, ".format(i)
        print_lucks = print_lucks[:-2]
        print(print_lucks)

    def fill(self, user_input):
        if self.state == "filling water":
            self.water += int(user_input)
            print("Write how many ml of milk do you want to add:")
        elif self.state == "filling milk":
            self.milk += int(user_input)
            print("Write how many grams of coffee beans do you want to add:")
        elif self.state == "filling beans":
            self.beans += int(user_input)
            print("Write how many disposable cups of coffee do you want to add:")
        elif self.state == "filling cups":
            self.cups += int(user_input)
        # self.water += int(input("Write how many ml of water do you want to add:\n"))
        # self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        # self.beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        # self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        print("I gave you $" + str(self.money) + "\n")
        self.money = 0

    def remaining(self):
        print("The coffee machine has:\n", self.water, "of water\n", self.milk, "of milk\n", self.beans,
              "of coffee beans\n", self.cups, "of disposable cups\n", '$' + str(self.money) + " of money\n")


def main():
    my_machine = CoffeeMachine(400, 540, 120, 9, 550)
    # my_machine = CoffeeMachine(0, 0, 0, 1, 0)
    while my_machine.state != "off":
        my_machine.process(input())


main()
