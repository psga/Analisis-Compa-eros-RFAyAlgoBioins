import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer los datos
data = '''Nombre,Carrera,Semestre,Intereses,Género'''  # Aquí iría todo el conjunto de datos

# Convertir el string a DataFrame usando StringIO
from io import StringIO
df = pd.read_csv(StringIO(data))

# Configurar el estilo de las gráficas
plt.style.use('seaborn')
sns.set_palette("husl")

# Crear una figura con múltiples subplots
fig = plt.figure(figsize=(20, 15))

# 1. Gráfico de barras apiladas
plt.subplot(2, 2, 1)
df_counts = pd.crosstab(df['Carrera'], df['Género'])
df_counts.plot(kind='bar', stacked=True)
plt.title('Distribución de Género por Carrera (Barras Apiladas)')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Género')
plt.tight_layout()

# 2. Gráfico de barras agrupadas
plt.subplot(2, 2, 2)
df_counts.plot(kind='bar')
plt.title('Distribución de Género por Carrera (Barras Agrupadas)')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Género')
plt.tight_layout()

# 3. Gráfico circular para proporción general de géneros
plt.subplot(2, 2, 3)
df['Género'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Proporción General de Géneros')

# 4. Gráfico de porcentajes normalizados
plt.subplot(2, 2, 4)
df_normalized = df_counts.div(df_counts.sum(axis=1), axis=0) * 100
df_normalized.plot(kind='bar', stacked=True)
plt.title('Distribución Porcentual de Género por Carrera')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Género')
plt.ylabel('Porcentaje')
plt.tight_layout()

# Ajustar el layout general
plt.tight_layout(pad=3.0)

# Mostrar las gráficas
plt.show()

# Imprimir un resumen estadístico
print("\nResumen estadístico:")
print("\nTotal de estudiantes por carrera:")
print(df['Carrera'].value_counts())
print("\nTotal de estudiantes por género:")
print(df['Género'].value_counts())
print("\nPorcentaje de género por carrera:")
print(df_normalized.round(2))
