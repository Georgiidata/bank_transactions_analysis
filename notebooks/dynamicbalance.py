import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Загрузка данных
df = pd.read_csv("C:/Users/ghsh/bank_transactions_analysis/data/bank_transactions.csv")
plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["balance_after"], marker="o", linestyle="-", color="blue")
plt.title("📅 Динамика баланса со временем")
plt.xlabel("Дата")
plt.ylabel("Баланс")
plt.xticks(rotation=45)
plt.grid()
plt.show()
