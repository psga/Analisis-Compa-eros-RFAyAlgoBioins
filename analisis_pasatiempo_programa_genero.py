import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
# Leer los datos
data = '''Nombre,Carrera,Semestre,Intereses,Género
Alejandro Giraldo Sarria,Ingeniería de control,10,Videojuegos,Masculino
Sebastian Arango,Ingeniería de Sistemas e Informática,8,Videojuegos,Masculino
Natalia Andrea Álvarez Hoyos,Ingeniería de Sistemas e Informática,10,Dibujar,Femenino
Julián Castaño Pineda,Estadística,8,Trotar,Masculino
Alejandra Rios Salgado,Estadística,10,Bailar,Femenino
Alejandro Orozco Ochoa,Ingeniería de Sistemas e Informática,9,Música,Masculino
Juan Pablo Gómez Reyes,Ingeniería de Sistemas e Informática,9,Videojuegos,Masculino
Santiago Varela Vanegas,Ingeniería de Sistemas e Informática,10,Videojuegos,Masculino
Hugo Andrés Mazo Pacheco,Ingeniería de Sistemas e Informática,13,Aprender herramientas de software y videojuegos,Masculino
Andrés Alexis Galvis Herrera,Ingeniería de Sistemas e Informática,9,Lectura,Masculino
Verónica Pérez Zea,Ingeniería de Sistemas e Informática,10,Bailar y Cine,Femenino
Valentina Ospina Narváez,Ingeniería de Sistemas e Informática,10,Bailar,Femenino
Alejandra Uribe Sierra,Ingeniería de Sistemas e Informática,10,Leer y bailar,Femenino
Juan Esteban Quiroz Taborda,Ingeniería de Sistemas e Informática,10,Senderismo,Masculino
Andres Felipe Callejas Ruiz,Ingeniería de Sistemas e Informática,8,Ilustración digital,Masculino
Stefany Cantero Cárdenas,Ingeniería de Sistemas e Informática,10,Leer,Femenino
Felipe Muñoz Echeverri,Ingeniería de Sistemas e Informática,8,Cine,Masculino
Juan Manuel Vera Echeverri,Ingeniería de Sistemas e Informática,10,Videojuegos y Cine,Masculino
Hernan Dario Tapias Martinez,Ingeniería de control,3,Aeromodelismo,Masculino
Mateo Arenas Montoya,Ingeniería física,10,Correr por montaña,Masculino
Juan Felipe López Ramírez,Ingeniería de Sistemas e Informática,10,Música,Masculino
Jeronimo Ledesma Patiño,Ingeniería de Sistemas e Informática,8,Música,Masculino
Maria Camila Zapata Arrubla,Ingeniería de Sistemas e Informática,9,Bailar y hacer ejercicio,Femenino
Samuel Botero Rivera,Ingeniería física,8,Fotografía,Masculino
Juan José Tobón Zapata,Ingeniería de Sistemas e Informática,9,Música,Masculino
Pablo Andres Usuga,Ciencias De la Computación,8,Música,Masculino
Julian David Diaz Jaramillo,Ingeniería de Sistemas e Informática,8,Videojuegos,Masculino
Tomás Rodríguez Taborda,Ingeniería de Sistemas e Informática,8,Cine,Masculino
Maria Del Pilar Mira Londoño,Estadística,11,Gimnasia,Femenino
Catalina Restrepo Salgado,Ingeniería de Sistemas e Informática,8,Programación competitiva,Femenino
Camilo Andrés Espíndola Aldana,Ingeniería de Sistemas e Informática,8,Música,Masculino
Luis José Mejía Restrepo,Ingeniería de Sistemas e Informática,8,Leer,Masculino
Miguel Fernando Olave Riascos,Ingeniería de Sistemas e Informática,8,Jugar baloncesto,Masculino
Luis Andrés Altamar Romero,Ingeniería de Sistemas e Informática,8,Senderismo,Masculino
Sebastián Aguinaga Velásquez,Ingeniería de Sistemas e Informática,9,Videojuegos,Masculino
Juan Esteban Cadavid Arango,Ingeniería de Sistemas e Informática,8,Videojuegos,Masculino
Carlos Sebastián Zamora Rosero,Ingeniería de Sistemas e Informática,10,Bailar,Masculino
José Daniel Londoño Londoño,Ingeniería de Sistemas e Informática,8,Historia,Masculino
Julián Orrego Martínez,Ingeniería de Sistemas e Informática,10,Películas,Masculino
Juan Pablo Pineda Lopera,Ingeniería de Sistemas e Informática,8,Música,Masculino
Paula Kern,Informática,5,Senderismo,Femenino
Juan José Zapata Cadavid,Ingeniería de Sistemas e Informática,9,Videojuegos,Masculino
Carolina Alvarez Murillo,Ingeniería de Sistemas e Informática,8,Leer,Femenino
Juan Carlos Múnera Arango,Ingeniería de Sistemas e Informática,10,Senderismo,Masculino
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
