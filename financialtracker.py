import json

class Category:
    # Initialize category with name and budget
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.expenses = []

    # Add an expense to the category
    def add_expense(self, amount):
        self.expenses.append(amount)

    # Calculate total expenses for the category
    def get_total_expenses(self):
        return sum(self.expenses)


class FinancialTracker:
    # Initialize the financial tracker and load saved data
    def __init__(self):
        self.categories = []
        self.load_data()

    # Add a new budget category and save data
    def add_category(self, name, budget):
        category = Category(name, budget)
        self.categories.append(category)
        self.save_data()

    # Add an expense to a specified category and save data
    def add_expense(self, category_name, amount):
        for category in self.categories:
            if category.name == category_name:
                category.add_expense(amount)
                self.save_data()
                return
        print(f"Category '{category_name}' not found.")

    # Interactive method to add a category based on user input
    def add_user_category(self):
        name = input("Enter the category name: ")
        budget = float(input(f"Enter the budget for {name}: "))
        self.add_category(name, budget)

    # Interactive method to add an expense based on user input
    def add_user_expense(self):
        category_name = input("Enter the category for the expense: ")
        amount = float(input("Enter the expense amount: "))
        self.add_expense(category_name, amount)

    # Display all categories with their budget and expenses
    def display_categories(self):
        for category in self.categories:
            print(f"\nCategory: {category.name}")
            print(f"Budget: {category.budget}")
            print("Expenses:")
            for expense in category.expenses:
                print(f" - {expense}")
            print("----------")

    # Check each category's budget against its expenses
    def check_budgets(self):
        for category in self.categories:
            total_expense = category.get_total_expenses()
            if total_expense > category.budget:
                print(f"Alert: Budget exceeded for {category.name}! (Spent: {total_expense}, Budget: {category.budget})")

    # Save current state of categories to a file
    def save_data(self):
        data = [{'name': cat.name, 'budget': cat.budget, 'expenses': cat.expenses} for cat in self.categories]
        with open('financial_data.json', 'w') as file:
            json.dump(data, file)

    # Load saved category data from a file
    def load_data(self):
        try:
            with open('financial_data.json', 'r') as file:
                data = json.load(file)
                for cat_data in data:
                    category = Category(cat_data['name'], cat_data['budget'])
                    category.expenses = cat_data['expenses']
                    self.categories.append(category)
        except FileNotFoundError:
            pass  # File doesn't exist, start with empty categories

def main():
    # Create an instance of FinancialTracker and interact with the user
    tracker = FinancialTracker()
    while True:
        # User interface menu
        print("\nFinancial Tracker")
        print("1. Add Category")
        print("2. Add Expense")
        print("3. Display Categories")
        print("4. Check Budgets")
        print("5. Exit")
        choice = input("Enter your choice: ")

        # Handling the user's choice
        if choice == "1":
            tracker.add_user_category()
        elif choice == "2":
            tracker.add_user_expense()
        elif choice == "3":
            tracker.display_categories()
        elif choice == "4":
            tracker.check_budgets()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
