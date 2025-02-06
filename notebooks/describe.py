import pandas as pd

# Загрузка данных
df = pd.read_csv("C:/Users/ghsh/bank_transactions_analysis/data/bank_transactions.csv")

# Основная статистика
print("Основная статистика:")
print(df.describe())

# Число транзакций по каждой категории
print("\nЧисло транзакций по категориям:")
print(df['category'].value_counts())

# Средняя сумма по типу транзакции (Expense vs Income)
print("\nСредняя сумма по типу транзакции:")
print(df.groupby('transaction_type')['amount'].mean())

# Распределение баланса после транзакций
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hist(df['balance_after'], bins=30, color='skyblue', edgecolor='black')
plt.title("Распределение баланса после транзакций")
plt.xlabel("Баланс после транзакции")
plt.ylabel("Частота")
plt.show()
