from budget import *

if __name__=="__main__":
    food = Category("Food")
    clothing = Category("Clothing")
    entertainment = Category("Entertainment")
    # num = 30 - len(food.name)
    # title_catagory = "*" * int(num/2) + food.name + "*" * int(num/2)
    # print(title_catagory)
    food.deposit(1000, "initial deposit")
    food.withdraw(200, "groceries")
    food.withdraw(50, "restaurant and more foo")

    clothing.deposit(500, "initial deposit")
    clothing.withdraw(100, "groceries")
    clothing.withdraw(50, "restaurant and more foo")

    entertainment.deposit(200, "initial deposit")
    entertainment.withdraw(30, "groceries")
    entertainment.withdraw(10, "restaurant and more foo")

    # Diplay
    # food.transfer(50, clothing)
    # for item in food.ledger:
    #     print(item["description"] + str(item["amount"]).rjust(30 - len(str(item["description"]))))
    # print("Total: ", food.get_balance())
    # print(sum(item["amount"] for item in food.ledger if item["amount"] < 0))

    categories = [food,clothing,entertainment]
    print(create_spend_chart(categories))