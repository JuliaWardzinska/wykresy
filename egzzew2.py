import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# fig, (ax1, ax2) = plt.subplots(1,2, )
# data = {'A': 35, 'B': 46 , 'C': 14, 'D': 41 ,'E': 40}
# data2 = {'A': -31, 'B': -34 , 'C': -38, 'D': -33 ,'E': -30}
#
# y = np.arange(0,40,10)
# z = np.arange(-30, 0, 10)
# osx = list(data.keys())
# wart1 = list(data.values())
# osx2 = list(data2.keys())
# wart2 = list(data2.values())
#
# color1 = ('powderblue', 'pink', 'coral', 'grey', 'darkviolet')
# color2 =('violet', 'cyan','cyan','peru','olive' , )
#
# ax1.barh(osx, wart1, color = color1)
# ax2.barh(osx2, wart2, color = color2)
# ax1.set_title("Wykres lewy")
# ax2.set_title("Wykres prawy")
# plt.show()

# xlsx= pd.ExcelFile('ceny2.xlsx')
# df4= pd.read_excel(xlsx, header=0)
# print(df4)
# plt.subplot()
# x = df4['Rok'].unique()
# grupa = df4.groupby(by = 'Rodzaje towarów')
# ryz = grupa.get_group('ryż - za 1kg')
# maka = grupa.get_group('mąka pszenna - za 1kg')
# ryz2 = ryz.groupby('Rok').agg({'Wartość':['sum']}).values
# maka2 = maka.groupby('Rok').agg({'Wartość':['sum']}).values
# plt.plot(x, ryz2, label="ryz")
# plt.plot(x, maka2, label="maka")
# plt.xlabel('Rok')
# plt.ylabel('Cena')
# plt.title('Cena produktów w danym roku')
# plt.text(2011,2, '129936')
# plt.legend()
# plt.savefig("zadanie2.png")
# plt.show()
df = pd.read_csv('nieruchomosci2.csv', header=None, sep=";", decimal=".")

df_1 = df.T
print(df_1)
# print(df_1)

grouped_df = df_1.groupby(0)
grouped_list_label = grouped_df[1].apply(list)
grouped_list_value = grouped_df[3].apply(list)

grouped_list_label = grouped_list_label.reset_index()
grouped_list_value = grouped_list_value.reset_index()

# df_1.reset_index()

grouped_label = grouped_list_label.T
grouped_value = grouped_list_value.T

grouped_label = grouped_label.reset_index()
grouped_value = grouped_value.reset_index()

grouped_value_pierwotny = []
for one_value in grouped_value[0][1]:
    grouped_value_pierwotny.append(int(one_value.replace(" ", "")))

grouped_pierwotny_label = grouped_label[0][1]

print(grouped_value_pierwotny)
print(grouped_pierwotny_label)

df_new = pd.DataFrame(grouped_value_pierwotny, index=grouped_pierwotny_label)

plot = df_new.plot.pie(subplots=True)

plt.show()