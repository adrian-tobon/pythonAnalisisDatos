import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


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
'''
plt.figure(figsize=(6,3))
plt.bar(df_stacked['Category'],df_stacked['Group 1'],label = 'Group 1',color='lightblue')
plt.bar(df_stacked['Category'],df_stacked['Group 2'],bottom=df_stacked['Group 1'],label = 'Group 2',color='lightcoral')
plt.title('Stacked Bar chart - Matplotlib')
plt.xlabel('Category')
plt.ylabel('Values')
plt.grid(True,axis='both',linestyle='--',alpha=0.5)
plt.legend()
plt.show()
'''

#grafico de barras agrupado
'''
plt.figure(figsize=(6,3))
width = 0.3

categories = df_stacked['Category']
index = range(len(categories))

plt.bar([i - width/2 for i in index],df_stacked['Group 1'],width=width,label = 'Group 1',color='lightblue')
plt.bar([i + width/2 for i in index],df_stacked['Group 2'],width=width,label = 'Group 2',color='lightcoral')

plt.title('Gruped Bar chart')
plt.xlabel('Category')
plt.ylabel('Values')

plt.xticks(index,categories)
plt.legend()
plt.grid(True,axis='both',linestyle='--',alpha=0.5)
plt.show()
'''

#grafico de barras personalizado
'''
plt.figure(figsize=(4, 3))
plt.bar(df['Category'], df['Values'], color='cornflowerblue', edgecolor='black', linewidth=2, alpha=0.8)
plt.title('Customized Bar Chart')
plt.xlabel('Category')
plt.ylabel('Values')
plt.xticks(rotation=45, fontsize=12)
plt.yticks(rotation=45, fontsize=12)
plt.grid(True, axis='both', linestyle='--', alpha=0.5)
plt.show()
'''

#grafico de lineas
data3 = {'Month':['Jan','Feb','Mar','Apr','May','Jun'],
         'Sales':[250,300,400,350,450,500]}

df3 = pd.DataFrame(data3)

print(df3)

#mathplotlib
'''
plt.figure(figsize=(6,3))
plt.plot(df3['Month'],df3['Sales'],color='darkblue',marker='o')
plt.title('Line chart - Mathplotlib ')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True,axis='both',linestyle='--',alpha=0.5)
plt.legend()
plt.show()
'''
#seaborn
'''
sns.set_style("whitegrid")

plt.figure(figsize=(6,3))
#sns.lineplot(x=df3['Month'],y=df3['Sales'],color='darkblue')
sns.lineplot(x='Month',y='Sales',color='darkblue',data=df3,marker='o',color='red')
plt.title('Line chart - Seaborn ')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True,axis='both',linestyle='--',alpha=0.5)
plt.legend()
plt.show()
'''

#multiples lineas
data_multi = {'Month':['Jan','Feb','Mar','Apr','May','Jun'],
         'Sales A':[250,300,400,350,450,500],
         'Sales B':[200,250,300,280,320,400]}

df_multi = pd.DataFrame(data_multi)
print(df_multi)

#matplotlib
'''
plt.figure(figsize=(6,3))
plt.plot(df_multi['Month'],df_multi['Sales A'],color='darkblue',marker='o',label='Product A')
plt.plot(df_multi['Month'],df_multi['Sales B'],color='red',marker='D',label='Product A')
plt.title('Multiple Line chart - Mathplotlib ')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True,axis='both',linestyle='--',alpha=0.5)
plt.legend()
plt.show()
'''
#seaborn
'''
plt.figure(figsize=(6,3))
sns.lineplot(x=df_multi['Month'],y=df_multi['Sales A'],color='darkblue',marker='o',label='Product A')
sns.lineplot(x=df_multi['Month'],y=df_multi['Sales B'],color='red',marker='D',label='Product A')
plt.title('Multiple Line chart - Seaborn ')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True,axis='both',linestyle='--',alpha=0.5)
plt.legend()
plt.show()
'''

#grafico de lineas con intervalos de confianza
'''
df_long = pd.melt(df_multi,id_vars=['Month'],value_vars=['Sales A','Sales B'],var_name='Product',value_name='Sales')
print(df_long)

plt.figure(figsize=(6,3))
sns.lineplot(x=df_long['Month'],y=df_long['Sales'],hue=df_long['Product'],color='darkblue',marker='o',errorbar='sd')
plt.title('Line chart with confidence interval - Seaborn ')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
'''

# Crear un DataFrame con múltiples observaciones por cada mes y producto
'''
np.random.seed(42)  # Para reproducibilidad
data_multi_random = {'Month': ['Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb', 'Mar', 'Mar', 'Mar', 
                               'Apr', 'Apr', 'Apr', 'May', 'May', 'May', 'Jun', 'Jun', 'Jun'],
                     'Product': ['Product A', 'Product A', 'Product A', 'Product A', 'Product A', 'Product A', 
                                 'Product A', 'Product A', 'Product A', 'Product A', 'Product A', 'Product A', 
                                 'Product A', 'Product A', 'Product A', 'Product A', 'Product A', 'Product A'],
                     'Sales': [250, 260, 240, 300, 310, 290, 400, 410, 390, 350, 360, 340, 450, 460, 440, 500, 510, 490]}

df_multi_random = pd.DataFrame(data_multi_random)

print(df_multi_random)

# Añadir una pequeña variabilidad a las ventas de 'Product B'
data_multi_random_b = {'Month': ['Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb', 'Mar', 'Mar', 'Mar', 
                               'Apr', 'Apr', 'Apr', 'May', 'May', 'May', 'Jun', 'Jun', 'Jun'],
                     'Product': ['Product B', 'Product B', 'Product B', 'Product B', 'Product B', 'Product B', 
                                 'Product B', 'Product B', 'Product B', 'Product B', 'Product B', 'Product B', 
                                 'Product B', 'Product B', 'Product B', 'Product B', 'Product B', 'Product B'],
                     'Sales': [200, 210, 190, 250, 260, 240, 300, 310, 290, 280, 290, 270, 320, 330, 310, 400, 410, 390]}

df_multi_random_b = pd.DataFrame(data_multi_random_b)

# Concatenar ambos productos
df_random = pd.concat([df_multi_random, df_multi_random_b])

# Graficar con Seaborn mostrando el intervalo de confianza
plt.figure(figsize=(4, 3))
sns.lineplot(x='Month', y='Sales', hue='Product', data=df_random, marker='o', errorbar='sd')
plt.title('Line Chart with Confidence Interval - Seaborn')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
'''

#graficos de dispersion

data4 = {'Height': [150, 160, 165, 170, 175, 180, 185, 190],
        'Weight': [50, 55, 60, 65, 70, 75, 80, 85]}
df4 = pd.DataFrame(data4)
print(df4)

#matplotlib
'''
plt.figure(figsize=(4, 3))
plt.scatter(df4['Height'], df4['Weight'], marker='o', color='red')
plt.title('Scatter chart - Mathplotlib')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.grid(True,axis='both',linestyle='--',alpha=0.5)
plt.show()
'''
#seaborn
df4['Category'] = ['Group 1', 'Group 1', 'Group 2', 'Group 2', 'Group 1', 'Group 2', 'Group 1', 'Group 2']
'''
sns.set_style("whitegrid")
sns.set_palette("muted")

plt.figure(figsize=(4, 3))
#sns.scatterplot(x=df4['Height'], y=df4['Weight'],hue=df4['Category'], marker='o', color='red')
sns.regplot(x=df4['Height'], y=df4['Weight'],scatter_kws={'s':50}, line_kws={'color':'red'})
plt.title('Scatter chart - Seaborn')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()
'''
#tamaño variable (Bubble plot)
df4['Income'] = [80000, 32000, 35000, 40000, 45000, 48000, 52000, 60000]
'''
plt.figure(figsize=(4, 3))
plt.scatter(df4['Height'], df4['Weight'],s=df4['Income']*0.001,alpha=0.6,edgecolor='w',linewidth=2, color='red')
plt.title('Bubble plot chart - Mathplotlib')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.grid(True,axis='both',linestyle='--',alpha=0.5)
plt.show()
'''

#graficos de dispersion con multiples series
data_multi2 = {'Height': [150, 160, 165, 170, 175, 180, 185, 190],
              'Weight_A': [50, 55, 60, 65, 70, 75, 80, 85],
              'Weight_B': [48, 53, 58, 63, 68, 73, 78, 83]}
df_multi2 = pd.DataFrame(data_multi2)
print(df_multi2)

#matplotlib
'''
plt.figure(figsize=(4, 3))
plt.scatter(df_multi2['Height'], df_multi2['Weight_A'], color='red',label="Group A")
plt.scatter(df_multi2['Height'], df_multi2['Weight_B'], color='blue',label="Group B")
plt.title('Bubble plot chart - Mathplotlib')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.grid(True,axis='both',linestyle='--',alpha=0.5)
plt.legend()
plt.show()
'''
#seaborn
'''
plt.figure(figsize=(4, 3))
sns.scatterplot(x=df_multi2['Height'], y=df_multi2['Weight_A'], color='red',label="Group A")
sns.scatterplot(x=df_multi2['Height'], y=df_multi2['Weight_B'], color='blue',label="Group B")
plt.title('Bubble plot chart - Seaborn')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.grid(True,axis='both',linestyle='--',alpha=0.5)
plt.legend()
plt.show()
'''


#matrice de correlacion

data5 = {'Height': [150, 160, 165, 170, 175, 180, 185, 190],
        'Weight': [50, 55, 60, 65, 70, 75, 80, 85],
        'Income': [30000, 32000, 35000, 40000, 45000, 48000, 52000, 60000]}
df5 = pd.DataFrame(data5)
correlation_matrix = df5.corr()
print(correlation_matrix)

mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
#mask = np.tril(np.ones_like(correlation_matrix, dtype=bool))

plt.figure(figsize=(4, 3))
sns.heatmap(correlation_matrix,annot=True,cmap='coolwarm',mask=mask,linewidth=0.5)
plt.title('Heat Map - Seaborn')
plt.show()