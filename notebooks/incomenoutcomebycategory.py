import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Загрузка данных
df = pd.read_csv("C:/Users/ghsh/bank_transactions_analysis/data/bank_transactions.csv")
# Настройки графиков
plt.style.use("ggplot")

# Группируем суммы по категориям
category_totals = df.groupby("category")["amount"].sum().sort_values()

# Столбчатая диаграмма расходов по категориям
plt.figure(figsize=(12, 6))
category_totals.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("📊 Расходы и доходы по категориям")
plt.xlabel("Категория")
plt.ylabel("Сумма")
plt.xticks(rotation=45)
plt.show()
