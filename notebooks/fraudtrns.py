import pandas as pd
# Загрузка данных
df = pd.read_csv("C:/Users/ghsh/bank_transactions_analysis/data/bank_transactions.csv")

# 1. Поиск крупных транзакций (сумма > 1000)
large_transactions = df[df['amount'].abs() > 1000]

# 2. Частые транзакции: сортируем по дате и считаем количество транзакций за день
df['date'] = pd.to_datetime(df['date'])
df['transaction_count_per_day'] = df.groupby('date')['transaction_id'].transform('count')

# 3. Подозрительные категории: фильтруем на случайные категории, если такие будут
suspicious_categories = ["Freelance", "Loan", "Unusual Category"]
suspicious_transactions = df[df['category'].isin(suspicious_categories)]

# Выводим результаты
print("Подозрительные транзакции (сумма > 1000):")
print(large_transactions)

print("\nТранзакции с частотой больше 5 за день:")
print(df[df['transaction_count_per_day'] > 5])

print("\nПодозрительные категории транзакций:")
print(suspicious_transactions)
