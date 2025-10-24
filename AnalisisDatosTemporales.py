import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

##########Analisis de datos temporales##########

#manipulacion de datos de fecha y hora

df_sales_data = pd.read_csv('pythonAnalisisDatos/sales_data_correlated.csv')
print(df_sales_data)
print(df_sales_data.info())