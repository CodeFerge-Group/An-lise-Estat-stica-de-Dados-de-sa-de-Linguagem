import pandas as pd
import numpy as np

# 1. Carregar os dados
df = pd.read_csv('pacientes.csv')

# 2. Limpeza e Cálculos com NumPy
# Vamos calcular o IMC (Índice de Massa Corporal)
# Fórmula: peso / altura²
df['IMC'] = df['peso'] / np.power(df['altura'], 2)

# 3. Análise Estatística com Pandas
print("--- Estatísticas Gerais dos Pacientes ---")
print(df.describe()) # Mostra média, desvio padrão, min, max, etc.

# 4. Agrupamento Estratégico
# Ver a média de colesterol entre quem tem e não tem diabetes
media_colesterol = df.groupby('diabetes')['colesterol'].mean()
print("\n--- Média de Colesterol por Grupo ---")
print(media_colesterol)

# 5. Usando NumPy para uma condição lógica (Risco de Hipertensão)
# Se a pressão for > 130, marcar como 'Risco'
df['Status_Pressao'] = np.where(df['pressao_arterial'] > 130, 'Risco', 'Normal')

print("\n--- Dados Finais com Análise ---")
print(df[['nome', 'IMC', 'Status_Pressao']])


import seaborn as sns
import matplotlib.pyplot as plt

# 1. Definir um tema visual mais profissional
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# 2. Criar o gráfico com uma paleta de cores degradê (magma ou viridis)
# O parâmetro 'hue' atribui cores diferentes por nome
grafico = sns.barplot(x='nome', y='IMC', data=df, palette="magma", hue='nome', legend=False)

# 3. Adicionar uma linha de corte (IMC = 25 é o limite do peso normal)
# Isso agrega valor estatístico ao seu trabalho
plt.axhline(25, color='red', linestyle='--', label='Limite Saudável (25.0)')

# 4. Colocar os valores exatos em cima das barras (Data Labels)
for p in grafico.patches:
    grafico.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 9), 
                   textcoords = 'offset points',
                   fontsize=10, fontweight='bold')

# 5. Títulos e Legendas
plt.title('Análise de IMC por Paciente', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Paciente', fontsize=12)
plt.ylabel('Índice de Massa Corporal (IMC)', fontsize=12)
plt.legend(loc='upper right')

# Ajustar layout para não cortar os nomes
plt.tight_layout()
plt.show()

