# budget.py

class Budget:
    def __init__(self, user_name, initial_balance):
        # Initializes a new budget instance for a user
        # user_name (str): The name of the user
        # initial_balance (float): The starting balance
        self.user_name = user_name
        self._balance = initial_balance  # Private attribute to track the balance
        self.transactions = []  # Public attribute to store transaction records

    def __str__(self):
        # Provides a human-readable representation of the budget instance
        return f"Budget for {self.user_name} with balance: {self._balance}"

    def __len__(self):
        # Magic method to return the number of transactions
        return len(self.transactions)

    def _update_balance(self, amount):
        # Private method to update the balance based on a transaction
        # This method satisfies the private method requirement.
        self._balance += amount

    def add_transaction(self, amount):
        # Public method to add a transaction
        # amount (float): The transaction amount (negative for expenses, positive for income)
        # This method satisfies the public method requirement and the use of parameters/arguments.
        self.transactions.append(amount)
        self._update_balance(amount)

    def get_balance(self):
        # Public method to get the current balance
        # Returns the current balance, satisfying the public method and return value requirements.
        return self._balance
