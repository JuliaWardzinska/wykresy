# kolo 4 zadania, 3 wykresy, 2 grupy, beda przypisane biblioteki, matlib bedzie trzeba powyciagać grupy, 1 wektor, etrykiety itd.sami bioblioteki instalujemy i projekt robimy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# a = np.array([20, 30 , 40, 50])
# b = np.arange(4)
#
# c = a + b
# print(c)
# d = np.sqrt(b)
# print(d)
#
# e = d + c
# print(e)

# a = np.arange(12).reshape((3,4))
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.sum(axis=1))
# print(a.cumsum(axis=1))

# a= np.arange(3)
# b= np.arange(3)
# print(np.dot(a,b))
# print(a.dot(b))
# c = np.arange(3)
# d = np.array([[0],[1],[2]])
# print(c.dot(d))
# e = np.array([[2,5,1], [3,4,5]])
# f = np.array([[3,4],[1,6],3,3])
# print(e.dot(f))

# a= np.arange(6).reshape((3,2))
# print(a.flat)
# for b in a:
#     for c in b:
#         print(c)
# for d in a.flat:
#     print(d)

# a = np.arange(12).reshape((3,4))
# print(a)
# b = a.reshape((4,3))
# print(b)
# c = b.ravel()
# print(c)
# d = b.T
# print(d)


# s=pd.Series([1,3,5,5.5,"a"])
# print(s)
t = pd.Series([10,12,14,8], index=["a","b","c","d"])
print(t)
data = {'Kraj':['Belgia','Indie','Brazylia'],'Stolica':["bruksel",'new delpi',"brasilia"],'populacja':[1112312,131241,123414]}
df = pd.DataFrame(data)
print(df)
#
# daty = pd.date_range('20220507',periods=5)
# df2 = pd.DataFrame(np.random.randn(5,4),index=daty,columns=list('ABCD'))
# print(df2)
#
df3 = pd.read_csv('dane.csv', header=0,sep=";", decimal='.')
# print(df3)
# xlsx = pd.ExcelFile('imiona.xlsx')
# df4 = pd.read_excel(xlsx,header=0)
# print(df4)

# df3.to_csv('dane2.csv',index=False)
# df4.to_excel('imiona2.xlsx',sheet_name='dane')
# print(df4.head(10))
# print(df4.tail(10))
# print(df4.sample())
# print(df4.sample(5))
# print(df.sample(4, replace=True))

# print(t['a'])
# print(t.a)
# print(df[0:1])
# print(df['Kraj'])
# #
# print(df.iloc[[0], [0]])
# print(df.loc[[0], 'Kraj'])
# print(df.at[0,'Kraj'])

# print(t['a'])
# print(t[t > 10])
# print(t[(t < 13) & (t > 8)])
# print(t.where(t > 10))
# print(t.where (t > 10, 'warunek niespelniony'))
# t.where(t > 10, 'warunek niespelniony', inplace=True)
# print(t)

# print(df['Kraj'])
# print(df[df['populacja'] > 1100000])
#
# t['e'] = 14
# print(t)
#
# df.loc[3] = 'nowy element'
# print(df)
# df.loc[4] = ['Polska', 'Warszwa', 38537473]
# print(df)

# new = df.drop([3])
# print(new)
# df.drop([3], inplace=True)
# print(df)
# df['Kontynent'] = ['europa', 'azja', 'amery pol', 'europa']
# print(df)
#
# df.sort_values(by='Kraj', inplace=True)
# print(df)
# grupa = df.groupby(by='Kontynent')
# print(grupa.get_group('europa'))
# grupa = df.groupby('Kontynent').agg({'populacja': ['sum']})
# print(grupa)
#
# grupa.plot(kind = 'bar', xlable = 'Kontynenty', ylabel ='populacja', rot =0, tiltle = ' popuklacja w mln') Może być nie tak

# wykres = grupa.plot.bar()
# wykres.set_xlable('Kontynrnt')
# wykres.set_ylable('populacja w mld')
# wykres.tick_params(axis="x", lablerotation = 0)
# wykres.set_title('populacja na kontynentach')
# plt.savefig('plot2.png')
# plt.show()

# grupa = df3.groupby('Imię i nazwisko').agg({'Wartość zamówienia': ['sum']})
# print(grupa)
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=20, figsize=(8,8), colors=['red','green'])
# plt.legend(loc='upper left')
# plt.show()


seria = pd.Series(np.random.randn(1000))
seria = seria.cumsum()

seria.plot()
plt.show()

# cw 20.05.2022
# import Pillow 9.0.1
