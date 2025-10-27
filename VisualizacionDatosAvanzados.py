import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

##########Visualizacion de datos avanzados##########
data = {'Category A': [25, 30, 35, 45, 50, 55, 60, 70, 80, 85],
        'Category B': [20, 25, 30, 35, 40, 45, 50, 55, 65, 70]}
df = pd.DataFrame(data)
print(df)

#Mathplotlib
'''
plt.figure(figsize=(6,3))
plt.boxplot([df['Category A'],df['Category B']],tick_labels=['Category A','Category B'])
plt.title('Boxplot chart - Matplotlib')
plt.ylabel('Values')
plt.grid(True)
plt.show()
'''
#seaborn
data_seaborn = {'Category': ['A']*10 + ['B']*10,
        'Values': [25, 30, 35, 45, 50, 55, 60, 70, 80, 85, 20, 25, 30, 35, 40, 45, 50, 55, 65, 70]}
df_seaborn = pd.DataFrame(data_seaborn)
print(df_seaborn)

'''
plt.figure(figsize=(6,3))
sns.boxplot(x=df_seaborn['Category'],y=df_seaborn['Values'],hue=df_seaborn['Category'],palette='pastel')
sns.swarmplot(x=df_seaborn['Category'],y=df_seaborn['Values'],color='black',size=5)
plt.title('Boxplot chart - Seaborn')
plt.ylabel('Values')
plt.grid(True)
plt.show()
'''
#division por subcategorias

data_subcat = {'Category': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
               'Group': ['X', 'X', 'Y', 'Y', 'Y', 'X', 'X', 'Y', 'Y', 'Y'],
               'Values': [25, 30, 35, 45, 50, 20, 25, 30, 35, 40]}
df_subcat = pd.DataFrame(data_subcat)
print(df_subcat)
'''
plt.figure(figsize=(6,3))
sns.boxplot(x=df_subcat['Category'],y=df_subcat['Values'],hue=df_subcat['Group'],palette='Set2')
plt.title('Boxplot with Subcategories chart - Seaborn')
plt.ylabel('Values')
plt.grid(True)
plt.show()
'''

#grafico de violin
data_violin = {'Category': ['A']*10 + ['B']*10,
        'Values': [25, 30, 35, 45, 50, 55, 60, 70, 80, 85, 20, 25, 30, 35, 40, 45, 50, 55, 65, 70]}
df_violin = pd.DataFrame(data_violin)
print(df_violin)

'''
plt.figure(figsize=(6,3))
sns.violinplot(x=df_violin['Category'],y=df_violin['Values'],hue=df_violin['Category'],palette='Set2')
plt.title('Violin plot chart - Seaborn')
plt.ylabel('Values')
plt.grid(True)
plt.show()
'''

data_split = {'Category': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
              'Group': ['X', 'X', 'Y', 'Y', 'Y', 'X', 'X', 'Y', 'Y', 'Y'],
              'Values': [25, 30, 35, 45, 50, 20, 25, 30, 35, 40]}
df_split = pd.DataFrame(data_split)
print(df_split)

'''
plt.figure(figsize=(6,3))
sns.violinplot(x=df_split['Category'],y=df_split['Values'],hue=df_split['Group'],split=True,palette='Set2')
plt.title('Split Violin plot chart - Seaborn')
plt.ylabel('Values')
plt.grid(True)
plt.show()
'''
'''
plt.figure(figsize=(6,3))
sns.violinplot(y=df_violin['Category'],x=df_violin['Values'],hue=df_violin['Category'],palette='Set2',inner='quartile')
#sns.boxplot(y=df_violin['Category'],x=df_violin['Values'],hue=df_violin['Category'],width=0.1,palette='dark:black',showcaps=True,boxprops={'facecolor':'None'})
plt.title('Split Violin plot chart - Seaborn')
plt.ylabel('Values')
plt.grid(True)
plt.show()
'''

#mapas de calor
data_heatmap = np.random.rand(10, 12)
print(data_heatmap)

'''
plt.figure(figsize=(12, 8))
sns.heatmap(data_heatmap,cmap='Greens',linewidth=0.5,annot=True,fmt='.2f')
plt.title('Heat Map - Seaborn')
plt.show()
'''

data_corr = {'A': [0, 2, 3, 4, 5], 
        'B': [5, 8, 3, 2, 1], 
        'C': [2, 3, 4, 5, 6], 
        'D': [5, 3, 1, 4, 2]}
df_corr = pd.DataFrame(data_corr)
print(df_corr)

corr_matrix = df_corr.corr()

mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
#mask = np.tril(np.ones_like(corr_matrix, dtype=bool))

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix,cmap='magma',linewidth=1.5,annot=True,mask=mask,linecolor='white')
#sns.heatmap(df_corr, vmin=0, vmax=10, cmap='YlGnBu', cbar_kws={'label': 'Value'})
plt.title('Heat Map Correlation Matrix - Seaborn')
plt.show()


