import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

##########Analisis de correlacion y regresion##########

#Medicion de correlacion

df_sales_data = pd.read_csv('pythonAnalisisDatos/sales_data.csv')
print(df_sales_data)
print(df_sales_data.info())


correlation_matrix = df_sales_data[['Quantity Ordered','Price Each']].corr()
print(correlation_matrix)
print(type(correlation_matrix))
'''
#mapa de calor
plt.figure(figsize=(5,3))
sns.heatmap(correlation_matrix,annot=False,cmap='coolwarm',linewidths=0.5)
plt.title('Mapa de Calor Correlacion')
plt.show()
'''
df_sales_data_correlated = pd.read_csv('pythonAnalisisDatos/sales_data_correlated.csv')
print(df_sales_data_correlated)
print(df_sales_data_correlated.info())


correlation_matrix2 = df_sales_data_correlated[['Quantity Ordered','Price Each']].corr()
print(correlation_matrix2)
print(type(correlation_matrix2))

'''
plt.figure(figsize=(5,3))
sns.heatmap(correlation_matrix2,annot=True,cmap='coolwarm',linewidths=0.5)
plt.title('Mapa de Calor Correlacion')
plt.show()
'''

corr_value = df_sales_data_correlated['Price Each'].corr(df_sales_data_correlated['Quantity Ordered'])
print(f"Correlacion entre Price Each y Quatity Orderen: {corr_value}")

strong_corr = correlation_matrix2[(correlation_matrix2 > 0.8) | (correlation_matrix2 < -0.8)]
print(strong_corr)
'''
sns.pairplot(df_sales_data_correlated[['Price Each','Quantity Ordered']])
plt.show()
'''
#graficos de dispersion
'''
plt.figure(figsize=(5,3))
#plt.scatter(df_sales_data_correlated['Price Each'],df_sales_data_correlated['Quantity Ordered'], alpha=0.5)
sns.scatterplot(df_sales_data_correlated,x='Price Each',y='Quantity Ordered')
plt.title('Dispersion Correlacion')
plt.xlabel('Price Each')
plt.ylabel('Quantity Ordered')
plt.show()
'''
#agrupacion por datos categoricos
'''
plt.figure(figsize=(5,3))
#plt.scatter(df_sales_data_correlated['Price Each'],df_sales_data_correlated['Quantity Ordered'], alpha=0.5)
sns.scatterplot(df_sales_data_correlated,x='Price Each',y='Quantity Ordered',hue='Product',palette='viridis')
plt.title('Dispersion Correlacion')
plt.xlabel('Price Each')
plt.ylabel('Quantity Ordered')
#plt.legend(bbox_to_anchor=(1.05,1),loc='upper left')
plt.show()
'''

#dispersion con regresion lineal
'''
plt.figure(figsize=(5,3))
#plt.scatter(df_sales_data_correlated['Price Each'],df_sales_data_correlated['Quantity Ordered'], alpha=0.5)
#sns.scatterplot(df_sales_data_correlated,x='Price Each',y='Quantity Ordered',hue='Product',palette='viridis', alpha=0.5, s=100, edgecolor='k')
sns.regplot(df_sales_data_correlated,x='Price Each',y='Quantity Ordered',scatter_kws={'alpha':0.5,'s':100,'edgecolor':'k'},line_kws={'color':'red'})
plt.title('Dispersion Correlacion')
plt.xlabel('Price Each')
plt.ylabel('Quantity Ordered')
plt.grid(True,linestyle='--',alpha=0.5)
#plt.legend(bbox_to_anchor=(1.05,1),loc='upper left')
plt.show()
'''

# regrsion lineal y multiple

# regresion lineal simple

x = df_sales_data_correlated[['Price Each']] #variable independiente
y = df_sales_data_correlated[['Quantity Ordered']] #variable dependiente

model = LinearRegression()
model.fit(x,y)

y_pred = model.predict(x)

'''
plt.figure(figsize=(5,3))
sns.scatterplot(df_sales_data_correlated,x='Price Each',y='Quantity Ordered', alpha=0.5)
plt.plot(x,y_pred,color='red',linewidth=2)
plt.title('Regresion Lineal: Price Each vs. Quantity Ordered')
plt.xlabel('Price Each')
plt.ylabel('Quantity Ordered')
plt.grid(True,linestyle='--',alpha=0.5)
plt.show()
'''

r_squared = model.score(x,y)
print(f"R²(coeficiente de determinacion) del modelo = {r_squared}")

#regresion multiple

df_sales_data_correlated['Order Month'] = pd.to_datetime(df_sales_data_correlated['Order Date'],errors='coerce').dt.month
print(df_sales_data_correlated)

x_multiple = df_sales_data_correlated[['Price Each','Order Month']]
#y = df_sales_data_correlated['Quantity Ordered'] # ya se declaro previasmente

model_multiple = LinearRegression()
model_multiple.fit(x_multiple,y)

print(f"Coeficientes: {model_multiple.coef_}")
print(f"interseccion: {model_multiple.intercept_}")

r_squared_multiple = model_multiple.score(x_multiple,y)
print(f"R²(coeficiente de determinacion) del modelo multiple = {r_squared_multiple}")

#residuales
residuals = y - model_multiple.predict(x_multiple)
print(type(model_multiple.predict(x_multiple)))
print(type(residuals))

#no me funciona el grafico
'''
plt.figure(figsize=(5,3))
sns.scatterplot(x=model_multiple.predict(x_multiple), y=residuals)
plt.axhline(0,color='red',linestyle='--')
plt.title('Grafico Residuales')
plt.xlabel('Predicciones')
plt.ylabel('Residuos')
plt.grid(True,linestyle='--',alpha=0.5)
plt.show()
'''
