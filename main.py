#%% Cargar datos
import pandas as pd
import seaborn as sns
#import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn import linear_model
import statsmodels.api as sm

#jpj
df_T = pd.read_excel('Ti_Terapia.xlsx') # wide format
df_X = df_T.melt(id_vars=['EDAD','GÉNERO','TIEMPO (MESES)','TIPO SONIDO','FREC','TTO EN MESES','TIPO DE INTERVENCIÓN','ARISTA SS','HIPERACUSIA','SALUD MENTAL'],value_vars=['THI INICIAL','THI FINAL'],var_name='Momento',value_name='THI')
df_X.reset_index() # df_X long format
#%% Grafico Final/inicial
fig,ax = plt.subplots(figsize= (12,10))
sns.set_style('white')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
g= sns.boxplot(data=df_X, x='Momento',y='THI', linewidth=5)
#g= sns.swarmplot(data=df_X, x='Momento',y='THI')
ax.patches[0].set_facecolor('darkgoldenrod')
ax.patches[1].set_facecolor('mediumseagreen')
g.tick_params(labelsize=25)
ax.set_xticklabels( ('Inicial', 'Post-Tratamiento'), fontweight= 'bold', fontsize=32 )


ax.set_xlabel('', fontweight='bold', fontsize=30, labelpad=15)
ax.set_ylabel('Puntaje THI (Tinnitus Handicap Inventory)', fontweight='bold', fontsize=30, labelpad=15)

plt.show()

#%% Graficos 2a y b :--> Distribución de nivel de THI
B=[0,17,37,57,77,100]
df_i = df_X[df_X['Momento']=='THI INICIAL']

fig,ax = plt.subplots(figsize= (12,10))
sns.set_style('white')
f=sns.histplot(data=df_i, x='THI', bins=B, stat='percent', multiple='layer') #, common_norm=False,element='step', fill=False)
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
f.tick_params(labelsize=25)

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
h = sns.jointplot(data = df_T, s=75, x='THI INICIAL', y='Porcentaje Reducción THI', marginal_kws=dict(bins=12, fill=True), marginal_ticks=True)
h.ax_joint.set_xlabel('Nivel Inicial de THI (pts)', fontweight='bold', fontsize=19, labelpad=15)
h.ax_joint.set_xticks([0,20,40,60,80,100],visible=True)
h.ax_joint.xaxis.set_ticklabels(h.ax_joint.get_xticklabels(),fontsize=15, rotation=90)
h.ax_joint.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
h.ax_joint.set_ylabel('Porcentaje Reducción THI', fontweight='bold', fontsize=19, labelpad=15)
h.ax_joint.set_yticks([0, 0.2,0.4,0.6,0.8,1], visible=True)
h.ax_joint.yaxis.set_ticklabels(h.ax_joint.get_yticklabels(),fontsize=15)
h.ax_joint.yaxis.set_major_formatter(ticker.PercentFormatter(1))
h.ax_joint.tick_params(bottom=True, left=True)


plt.ylim(-0.1,1.1)
plt.xlim(-5, 100)
plt.tight_layout()
plt.show()

#%%
fig,ax = plt.subplots(figsize= (20,20))

sns.histplot(data= df_T, x='Porcentaje Reducción THI', stat= 'percent',bins=[0,0.25,0.5,0.75,1])
for bars in ax.containers:
    ax.bar_label(bars,fmt = '%.0f%%', size=28, weight='bold')
plt.show()

#%%

df_U = df_T[df_T['THI FINAL'].notnull()]
print(df_U['TTO EN MESES'].mean())
print(df_U['TTO EN MESES'].std())

#%% Bin data --> no lo usaré
df_X['THI (nivel)'] = pd.cut( x= df_X['THI'], bins=[0,17,37,57,77,100], labels = ['Muy leve','Leve','Moderado','Severo','Catrastrófico'])
sns.countplot(data=df_X, x='THI (nivel)', hue='Momento')
plt.show()
print(df_T)

#%%
df_E = pd.read_excel('Ti_Eval.xlsx') # wide format
fig,ax = plt.subplots(figsize= (12,10))
sns.set_style('white')
B=[10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95]
f=sns.histplot(data=df_E, x='EDD', bins = B,stat='percent', multiple='layer')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_xlabel('EDAD', fontweight='bold', fontsize=30, labelpad=15)
ax.set_ylabel('Porcentaje de Pacientes', fontweight='bold', fontsize=30, labelpad=15)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f%%'))
f.set_xticks([10, 20, 30, 40, 50, 60, 70, 80, 90], visible=True)
f.tick_params(labelsize=25)
plt.show()

 #%%
df_E = pd.read_excel('Ti_Eval.xlsx') # wide format
def anyo(row):
    return  float((float(row['TIEMPO EVOL']) / 12 ))
df_E['TIEMPO EVOL'] = df_E.apply(anyo , axis=1)
B=[0,1,2,3,4,5,7,8,9,10,15,20,25,30,40,50,60]
fig,ax = plt.subplots(figsize= (12,10))
sns.set_style('white')
f=sns.histplot(data=df_E, x='TIEMPO EVOL', color='firebrick', bins=B,stat='percent', multiple='layer')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_xlabel('Tiempo de Presencia de Tinnitus (años)', fontweight='bold', fontsize=30, labelpad=15)
ax.set_ylabel('Porcentaje de Pacientes', fontweight='bold', fontsize=30, labelpad=15)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f%%'))
#f.set_xticks([10, 20, 30, 40, 50, 60, 70, 80, 90], visible=True)
f.tick_params(labelsize=25)
plt.show()

 #%%

fig,ax = plt.subplots(figsize= (12,10))
sns.set_style('white')
f=sns.histplot(data=df_T, x='TTO EN MESES', color='darkturquoise',stat='percent', multiple='layer')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_xlabel('Duración Terapia Sonora (meses)', fontweight='bold', fontsize=30, labelpad=15)
ax.set_ylabel('Porcentaje de Pacientes', fontweight='bold', fontsize=30, labelpad=15)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f%%'))
#f.set_xticks([10, 20, 30, 40, 50, 60, 70, 80, 90], visible=True)
f.tick_params(labelsize=25)
plt.show()

#%%
df_A = df_T
df_A.dropna(subset=['Porcentaje Reducción THI'], inplace= True)
df_A = df_A[['EDAD','FREC','TTO EN MESES', 'THI INICIAL','Porcentaje Reducción THI']]
df_A= df_A.dropna()
x = df_A[['EDAD','FREC','TTO EN MESES', 'THI INICIAL']]
y = df_A['Porcentaje Reducción THI']

x=sm.add_constant(x)
model = sm.OLS(y,x).fit()
predictions = model.predict(x)
print_model = model.summary()
print(print_model)