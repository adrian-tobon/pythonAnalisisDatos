import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

plt.figure(figsize=(5,3))
#plt.scatter(df_sales_data_correlated['Price Each'],df_sales_data_correlated['Quantity Ordered'], alpha=0.5)
sns.scatterplot(df_sales_data_correlated,x='Price Each',y='Quantity Ordered')
plt.title('Dispersion Correlacion')
plt.xlabel('Price Each')
plt.ylabel('Quantity Ordered')
plt.show()