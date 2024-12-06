import csv  # For reading and writing csv files
import os #  For file handling
from datetime import datetime # For working with dates

def setup_csv(file_name="expenses.csv"):
    """
    Checks if the CSV file exists. If not, creates it with the appropriate headers.

    Args:
        file_name (str, optional): _description_. Defaults to "expenses.csv".
    """
    if not os.path.exists(file_name):
        # Create the file and write headers
        with open(file_name, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
        print(f"{file_name} created successfully!")
    else:
        print(f"{file_name} already exists.")
        
def add_expense(file_name="expenses.csv"):
    """
    Adds a new expense to the csv file.

    Args:
        file_name (str, optional): _description_. Defaults to "expenses.csv".
    """
    try:
        date = input("Enter the date (YYYY-MM-DD): ")
        datetime.strptime(date, "%Y-%m-%d")
        
        category = input("Enter the category (e.g. Food, Transport): ").strip()
        amount = float(input("Enter the amount: ")) # Ensure it's a number
        description = input("Enter the description (optional): ").strip()
        
        # Append the csv
        with open(file_name, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])
            print("Expense added successfully!")
    except ValueError as e:
        print(f"Error: {e}. Please enter the details in the correct format.")
        
def view_expense(file_name="expenses.csv"):
    """
    Reads and displays the expenses from the CSV file in a table format.
    """
    if not os.path.exists(file_name):
        print("No expense file found. Please add an expense first.")
        return
    
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        expenses = list(reader)
        
        if len(expenses) <= 1:
            print("No expenses recorded yet.")
            return
        
        # Print header
        print(f"{'Date':<15} {'Category':<15} {'Amount':<10} {'Description':<30}")
        print("_" * 70)
        
        # Print each expense
        for row in expenses[1:]:
            print(f"{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<30}")
        
if __name__ == "__main__":
    setup_csv()
    add_expense()
    print("\nYour recorded expenses:")
    view_expense()