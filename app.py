# app.py

from budget import Budget
from collections import defaultdict
import os
import sys
import datetime
import re


def get_filename(user_name):
    """
    this function Generates a filename for the budget report based on the user's name
    we use the datetime module in order to get the current date and time and have that 
    included in our saved file. So in essence, we return the file name 'name_budget_report_(current month)_(current year).txt;.
    if that file does not exist we make it. 
    This is my file creation and user defined function.
    
    """
    directory = "Budget_report"
    if not os.path.exists(directory):
        os.makedirs(directory)
    current_time = datetime.datetime.now()
    filename = os.path.join(
        directory, f"{user_name}_budget_report_{current_time.strftime('%B')}_{current_time.year}.txt")
    return filename


def load_budget_state(filename):
    """
    Loads the initial balance and category totals from a specified file.
    This function attempts to open and read a file whose name is provided by the 'filename' parameter.
    It expects the file to contain lines formatted as 'Key: Value', where 'Key' can be 'Current Balance'
    or a category name. 'Value' is expected to be a numeric amount. 
    
    
    """
    category_totals = defaultdict(float)
    try:
        with open(filename, 'r') as file:
            for line in file:
                key, value = line.strip().split(": ")
                if key == "Current Balance":
                    balance = float(value)
                else:
                    category_totals[key] = float(value)
    except FileNotFoundError:
        print("File not found. Starting with an empty budget list.")
        balance = 0.0  # Start with a zero balance if no file found
    except ValueError:
        print("Error processing file. Ensure it's in the correct format.")
        balance = 0.0  # Default to zero balance on error
    return balance, category_totals


def save_current_state(filename, budget):
    """
    
    Saves the current state of the budget, including balance and category totals.
    This function opens (or creates if not existing) a file for writing, specified by the 'filename' parameter. It then writes
    the current balance of the budget on the first line in the format 'Current Balance: {amount}'. Following the balance,
    it writes out each category and its total in the format '{category}: {total}' on separate lines.
    
    This is also my outputfile requirement for the project.
    """
    with open(filename, 'w') as file:
        # Write the current balance
        file.write(f"Current Balance: {budget.get_balance()}\n")
        # Write category totals
        for category, total in budget.category_totals.items():
            file.write(f"{category}: {total}\n")


def validate_transaction_input(input_str):
    """
    Validates the transaction input format using regex module.
    Expected format: 'amount,category'. we take the user input pass it in this function
    and make sure it matches returning a truthy or falsy value.
    """
    return re.match(r'^-?\d+(\.\d+)?,.*$', input_str)


# This is the entry point of the application.
if __name__ == "__main__":
    # Prompt the user for their name to personalize the budget report.
    user_name = input("Enter your name: ")

    # Generate the filename for the budget report based on the user's name and the current date.
    transactions_file = get_filename(user_name)
    # Load the initial balance and category totals from the saved file, if it exists.
    initial_balance, loaded_category_totals = load_budget_state(
        transactions_file)

    # Initialize the Budget object with the user's name and the loaded initial balance.
    budget = Budget(user_name, initial_balance)
    # Update the budget's category totals with the loaded values from the file.
    budget.category_totals.update(loaded_category_totals)

    # THI IS MY SET CONTAINER REQUIREMENT
    #keeps track of unique categories added during the current session.
    current_session_categories = set()

    # Print the initial state of the budget for the user.
    print(budget)

    # Start an input loop to process user transactions or exit commands.
    while True:
        # Prompt the user to enter a transaction or 'quit' to exit the application.
        transaction_input = input(
            "\nEnter a transaction (amount,category) or 'quit' to exit: ")

        # Check if the user wants to exit the application.
        if transaction_input.lower() == 'quit':
            # Print all unique categories added during the current session before exiting.
            if current_session_categories:  # Check if the set is not empty
                print("Categories added in this session:",
                      ", ".join(sorted(current_session_categories)))
            else:
                print("No categories were added in this session.")
            break
        # Validate the format of the user's transaction input.
        if not validate_transaction_input(transaction_input):
            print("Invalid input format. Please use 'amount,category'.")
            continue

        # Attempt to parse the transaction amount and category from the user's input.
        try:
            amount, category = transaction_input.split(',')
            # Convert the amount to a float for numerical operations.
            amount = float(amount)
            # Trim any leading/trailing whitespace from the category.
            category = category.strip()
        except ValueError:
            # Handle cases where the input cannot be properly parsed.
            print(
                "Error processing your input. Please ensure it's in 'amount,category' format.")
            continue

        # Add the parsed transaction to the budget and track the category.
        budget.add_transaction(amount, category)
        # Track the category in the session set.
        current_session_categories.add(category)

        # Print the updated budget balance and the total for the transaction's category.
        print(
            f"New balance for the month: {budget.get_balance()}. Updated category total for '{category}': {budget.get_category_total(category)}")
        # Display the total number of transactions recorded during the current session.
        print(f"Total transactions recorded this session: {len(budget)}")

    # After exiting the input loop, save the current state of the budget to a file.
    save_current_state(transactions_file, budget)
    # Confirm to the user that the current state has been saved.
    print("Current state saved. Exiting application.")
