import pandas as pd
import matplotlib.pyplot as plt

# Dados simulados para o exemplo
dados = {
    "Configuração": ["10", "20", "30", "40", "50"],
    "Itens Produzidos": [100, 200, 300, 400, 500],
    "Itens Consumidos": [90, 180, 270, 360, 450],
}

df = pd.DataFrame(dados)
plt.plot(df["Configuração"], df["Itens Produzidos"], label="Produzidos")
plt.plot(df["Configuração"], df["Itens Consumidos"], label="Consumidos")
plt.xlabel("Capacidade do Buffer")
plt.ylabel("Itens")
plt.title("Produção e Consumo por Capacidade do Buffer")
plt.legend()
plt.show()
