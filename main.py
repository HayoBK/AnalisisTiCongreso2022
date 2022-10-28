#%% Cargar datos
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#jpj
df_T = pd.read_excel('Ti_Terapia.xlsx') # wide format
df_X = df_T.melt(id_vars=['EDAD','GÉNERO','TIEMPO (MESES)','TIPO SONIDO','FREC','TTO EN MESES','TIPO DE INTERVENCIÓN','ARISTA SS','HIPERACUSIA','SALUD MENTAL'],value_vars=['THI INICIAL','THI FINAL'],var_name='Momento',value_name='THI')
df_X.reset_index() # df_X long format
#%% Grafico Final/inicial

sns.boxplot(data=df_X, x='Momento',y='THI')
#sns.swarmplot(data=df_X,x='Momento',y='THI')
plt.show()

#%% Graficos 2a y b :--> Distribución de nivel de THI
B=[0,17,37,57,77,100]
df_i = df_X[df_X['Momento']=='THI FINAL']

fig,ax = plt.subplots(figsize= (12,10))
sns.set_style('white')
sns.histplot(data=df_i, x='THI', bins=B, stat='percent', multiple='layer') #, common_norm=False,element='step', fill=False)
for bars in ax.containers:
    ax.bar_label(bars,fmt = '%.0f%%', size=28, weight='bold')
ax.patches[0].set_facecolor('mediumturquoise')
ax.patches[1].set_facecolor('khaki')
ax.patches[2].set_facecolor('goldenrod')
ax.patches[3].set_facecolor('firebrick')
ax.patches[4].set_facecolor('maroon')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_xlabel('Puntaje THI', fontweight='bold', fontsize=30, labelpad=15)
ax.set_ylabel('Porcentaje de Pacientes', fontweight='bold', fontsize=30, labelpad=15)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f%%'))
plt.ylim(0,50)
plt.show()

#%% Reducción
def reduccion(row):
    return (row['THI INICIAL']- row['THI FINAL'])
def Preduccion(row):
    return ( (row['THI INICIAL']- row['THI FINAL']) / row['THI INICIAL'] )
df_T['Reducción THI'] = df_T.apply(reduccion , axis=1)
df_T['Porcentaje Reducción THI'] = df_T.apply(Preduccion , axis=1)
df_T['THI (nivel)'] = pd.cut( x= df_T['THI INICIAL'], bins=[0,17,37,57,77,100], labels = ['Muy leve','Leve','Moderado','Severo','Catrastrófico'])

fig,ax = plt.subplots(figsize= (20,20))
sns.set_style('white')
h = sns.jointplot(data = df_T, s=75, x='Reducción THI', y='Porcentaje Reducción THI', marginal_kws=dict(bins=14, fill=True))
h.ax_joint.set_xlabel('Reducción puntaje THI', fontweight='bold', fontsize=22, labelpad=15)
h.ax_joint.set_xticks([0,10,20,30,40,50,60], visible=True)
h.ax_joint.xaxis.set_ticklabels(h.ax_joint.get_xticklabels(),fontsize=15, rotation=90)
h.ax_joint.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
h.ax_joint.set_ylabel('Porcentaje Reducción THI', fontweight='bold', fontsize=22, labelpad=15)
h.ax_joint.set_yticks([0, 0.2,0.4,0.6,0.8,1], visible=True)
h.ax_joint.yaxis.set_ticklabels(h.ax_joint.get_yticklabels(),fontsize=15, rotation=90)
h.ax_joint.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f%%'))
plt.ylim(-0.1,1.1)
plt.xlim(-5,60)

plt.show()

#%% Bin data --> no lo usaré
df_X['THI (nivel)'] = pd.cut( x= df_X['THI'], bins=[0,17,37,57,77,100], labels = ['Muy leve','Leve','Moderado','Severo','Catrastrófico'])
sns.countplot(data=df_X, x='THI (nivel)', hue='Momento')
plt.show()
print(df_T)
