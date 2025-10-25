import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

##########Visualizacion de datos basicos##########

df_sales_data = pd.read_csv('pythonAnalisisDatos/sales_data_correlated.csv')
print(df_sales_data)
print(df_sales_data.info())
