# -*- coding: utf-8 -*-
"""Budget App

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19BQ0KEftW7pBNtR5GqoLYHvn8JK_WSN-
"""

# Freecodecamp's Scientific Computing with Python Projects - Budget App

# Create the Category class.
class Category:
    # It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment.
    def __init__(self, category_name):
        self.name = category_name
        # When objects are created, they are passed in the name of the category.
        # The class should have an instance variable called ledger that is a list.
        self.ledger = []

    def deposit(self, amount, description=""):
        # Append an object to the ledger list in the form of {"amount": amount, "description": description}.
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        # Check if there are enough funds
        if self.check_funds(amount):
            # Withdrawal amount stored as negative number
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def check_funds(self, amount):
        # Calculate total balance
        total_balance = sum(item['amount'] for item in self.ledger)
        # Check if there are enough funds
        if total_balance >= amount:
            return True
        else:
            return False

    def get_balance(self):
        # Calculate total balance based on deposits and withdrawals
        total_balance = sum(item['amount'] for item in self.ledger)
        return total_balance

    def transfer(self, amount, destination_category):
        # Check if there are enough funds for transfer
        if self.check_funds(amount):
            # Add withdrawal from source category
            self.withdraw(amount, f"Transfer to {destination_category.name}")
            # Add deposit to destination category
            destination_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            description = item['description'][:23]
            amount = '{:.2f}'.format(item['amount'])[-7:]
            items += f"{description:<23}{amount:>7}\n"
            total += item['amount']
        total_line = f"Total: {total:.2f}\n\n"
        return title + items + total_line

# Example usage:
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)

def create_spend_chart(categories):
    # Get the total spent for each category
    category_spent = {}
    for category in categories:
        total_spent = sum(item['amount'] for item in category.ledger if item['amount'] < 0)
        category_spent[category.name] = total_spent

    # Get the total spent across all categories
    total_spent_all = sum(category_spent.values())

    # Calculate the percentage spent for each category
    category_percentage = {}
    for category, spent in category_spent.items():
        percentage = (spent / total_spent_all) * 100
        category_percentage[category] = percentage

    # Create the bar chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:3}| "
        for category, percentage in category_percentage.items():
            bar = "o  " if percentage >= i else "   "
            chart += f"{bar}"
        chart += "\n"

    # Add horizontal line below the bars
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Determine the maximum length of category names
    max_name_length = max(len(category) for category in category_percentage.keys())

    # Add category names vertically below the bars
    for i in range(max_name_length):
        chart += "     "
        for category in category_percentage.keys():
            name = category[i] if i < len(category) else " "

            chart += f"{name}  "
        chart += "\n"

    return chart[:-1]

# Example usage:
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)


food_category = Category("Food")
food_category.deposit(1000, "Initial deposit")
food_category.withdraw(150, "Restaurant")
clothing_category = Category("Clothing")
clothing_category.deposit(500, "Initial deposit")
clothing_category.withdraw(100, "Shoes")
education_category = Category("Education")
education_category.deposit(200, "Initial deposit")
education_category.withdraw(100, "Books")
entertainment_category = Category("Entertainment")
entertainment_category.deposit(800, "Initial deposit")
entertainment_category.withdraw(200, "Concert")

print(clothing_category)

print(create_spend_chart([food_category, clothing_category, education_category, entertainment_category]))