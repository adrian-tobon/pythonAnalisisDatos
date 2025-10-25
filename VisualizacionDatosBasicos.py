import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


##########Visualizacion de datos basicos##########
''' Principios Clave para una Buena Visualización
   
Antes de entrar en detalles técnicos, es importante destacar algunos principios generales que guiarán todas las visualizaciones que se realicen:

- **Claridad y Simplicidad:** La visualización debe ser clara y fácil de entender. No sobrecargues el gráfico con demasiada información innecesaria.
- **Enfocar en lo Importante:** El gráfico debe destacar la información más relevante para el análisis. Usa colores, tamaños y otras características visuales para dirigir la atención del espectador.
- **Consistencia:** Asegúrate de que los gráficos mantengan un estilo consistente. Si estás usando una paleta de colores, mantén los mismos colores para las mismas categorías en diferentes gráficos.
- **Títulos y Etiquetas:** Un gráfico debe tener un título claro, etiquetas en los ejes, y si es necesario, una leyenda que explique los datos.
- **Simplicidad en el Diseño:** Evita elementos distractores como decoraciones excesivas, fondos complejos o colores que dificulten la lectura.

## Construcción de Gráficos en Python

Para crear gráficos en Python, las bibliotecas más comunes son Matplotlib y Seaborn. Ambas nos permitirán crear gráficos efectivos y bien diseñados.

### Matplotlib:
Es la biblioteca más básica para crear gráficos en Python. Ofrece mucho control sobre los elementos visuales del gráfico.
### Seaborn:
Seaborn está construido sobre Matplotlib y hace más fácil la creación de gráficos complejos con una sintaxis más sencilla. Además, tiene configuraciones estéticas predefinidas para hacer los gráficos más bonitos por defecto.
'''

data = {'Category' : ['A','B','C'],'Values':[10,20,15]}
df = pd.DataFrame(data)

#matplotlib
'''
plt.figure(figsize=(6,3))
plt.bar(df['Category'],df['Values'],color='skyblue')
plt.title('Bar chart - Matplotlib')
plt.xlabel('Category')
plt.ylabel('Values')
plt.grid(True,linestyle='--',alpha=0.7)
plt.show()
'''

#seaborn
'''
sns.set_style("whitegrid")
sns.set_palette("muted")

plt.figure(figsize=(6,3))
sns.barplot(x = df['Category'],y = df['Values'],color='skyblue')
plt.title('Bar chart - Seaborn')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()
'''
''' Elementos Clave para Personalizar Gráficos

- **Tamaño del gráfico:** Controlado por figsize en plt.figure().
- **Colores:** Puedes especificar colores usando el parámetro color en Matplotlib o con palette en Seaborn.
- **Título y etiquetas:** Usa plt.title(), plt.xlabel() y plt.ylabel() para describir el gráfico.
- **Leyenda:** Si el gráfico tiene varias series de datos, una leyenda puede ser útil para indicar qué representa cada línea o barra.
- **Cuadrícula (Grid):** Una cuadrícula ligera puede ayudar a la lectura de los gráficos. Usa plt.grid() para agregarla.

## Consejos de Estética

- **Usa colores suaves:** Paletas de colores como las de Seaborn ("muted", "pastel") o colores claros en Matplotlib (`'skyblue'`, `'lightcoral'`) son buenos para hacer gráficos agradables visualmente.
- **Evita el uso excesivo de decoraciones:** No sobrecargues el gráfico con demasiadas líneas, colores o efectos 3D.
- **Tamaño del texto:** Usa `plt.xticks()` o `plt.yticks()` para ajustar el tamaño del texto en los ejes si es necesario.

'''

data2 = {'Category' : ['A','B','C','D'],'Values':[25,40,35,30]}
df2 = pd.DataFrame(data2)
print(df2)

#grafico de barras

#matplotlib
'''
plt.figure(figsize=(6,3))
plt.bar(df2['Category'],df2['Values'],color='lightblue')
#plt.barh(df2['Category'],df2['Values'],color='lightblue')
plt.title('Basic Bar chart - Matplotlib')
plt.xlabel('Category')
plt.ylabel('Values')
plt.grid(True,axis='y',linestyle='--',alpha=0.5)
plt.show()
'''

#seaborn
'''
sns.set_style("whitegrid")
sns.set_palette("pastel")

plt.figure(figsize=(6,3))
sns.barplot(x = 'Category',y = 'Values',color='skyblue',data=df2)
plt.title('Basic Bar chart - Seaborn')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()
'''
#datos apilados
data_stacked = {'Category' : ['A','B','C','D'],'Group 1':[25,40,35,30],'Group 2':[15,25,20,25]}
df_stacked = pd.DataFrame(data_stacked)

print(df_stacked)

#matplotlib

plt.figure(figsize=(6,3))
plt.bar(df_stacked['Category'],df_stacked['Group 1'],label = 'Group 1',color='lightblue')
plt.bar(df_stacked['Category'],df_stacked['Group 2'],bottom=df_stacked['Group 1'],label = 'Group 2',color='lightcoral')
plt.title('Basic Bar chart - Matplotlib')
plt.xlabel('Category')
plt.ylabel('Values')
plt.grid(True,axis='both',linestyle='--',alpha=0.5)
plt.legend()
plt.show()


#seaborn
'''
sns.set_style("whitegrid")
sns.set_palette("pastel")

plt.figure(figsize=(6,3))
sns.barplot(x = 'Category',y = 'Values',color='skyblue',data=df2)
plt.title('Basic Bar chart - Seaborn')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()
'''