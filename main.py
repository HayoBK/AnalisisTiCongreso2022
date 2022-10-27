#%% Cargar datos
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#jpj
df_T = pd.read_excel('Ti_Terapia.xlsx')
df_X = df_T.melt(id_vars=['EDAD','GÉNERO','TIEMPO (MESES)','TIPO SONIDO','FREC','TTO EN MESES','TIPO DE INTERVENCIÓN','ARISTA SS','HIPERACUSIA','SALUD MENTAL'],value_vars=['THI INICIAL','THI FINAL'],var_name='Momento',value_name='THI')
df_X.reset_index()
#%% Grafico Final/inicial
sns.boxplot(data=df_X, x='Momento',y='THI')
sns.swarmplot(data=df_X,x='Momento',y='THI')
plt.show()

#%%
B=[0,17,37,57,77,100]
fig,ax = plt.subplots()
df_i = df_X[df_X['Momento']=='THI INICIAL']
sns.histplot(data=df_i, x='THI', bins=B, stat='percent',multiple='layer', common_norm=False) #, common_norm=False,element='step', fill=False)
#sns.displot(data=df_X, x='THI',hue='Momento',bins=B ,kind='kde', common_norm=False)
for bars in ax.containers:
    ax.bar_label(bars,fmt = '%.0f%%', size=14)
plt.ylim(0,50)
plt.show()

df_i = df_X[df_X['Momento']=='THI FINAL']
sns.histplot(data=df_i, x='THI', bins=B, stat='percent',multiple='layer', common_norm=False) #, common_norm=False,element='step', fill=False)
#sns.displot(data=df_X, x='THI',hue='Momento',bins=B ,kind='kde', common_norm=False)
plt.ylim(0,50)
plt.show()

#%% Bin data --> no lo usaré
df_X['THI (nivel)'] = pd.cut( x= df_X['THI'], bins=[0,17,37,57,77,100], labels = ['Muy leve','Leve','Moderado','Severo','Catrastrófico'])
sns.countplot(data=df_X, x='THI (nivel)', hue='Momento')
plt.show()
print(df_T)
