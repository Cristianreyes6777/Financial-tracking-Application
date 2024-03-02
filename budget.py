from collections import defaultdict

"""

this is my User defined class. It is being exported into my main app.py file. 
this class containes the following:
    
    1. at least 1 private and 2 public self class attributes
    2. at least 1 private and 2 public class methods that take arguments, return values
    and are used by your program
    3. an init() class method that takes at least 1 argument
    4. A str() class method
    5. magic class method (my magic class method is the __len__ method that tells you how many transactions you've put in.')
    


"""


class Budget:
    def __init__(self, user_name, initial_balance):
        # Initializes a new budget instance for a user
        self.user_name = user_name  # Public attribute: The name of the user
        self._balance = initial_balance  # Private attribute: The starting balance
        # Public attribute: THIS IS MY LIST COLLECTION TYPE.I AM INITALIZING MY LIST TP STORE TRANSACTION RECORDS
        self.transactions = []
        # Public attribute: To store total expenses/income by category
        # THIS IS MY DICTIONARY COLLECTION TYPE. THIS IS WHERE i AM INITIALIZING MY DICT
        self.category_totals = defaultdict(float)

    def __str__(self):
        # representation of the budget instance
        return f"Budget for {self.user_name} with balance: {self._balance}"

    def __len__(self):
        # Magic method to return the number of transactions
        return len(self.transactions)

    def _update_balance(self, amount):
        # Private method to update the balance based on a transaction
        self._balance += amount

    def add_transaction(self, amount, category):
        # Public method to add a transaction and categorize it
        # THIS IS MY TUPLE COLLECTION TYPE. amount, category is stores as a tuple.
        self.transactions.append((amount, category))
        self._update_balance(amount)
        self.category_totals[category] += amount  # Update the category total

    def get_balance(self):
        # Public method to get the current balance
        return self._balance

    def get_category_total(self, category):
        # Public method to get the total amount spent or earned in a specific category
        return self.category_totals[category]
