import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#jpj
df_T = pd.read_excel('Ti_Terapia.xlsx')
df_X = df_T.melt(id_vars=['EDAD','GÉNERO','TIEMPO (MESES)','TIPO SONIDO','FREC','TTO EN MESES','TIPO DE INTERVENCIÓN','ARISTA SS','HIPERACUSIA','SALUD MENTAL'],value_vars=['THI INICIAL','THI FINAL'],var_name='Momento',value_name='THI')
df_X.reset_index()
sns.boxplot(data=df_X, x='Momento',y='THI')
plt.show()
print(df_T)
