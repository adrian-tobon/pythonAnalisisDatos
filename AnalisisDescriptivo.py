from unicodedata import category
import pandas as pd

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

#visualizaiocn de datos descriptivos

