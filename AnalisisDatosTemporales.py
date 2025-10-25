import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

##########Analisis de datos temporales##########

#manipulacion de datos de fecha y hora

df_sales_data = pd.read_csv('pythonAnalisisDatos/sales_data_correlated.csv')
print(df_sales_data)
print(df_sales_data.info())

df_sales_data['Order Date'] = pd.to_datetime(df_sales_data['Order Date'], errors='coerce')

#extraer datos de las fecha
df_sales_data['Year'] = df_sales_data['Order Date'].dt.year
df_sales_data['Month'] = df_sales_data['Order Date'].dt.month
df_sales_data['Day'] = df_sales_data['Order Date'].dt.day
df_sales_data['Day Name'] = df_sales_data['Order Date'].dt.day_name()
df_sales_data['Month Name'] = df_sales_data['Order Date'].dt.month_name()

print(df_sales_data)

#indices temporales
df_sales_data.set_index('Order Date',inplace=True)
monthly_sales = df_sales_data['Quantity Ordered'].resample('ME').sum()

print(monthly_sales)

#crear intervalos de tiempos y calculo de diferencias de tiempo

df_sales_data['Dias desde la ultima orden'] = df_sales_data.index.to_series().diff().dt.days
print(df_sales_data)

#graficos de series temporales
'''
plt.figure(figsize=(5,3))
#monthly_sales.plot()
sns.lineplot(data=monthly_sales)
plt.title('Ventas Mensuales')
plt.xlabel('Fecha')
plt.ylabel('Cantidad Vendida')
plt.xticks(rotation=45)
plt.grid(True,linestyle='--',alpha=0.5)
plt.show()
'''

#tendencias, estacionalidad y residuos
'''
decomposition = seasonal_decompose(monthly_sales,model='additive',period=2)
decomposition.plot()
plt.show()
'''

#grafico  de multiples series
plt.figure(figsize=(6,3))
df_sales_data[df_sales_data['Product'] == "USB-C Charging Cable"]['Quantity Ordered'].resample('ME').sum().plot(label= 'USB-C Cable')
df_sales_data[df_sales_data['Product'] == "Google Phone"]['Quantity Ordered'].resample('ME').sum().plot(label= 'Google Phone')
plt.title('Comparacion de Ventas por Producto')
plt.xlabel('Fecha')
plt.ylabel('Cantidad Vendida')
plt.legend()
plt.show()