
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Cancer_Pulmon.csv')

# Figura con subgráfica
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Boxplot de edad
sns.boxplot(ax=axs[0, 0], x=df['age'], color='skyblue')
axs[0, 0].set_title('Edad de los Pacientes con Cáncer de Pulmón', fontsize=16, fontweight='bold')
axs[0, 0].set_xlabel('Edad', fontsize=12)

# Boxplot de colesterol
sns.boxplot(ax=axs[0, 1], x=df['cholesterol_level'], color='lightcoral')
axs[1, 0].set_title('Niveles de Colesterol de los Pacientes', fontsize=16, fontweight='bold')
axs[1, 0].set_xlabel('Nivel de Colesterol', fontsize=12)

# Boxplot de BMI
sns.boxplot(ax=axs[1, 0], x=df['bmi'], color='lightgreen')
axs[0, 1].set_title('BMI de los Pacientes con Cáncer de Pulmón', fontsize=16, fontweight='bold')
axs[0, 1].set_xlabel('Índice de Masa Corporal (BMI)', fontsize=12)

# Ocultamos el gráfico adicional en la esquina inferior derecha
fig.delaxes(axs[1, 1])

plt.tight_layout()
plt.show()
