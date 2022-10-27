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
#sns.swarmplot(data=df_X,x='Momento',y='THI')
plt.show()

#%% Graficos 2a y b :--> Distribución de nivel de THI
B=[0,17,37,57,77,100]
df_i = df_X[df_X['Momento']=='THI INICIAL']

fig,ax = plt.subplots(figsize= (10,10))
sns.set(font_scale=2)
sns.set_style('white')
sns.histplot(data=df_i, x='THI', bins=B, stat='percent', multiple='layer') #, common_norm=False,element='step', fill=False)
for bars in ax.containers:
    ax.bar_label(bars,fmt = '%.0f%%', size=22)
ax.patches[0].set_facecolor('mediumturquoise')
ax.patches[1].set_facecolor('khaki')
ax.patches[2].set_facecolor('goldenrod')
ax.patches[3].set_facecolor('firebrick')
ax.patches[4].set_facecolor('maroon')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.ylim(0,50)
plt.show()


#%% Bin data --> no lo usaré
df_X['THI (nivel)'] = pd.cut( x= df_X['THI'], bins=[0,17,37,57,77,100], labels = ['Muy leve','Leve','Moderado','Severo','Catrastrófico'])
sns.countplot(data=df_X, x='THI (nivel)', hue='Momento')
plt.show()
print(df_T)
