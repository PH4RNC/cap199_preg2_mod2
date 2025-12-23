
# Solucion

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Cancer_Pulmon.csv')
fig, axes = plt.subplots(2, 2, figsize=(20, 12))
fig.suptitle('Cancer', fontsize=16, fontweight='bold')

# Histograma de la columna/variable : age
axes[0, 0].hist(df['age'], bins=5, color='skyblue', edgecolor='black')  # Sin línea de campana y 3 barras
axes[0, 0].set_title('Distribución de la Edad', fontsize=14)
axes[0, 0].set_xlabel('Edad', fontsize=12)
axes[0, 0].set_ylabel('Frecuencia', fontsize=12)
axes[0, 0].grid()

# Diagrama de tipo pie de la variable/columna : gender
gender_counts = df['gender'].value_counts()
colors = ['#1f77b4', '#ff7f0e']
axes[0, 1].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)  # Startangle para línea vertical
axes[0, 1].set_title('Distribución del género', fontsize=14)

# Distribución de países (Columna : country) en un diagrama de barras
country_counts = df['country'].value_counts()
axes[1, 0].bar(country_counts.index, country_counts.values, color='#f08080', edgecolor='none')  # Color rosado
axes[1, 0].set_title('Pacientes por país', fontsize=14)
axes[1, 0].set_ylabel('Número de Pacientes', fontsize=12)
axes[1, 0].tick_params(axis='x', rotation=90)

# Distribución de la etapa del cáncer (columna cancer_stage) en un diagrama de barras
stage_counts = df['cancer_stage'].value_counts()
axes[1, 1].bar(stage_counts.index, stage_counts.values, color='lightgreen', edgecolor='none')  # Color verde claro
axes[1, 1].set_title('Distribución de la etapa del cáncer', fontsize=14)
axes[1, 1].set_ylabel('Número de Observaciones', fontsize=12)

plt.show()
