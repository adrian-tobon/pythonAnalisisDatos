import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

##########Analisis Descriptivo##########
df_sales_data = pd.read_csv('pythonAnalisisDatos/sales_data.csv')
print(df_sales_data)
print(df_sales_data.info())

#estadisticas basicas y resumen de datos
stats = df_sales_data.describe()
print(stats)

mean_price = df_sales_data['Price Each'].mean()
median_price = df_sales_data['Price Each'].median()
mode_price = df_sales_data['Price Each'].mode()
std_price = df_sales_data['Price Each'].std()
min_price = df_sales_data['Price Each'].min()
max_price = df_sales_data['Price Each'].max()

#distribucion de frecuencias
product_counts = df_sales_data['Product'].value_counts()
print(product_counts)

#columnas categoricas
#df_sales_data[['Address','City','State']] = df_sales_data['Purchase Address'].str.split(",",expand=True)
#df_sales_data.drop('Purchase Address',axis=1,inplace=True)
#print(df_sales_data)
#df_sales_data['City'] = df_sales_data['Purchase Address'].apply(lambda x: x.split(',')[1].strip())
df_sales_data['City'] = df_sales_data['Purchase Address'].str.split(",",expand=True)[1]
city_counts = df_sales_data['City'].value_counts()
print(df_sales_data)
print(city_counts)

#distribucion de fechas
df_sales_data['Order Date'] = pd.to_datetime(df_sales_data['Order Date'], errors='coerce')
date_counts = df_sales_data['Order Date'].dt.month.value_counts().sort_index()
print(date_counts)

#visualizacion de datos descriptivos

#histograma
'''
plt.figure(figsize=(4,3))
sns.histplot(df_sales_data['Price Each'],bins=20,kde=True)
plt.title('Distribucion de Precios')
plt.xlabel('Precio Unitario')
plt.ylabel('Frecuencia')
plt.show()
'''

#count plot
'''
plt.figure(figsize=(5,3))
sns.countplot(data=df_sales_data, y= 'Product',order=df_sales_data['Product'].value_counts().index)
plt.title('frecuencia De Productos Vendidos')
plt.xlabel('Cantidad vendida')
plt.ylabel('Producto')
plt.show()
'''

#grafico de cajas
'''
plt.figure(figsize=(4,3))
sns.boxplot(x=df_sales_data['Price Each'])
plt.title('Boxplot de Precios Unitarios')
plt.xlabel('Precio Unitario')
plt.show()
'''


#df_sales_data['City'] = df_sales_data['Purchase Address'].str.split(",",expand=True)[1]
#city_counts = df_sales_data['City'].value_counts()
'''
plt.figure(figsize=(5,3))
city_order = df_sales_data['City'].value_counts().index
sns.countplot(data=df_sales_data, y= 'City',order=city_order)
plt.title('Cantidad de Ventas por Ciudad')
plt.xlabel('Cantidad de Ventas')
plt.ylabel('Ciudad')
plt.show()
'''
#grafico de lineas

#df_sales_data['Order Date'] = pd.to_datetime(df_sales_data['Order Date'], errors='coerce')
df_sales_data['Month'] = df_sales_data['Order Date'].dt.month
monthly_sales = df_sales_data['Month'].value_counts().sort_index()


plt.figure(figsize=(4,3))
plt.plot(monthly_sales.index,monthly_sales.values,marker='o')
plt.title('Ventas por mes')
plt.xlabel('Mes')
plt.ylabel('Cantidad de Ventas')
plt.show()

