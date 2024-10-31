import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
# Leer los datos
data = '''Nombre,Carrera,Semestre,Intereses,Género
xxx
'''  # Aquí iría todo el conjunto de datos
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# Convertir el string a DataFrame
df = pd.read_csv(StringIO(data))

# Procesar los intereses (separar intereses múltiples)
def split_interests(interest):
    # Eliminar texto entre paréntesis y dividir por "y" o ","
    cleaned = interest.split('(')[0].strip()
    interests = [i.strip() for i in cleaned.replace(' y ', ',').split(',')]
    return interests

# Expandir los intereses en múltiples filas
df_expanded = df.assign(Intereses=df['Intereses'].apply(split_interests)).explode('Intereses')

# Configurar el estilo
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = (20, 25)
plt.rcParams['font.size'] = 8

# Crear subplots
fig = plt.figure()
gs = fig.add_gridspec(3, 2, hspace=0.4)

# 1. Gráfico de barras horizontales - Intereses por Género
ax1 = fig.add_subplot(gs[0, 0])
interests_by_gender = pd.crosstab(df_expanded['Intereses'], df_expanded['Género'])
interests_by_gender.plot(kind='barh', ax=ax1)
ax1.set_title('Distribución de Intereses por Género')
ax1.set_xlabel('Cantidad de Estudiantes')

# 2. Gráfico de barras apiladas - Intereses por Programa
ax2 = fig.add_subplot(gs[0, 1])
interests_by_program = pd.crosstab(df_expanded['Intereses'], df_expanded['Carrera'])
interests_by_program.plot(kind='bar', stacked=True, ax=ax2)
ax2.set_title('Distribución de Intereses por Programa')
plt.xticks(rotation=45, ha='right')
ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# 3. Heatmap - Intereses vs Programa
ax3 = fig.add_subplot(gs[1, :])
heatmap_data = pd.crosstab(df_expanded['Intereses'], df_expanded['Carrera'])
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlOrRd', ax=ax3)
ax3.set_title('Heatmap de Intereses vs Programa')
plt.xticks(rotation=45, ha='right')

# 4. Gráfico de burbujas - Intereses, Programa y Género
ax4 = fig.add_subplot(gs[2, :])
bubble_data = pd.crosstab([df_expanded['Intereses'], df_expanded['Carrera']], df_expanded['Género'])
bubble_data = bubble_data.reset_index()
bubble_data['Total'] = bubble_data['Femenino'] + bubble_data['Masculino']

for idx, row in bubble_data.iterrows():
    ax4.scatter(row['Carrera'], row['Intereses'], 
               s=row['Total']*100, 
               alpha=0.6,
               label=f"{row['Total']} estudiantes")

ax4.set_title('Gráfico de Burbujas - Intereses, Programa y Género')
plt.xticks(rotation=45, ha='right')

# Ajustar el layout
plt.tight_layout()

# Mostrar las gráficas
plt.show()

# Imprimir resumen estadístico
print("\nResumen de Intereses más populares por Género:")
print(interests_by_gender)

print("\nResumen de Intereses más populares por Programa:")
print(interests_by_program)

# Calcular y mostrar porcentajes
print("\nPorcentaje de Intereses por Género:")
print((interests_by_gender / interests_by_gender.sum() * 100).round(2))
