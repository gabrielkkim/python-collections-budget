
import collections
from . import Expense

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)
    
# Collections Counter that count how many purchases were in each category

spending_counter = collections.counter(spending_categories)
print(spending_counter)
