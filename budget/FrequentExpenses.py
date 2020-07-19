import matplotlib.pyplot as plt
import collections
from . import Expense

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

# Collections Counter that count how many purchases were in each category

spending_counter = collections.Counter(spending_categories)
print(spending_counter)

top5 = spending_counter.most_common(5)
categories, count = zip(*top5)

fig, ax = plt.subplots()
ax.bar(categories, count) #, color=[numpy.ramdom.rand(3,) for _ in range(5) ]
