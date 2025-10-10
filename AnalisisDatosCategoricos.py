import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

##########Analisis de Datos categoricos##########

df_sales_data = pd.read_csv('pythonAnalisisDatos/sales_data.csv')
df_sales_data['City'] = df_sales_data['Purchase Address'].str.split(',',expand=True)[1]
print(df_sales_data)
print(df_sales_data.info())

#Analisis de frecuencia y proporciones
product_frecuency = df_sales_data['Product'].value_counts()
print(product_frecuency)

city_frecuency = df_sales_data['City'].value_counts()
print(city_frecuency)

product_proportion = df_sales_data['Product'].value_counts(normalize=True)
city_proportion = df_sales_data['City'].value_counts(normalize=True)

print(product_proportion)
print(city_proportion)

#frecuencia con tablas cruzadas
product_city_crosstab = pd.crosstab(df_sales_data['City'],df_sales_data['Product'])
print(product_city_crosstab)

#frecuencias agrupadas
product_by_city = df_sales_data.groupby('City')['Product'].value_counts()
print(product_by_city)

#proporciones con condiciones
high_price_products = df_sales_data[df_sales_data['Price Each'] >1000]
high_price_proportion = high_price_products['City'].value_counts(normalize=True)
print(high_price_proportion)

#grafico de barras vertical
'''
print(df_sales_data['Product'].value_counts().index)
plt.figure(figsize=(5,3))
sns.countplot(data=df_sales_data,x='Product',order=df_sales_data['Product'].value_counts().index)
plt.title('Frecuencia de Productos Vendidos(Vertical)')
plt.xlabel('Producto')
plt.ylabel('Cantidad Vendida')
plt.xticks(rotation=45)
plt.show()
'''
#grafico de barras horizontal
'''
plt.figure(figsize=(5,3))
sns.countplot(data=df_sales_data,y='Product',order=df_sales_data['Product'].value_counts().index)
plt.title('Frecuencia de Productos Vendidos(Horizontal)')
plt.xlabel('Producto')
plt.ylabel('Cantidad Vendida')
#plt.xticks(rotation=45)
plt.show()
'''
#grafico de barras agrupado
'''
plt.figure(figsize=(6,4))
sns.countplot(data=df_sales_data,x='City',hue='Product',order=df_sales_data['City'].value_counts().index)
plt.title('Frecuencia de Productos Vendidos por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Cantidad Vendida')
plt.xticks(rotation=45)
plt.legend(title='Producto',bbox_to_anchor=(1,1),loc='upper left')
plt.show()
'''

#grafico de barras para proporciones
product_proportion2 = df_sales_data['Product'].value_counts(normalize=True).reset_index()
product_proportion2.columns = ['Product','Proportion']

'''
plt.figure(figsize=(5,3))
sns.barplot(data=product_proportion2,x='Product',y='Proportion',palette='viridis')
#sns.barplot(data=product_proportion2,hue='Product',y='Proportion',legend=False)
plt.title('Proporcion de Productos Vendidos')
plt.xlabel('Producto')
plt.ylabel('Proporcion')
plt.xticks(rotation=45)
plt.grid(True,axis='y',linestyle='--',alpha=0.7)
plt.show()
'''

#grafico de tortas
'''
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']
explode = [0.2] + [0] * (len(product_proportion) - 1)
#explode = [0.1,0,0,0,0,0,0,0]

plt.figure(figsize=(4,4))
plt.pie(product_proportion, labels=product_proportion.index,autopct='%1.1f%%',startangle=90,
        colors=colors, explode=explode, shadow=True)
plt.title('Distribucion de Productos Vendidos')
#plt.axis('equal')
plt.show()
'''

#diagrama de torta con porciones agregadas

threshold = 0.10
city_proportion['Others'] = city_proportion[city_proportion < threshold].sum()
city_proportion = city_proportion[city_proportion >= threshold]

print(city_proportion)

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']
explode = [0.2] + [0] * (len(city_proportion) - 1)

plt.figure(figsize=(4,4))
plt.pie(city_proportion, labels=city_proportion.index,autopct='%1.1f%%',startangle=90,
         colors = colors,explode=explode,shadow=True)
plt.title('Distribucion de ventas por ciudad(agrupaciones pequeñas)')
#plt.axis('equal')
plt.show()
