import pandas as pd
import random
from datetime import datetime, timedelta

# Генерация случайных транзакций
def generate_transactions(n=100):
    categories = ["Grocery", "Transport", "Shopping", "Entertainment", "Rent", "Salary", "Freelance", "Bills"]
    transaction_types = {"Grocery": "Expense", "Transport": "Expense", "Shopping": "Expense",
                         "Entertainment": "Expense", "Rent": "Expense", "Bills": "Expense",
                         "Salary": "Income", "Freelance": "Income"}

    transactions = []
    balance = 2000  # Начальный баланс

    for i in range(n):
        date = (datetime(2024, 1, 1) + timedelta(days=i)).strftime('%Y-%m-%d')
        category = random.choice(categories)
        amount = round(random.uniform(10, 500), 2) if transaction_types[category] == "Expense" else round(random.uniform(1000, 5000), 2)
        if transaction_types[category] == "Expense":
            amount = -amount
        balance += amount

        transactions.append([i + 1, date, amount, category, balance, transaction_types[category]])

    return pd.DataFrame(transactions, columns=["transaction_id", "date", "amount", "category", "balance_after", "transaction_type"])

# Создаём CSV
df = generate_transactions(100)
df.to_csv("../data/bank_transactions.csv", index=False)
print("✅ Файл bank_transactions.csv создан в папке data/")
