# app.py

from budget import Budget
import os
import sys

def load_transactions(filename):
    # Function to load transactions from a file, satisfying the file I/O requirement.
    # filename (str): The name of the file to read from.
    try:
        with open(filename, 'r') as file:
            transactions = file.readlines()
    except FileNotFoundError:
        print("File not found. Starting with an empty transaction list.")
        transactions = []
    else:
        transactions = [float(line.strip()) for line in transactions]
    return transactions

def save_transactions(filename, transactions):
    # Function to save transactions to a file.
    # filename (str): The name of the file to write to.
    # transactions (list): The list of transactions to save.
    with open(filename, 'w') as file:
        for transaction in transactions:
            file.write(f"{transaction}\n")

def main():
    # Main function to run the application.
    user_name = input("Enter your name: ")
    transactions_file = f"{user_name}_transactions.txt"
    initial_transactions = load_transactions(transactions_file)

    budget = Budget(user_name, sum(initial_transactions))
    print(budget)

    # Example transaction
    while True:
        try:
            amount = float(input("Enter a transaction amount (negative for expenses, positive for income), or 'quit' to exit: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
        else:
            budget.add_transaction(amount)
            print(f"New balance: {budget.get_balance()}")
        finally:
            choice = input("Do you want to add another transaction? (yes/no): ")
            if choice.lower() != 'yes':
                break

    # Save transactions at the end
    save_transactions(transactions_file, budget.transactions)
    print("Transactions saved. Exiting application.")

if __name__ == "__main__":
    main()




