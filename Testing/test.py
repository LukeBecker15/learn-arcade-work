class Transaction:
    transaction_count = 0
    def __init__(self, date, amount, account):
        self.date = date
        self.amount = amount
        self.account = account

def main():
    my_transaction = Transaction("9/20/2020", 10, "320984230981")
    my_transaction = Transaction("9/20/2020", 10, "320984230981")
    my_transaction = Transaction("9/20/2020", 10, "320984230981")
    my_transaction = Transaction("9/20/2020", 10, "320984230981")

    print(Transaction.transaction_count)

main()

class Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    def bark(self):
        if self.weight < 10:
            print("Yip!")
        else:
            print("Woof")



def main_2():
    my_dog = Dog()
    my_dog.name = "Spot"
    my_dog2 = Dog()
    my_dog2.name = "Rover"

    my_dog2.bark()
    my_dog.bark()
main_2()