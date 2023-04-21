from builtins import set
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description =""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description =""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer to {self.name}")
            return True
        else: return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

def create_spend_chart(categories):
    lst_withdraw = []
    total_withdraw = 0
    # Calculate percentage
    for category in categories:
        withdraw = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        lst_withdraw.append(withdraw)
        total_withdraw += withdraw
    percentage_lst = [(withdraws/total_withdraw) * 100 for withdraws in lst_withdraw]

    # Build chart
    chart = "Percentage spent by category\n"
    for i in range(100,-1,-10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentage_lst:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += " "*4 + "---"*len(categories) + "\n"

    # Balance length of category's name
    max_length = max(len(category.name) for category in categories)
    add_empty = [category.name.ljust(max_length) for category in categories]

    for i in range(max_length):
        chart += " " * 5
        for name in add_empty:
            chart += name[i] + " "*2
        chart += "\n"
    return chart.rstrip()





