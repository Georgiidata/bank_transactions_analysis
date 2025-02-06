import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Загрузка данных
df = pd.read_csv("C:/Users/ghsh/bank_transactions_analysis/data/bank_transactions.csv")
plt.figure(figsize=(12, 6))
sns.boxplot(x=df["amount"], color="red")
plt.title("🔎 Выявление аномальных транзакций (выбросы)")
plt.xlabel("Сумма транзакции")
plt.show()
