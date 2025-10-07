import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##########Carga de datos y exploracion inicial##########
df_sales_data = pd.read_csv('pythonAnalisisDatos/sales_data.csv')

print(df_sales_data)
print(df_sales_data.info())
print(df_sales_data.describe())

#identificacion de datos faltantes y anomalias
df_sales_data_issues = pd.read_csv('pythonAnalisisDatos/sales_data_with_issues.csv')
print(df_sales_data_issues)
print(df_sales_data_issues.info())
print(df_sales_data_issues.describe())

#datos faltantes
print(df_sales_data_issues[df_sales_data_issues.isnull().any(axis=1)])
#df_sales_data_issues.dropna(axis=0,inplace=True)
#df_sales_data_issues['Quantity Ordered'] = df_sales_data_issues['Quantity Ordered'].fillna(value=0)

#anomalias
#precios menores que cero
print(df_sales_data_issues[df_sales_data_issues['Price Each'] < 0])

#fechas con mal formato
print(df_sales_data_issues[~df_sales_data_issues['Order Date'].str.match(r'^\d{4}-\d{2}-\d{2}',na=False)])



