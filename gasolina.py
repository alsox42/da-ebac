import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("gasolina.csv")

sns.lineplot(x="dia", y="venda", data=df)

plt.xlabel("Dia")
plt.ylabel("Preço")
plt.title("Gráfico de Preço da Gasolina")

plt.savefig("gasolina.png")