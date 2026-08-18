class BankAccount:
    def __init__(self, name, password, balance=0):
        self.name = name
        self.password = password
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False


class Bank:
    FILE = "bank.txt"

    def __init__(self):
        self.accounts = {}
        self.load()

    def load(self):
        try:
            for line in open(self.FILE):
                n, p, b = line.strip().split(",")
                self.accounts[n] = BankAccount(n, p, b)
        except FileNotFoundError:
            pass

    def save(self):
        with open(self.FILE, "w") as f:
            for a in self.accounts.values():
                f.write(f"{a.name},{a.password},{a.balance}\n")

    def create(self):
        name = input("Name: ")
        if name in self.accounts:
            print("Account already exists!")
            return
        self.accounts[name] = BankAccount(name, input("Password: "))
        self.save()
        print("Account created!")

    def login(self):
        name = input("Name: ")
        if name in self.accounts and input("Password: ") == self.accounts[name].password:
            return self.accounts[name]
        print("Invalid login!")

    def transfer(self, account):
        name = input("Recipient: ")
        amount = float(input("Amount: "))
        if name in self.accounts and account.withdraw(amount):
            self.accounts[name].deposit(amount)
            self.save()
            print("Transfer successful!")
        else:
            print("Invalid recipient or insufficient balance!")


bank = Bank()

while True:
    print("\n1. Create\n2. Deposit\n3. Withdraw\n4. Balance\n5. Transfer\n6. Exit")
    choice = input("Choice: ")

    if choice == "1":
        bank.create()

    elif choice == "6":
        break

    elif choice in "2345":
        account = bank.login()

        if account:
            if choice == "2":
                account.deposit(float(input("Amount: ")))

            elif choice == "3":
                if not account.withdraw(float(input("Amount: "))):
                    print("Insufficient balance!")

            elif choice == "4":
                print("Balance:", account.balance)

            elif choice == "5":
                bank.transfer(account)

            bank.save()
