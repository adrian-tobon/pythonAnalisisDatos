'''
### Conceptos Clave

Comencemos recordando algunos de los conceptos esenciales que vimos en este curso:

- **Carga y Preparación de Datos**: La primera etapa de cualquier proyecto de análisis de datos es la preparación. Aprendimos a importar datos desde diferentes fuentes, limpiarlos y prepararlos para el análisis. Este proceso es fundamental para evitar problemas de interpretación y asegurar que nuestras visualizaciones reflejen con precisión los datos.

- **Visualización de Datos Básica**: La elección correcta de gráficos es crucial. Usamos gráficos de barras para comparar categorías, gráficos de líneas para analizar tendencias y scatterplots para explorar relaciones entre variables. Cada gráfico tiene su propósito, y su efectividad depende de cómo se adapte al tipo de datos que queremos representar.

- **Análisis Avanzado de Datos**: Más allá de los gráficos básicos, profundizamos en técnicas avanzadas, como boxplots y gráficos de violín, que nos permiten ver la distribución y variabilidad de los datos, así como mapas de calor para visualizar relaciones en matrices de datos.

- **Dashboards Interactivos**: Por último, exploramos la creación de dashboards interactivos usando Streamlit y Dash. Estos paneles permiten que los usuarios interactúen directamente con los datos, cambiando parámetros y descubriendo patrones sin necesidad de modificar el código.

### Mejores Prácticas para Visualización de Datos

Pasemos ahora a algunas prácticas fundamentales que harán nuestras visualizaciones no solo más precisas, sino también más comprensibles y visualmente atractivas.

1. **Conoce a tu Audiencia**  
   El éxito de una visualización radica en su capacidad para comunicar información. Antes de elegir un gráfico o decidir el nivel de detalle, pregúntate: ¿Quién es la audiencia? Para un público general, es mejor simplificar los gráficos y enfocarse en los elementos principales. En cambio, si la audiencia tiene experiencia técnica, puedes incluir más detalles y elementos de análisis.

2. **Elige el Gráfico Correcto**

   No todos los gráficos son adecuados para todos los tipos de datos. Algunos ejemplos incluyen:

   - **Gráfico de barras**: Ideal para comparar valores de diferentes categorías.
   - **Gráfico de líneas**: Excelente para mostrar cómo cambian los datos a lo largo del tiempo.
   - **Scatterplot**: Útil para observar relaciones entre dos variables.
   - **Boxplot o Violin Plot**: Perfectos para analizar la distribución y variabilidad de los datos.

   Elegir el gráfico adecuado hará que el mensaje sea claro y preciso, facilitando la comprensión de la audiencia.

3. **Simplifica y Mantén el Enfoque en lo Importante**  
   Las visualizaciones claras y limpias son más fáciles de interpretar. Evita el uso de elementos decorativos que no aporten valor al análisis, como colores excesivamente brillantes o efectos 3D. En su lugar, asegúrate de que cada elemento en el gráfico tenga un propósito claro y ayude a enfocar la atención en lo más importante.

4. **Usa Colores con Intención**  
   Los colores pueden resaltar o distraer en una visualización. Usa colores fuertes para datos clave y tonos suaves para elementos de fondo. Para datos categóricos, mantén una paleta consistente, de modo que cada categoría tenga el mismo color en diferentes gráficos. También recuerda usar paletas de colores accesibles, evitando combinaciones que dificulten la lectura para personas con daltonismo.

5. **Anota y Etiqueta Claramente**  
   Una buena visualización debe contextualizarse con títulos y etiquetas claras. Incluye siempre un título descriptivo, etiquetas en los ejes y leyendas si el gráfico tiene varias categorías. Si es posible, añade anotaciones o comentarios sobre los puntos más relevantes del gráfico, ya que ayudan al espectador a entender rápidamente los hallazgos clave.

6. **Considera la Interactividad cuando sea Necesario**  
   Para análisis complejos o grandes conjuntos de datos, considera el uso de herramientas interactivas. Dashboards creados con Streamlit o Dash permiten al usuario filtrar y manipular los datos en tiempo real, descubriendo patrones y relaciones de manera más dinámica. La interactividad puede facilitar el análisis, especialmente cuando se necesitan múltiples vistas o cuando el usuario tiene preguntas específicas sobre los datos.

### Conclusión: Iteración y Mejora Continua

   - **Itera y Ajusta**: Cada visualización es una oportunidad para mejorar. Revisa y ajusta los gráficos, probando diferentes opciones hasta encontrar la más clara y precisa.
   - **Obtén Retroalimentación**: Muestra tus gráficos a colegas o usuarios para obtener opiniones. La perspectiva de otros puede revelar aspectos que no habías considerado.
   - **Mantente Actualizado**: La visualización de datos es un campo en constante evolución. Sigue experimentando con nuevas técnicas y herramientas, y no dejes de aprender.

'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import interact,widgets
import numpy as np

#carga de datos
data = pd.read_csv('pythonAnalisisDatos/co-emissions-per-capita.csv')
print(data)

#preparacion de datos - filtrado por paises de interes
countries = ['United States', 'China', 'India', 'United Kingdom', 'Mexico', 'Peru', 'Colombia']
filtered_data = data[data['Entity'].isin(countries)]

print(filtered_data)

#exploracion incial de los datos
print(f"{filtered_data['Year'].min()} - {filtered_data['Year'].max()}")
print(filtered_data.isnull().sum())

#grafico de datos

#Seaborn
'''
plt.figure(figsize=(12, 8))
sns.lineplot(x='Year', y='Annual CO₂ emissions (per capita)', hue='Entity', data=filtered_data)
plt.title('Emisiones de CO2 (per capita)')
plt.xlabel('Year')
plt.ylabel('Annual CO₂ emissions (per capita)')
plt.grid(True)
plt.legend(title='Pais')
plt.show()
'''

filtered_data['Decade'] = (filtered_data['Year'] // 10) * 10
print(filtered_data)

decade_data = filtered_data[filtered_data['Decade'] >= 1950]

decade_avg = decade_data.groupby(['Entity','Decade'])['Annual CO₂ emissions (per capita)'].mean().reset_index()
print(decade_avg)

'''
plt.figure(figsize=(12, 8))
sns.barplot(x='Decade', y='Annual CO₂ emissions (per capita)', hue='Entity', data=decade_avg)
plt.title('Emisiones de CO2 (per capita) por decadas')
plt.xlabel('Decada')
plt.ylabel('Annual CO₂ emissions (per capita)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(title='Pais')
plt.show()
'''

decades_1950_2020 = filtered_data[filtered_data['Decade'].isin([1950,2020])]
decades_1950_2020['Decade Label'] = decades_1950_2020['Decade'].astype(str)
print(decades_1950_2020)

all_decades_data = filtered_data[filtered_data['Decade'] >= 1950]
'''
plt.figure(figsize=(12, 8))
sns.boxplot(x='Decade', y='Annual CO₂ emissions (per capita)', data=all_decades_data)
#sns.violinplot(x='Decade', y='Annual CO₂ emissions (per capita)', data=all_decades_data)
#sns.boxplot(x='Decade Label', y='Annual CO₂ emissions (per capita)', data=decades_1950_2020)
#sns.violinplot(x='Decade Label', y='Annual CO₂ emissions (per capita)', data=decades_1950_2020)
plt.title('Emisiones de CO2 (per capita) por decadas de 1950 y 2020')
plt.xlabel('Decada')
plt.ylabel('Annual CO₂ emissions (per capita)')
plt.grid(True)
plt.show()
'''

pivot_data = filtered_data.pivot(index='Year',columns='Entity',values='Annual CO₂ emissions (per capita)')
print(pivot_data)

correlation_matrix = pivot_data.corr()
'''
plt.figure(figsize=(4, 3))
sns.heatmap(correlation_matrix,annot=True,cmap='coolwarm',linewidth=0.5)
plt.title('Correlacion Mapa de Calor')
plt.show()
'''

def scatter_plot_dynamic(country1,country2,trendline):
    if country1 == country2:
        print("Seleccione dos países diferentes para comparar.")
        return
    
    # Filtrar datos para los dos países seleccionados
    data1 = filtered_data[filtered_data['Entity'] == country1]
    data2 = filtered_data[filtered_data['Entity'] == country2]
    
    # Combinar datos en un solo DataFrame por año
    merged_data = data1[['Year', 'Annual CO₂ emissions (per capita)']].merge(
        data2[['Year', 'Annual CO₂ emissions (per capita)']],
        on='Year', suffixes=(f'_{country1}', f'_{country2}')
    )
    
    # Calcular el coeficiente de correlación
    correlation = merged_data[f'Annual CO₂ emissions (per capita)_{country1}'].corr(
        merged_data[f'Annual CO₂ emissions (per capita)_{country2}']
    )

    # Graficar el diagrama de dispersión
    plt.figure(figsize=(4, 3))
    sns.scatterplot(data=merged_data, 
                    x=f'Annual CO₂ emissions (per capita)_{country1}', 
                    y=f'Annual CO₂ emissions (per capita)_{country2}')
    
    plt.title(f"Relación entre Emisiones de CO₂ per cápita de {country1} y {country2}\nCoeficiente de Correlación: {correlation:.2f}")
    plt.xlabel(f"Emisiones de CO₂ per cápita - {country1}")
    plt.ylabel(f"Emisiones de CO₂ per cápita - {country2}")

    # Agregar línea de tendencia si se selecciona
    if trendline:
        # Calcular la línea de tendencia
        x = merged_data[f'Annual CO₂ emissions (per capita)_{country1}']
        y = merged_data[f'Annual CO₂ emissions (per capita)_{country2}']
        m, b = np.polyfit(x, y, 1)
        plt.plot(x, m * x + b, color="red", linestyle="--", label=f"Tendencia (y = {m:.2f}x + {b:.2f})")
        plt.legend()

    plt.show()


# Crear un widget interactivo para seleccionar los países y la opción de línea de tendencia
interact(scatter_plot_dynamic, 
         country1=widgets.Dropdown(options=countries, description='País 1', value='United States'),
         country2=widgets.Dropdown(options=countries, description='País 2', value='China'),
         trendline=widgets.Checkbox(value=False, description='Mostrar línea de tendencia'))