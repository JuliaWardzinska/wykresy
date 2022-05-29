import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from PIL import Image
#

# x = np.linspace(0, 2 * np.pi, 100)
# y = np.sin(x)
# z = np.cos(x)
#
# fig, ax1 = plt.subplots()
# plt.ylim([-1.0, 1])
# plt.xlim([0, 5])
# ax2= ax1.twinx()
#
# ax1.plot(x,y, color='orange', ls = ':')
# ax2.plot(x,z, color='brown', ls = ':')
# ax2.set_ylim(-2, 2, 0.5)
#
# ax1.set_ylabel('oś lewa', color = 'g')
# ax1.set_xlabel('oś dolna')
# ax2.set_ylabel('oś prawa', color = 'r')
# plt.title('To jest tytuł wykresu')
#
# legenda1 = plt.legend(["sin(x)"], loc = 'center right')
# legenda2 = plt.legend(["cos(x)"], loc = 'lower center' )
# plt.gca().add_artist(legenda1)
# plt.gca().add_artist(legenda2)
# plt.show()



xlsx= pd.ExcelFile('ceny1.xlsx')
df4= pd.read_excel(xlsx, header=0)
# print(df4)
# print
# print(df4.agg({'Wartość': ['sum']}))
# print(df4.agg({'Wartość': ['mean']}))
# print(df4[df4['Rodzaje towarów'] == 'ryż - za 1kg'].agg({'Wartość': ['mean']}))
# print(df4[df4['Rodzaje towarów'] == 'mąka pszenna - za 1kg'].agg({'Wartość': ['mean']}))


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
# plt.text(2010,4, '129936')
# plt.legend()
#
# # plt.savefig("zadanie2.png")
# plt.show()



# df = pd.read_csv('nieruchomosci1.csv', header=None, sep=";", decimal=".")
#
# df_1 = df.T
#
# print(df_1)
#
# grouped_df = df_1.groupby(0)
# grouped_list_label = grouped_df[1].apply(list)
# grouped_list_value = grouped_df[4].apply(list)
#
# grouped_list_label = grouped_list_label.reset_index()
# grouped_list_value = grouped_list_value.reset_index()
#
# # df_1.reset_index()
#
# grouped_label = grouped_list_label.T
# grouped_value = grouped_list_value.T
#
# grouped_label = grouped_label.reset_index()
# grouped_value = grouped_value.reset_index()
#
# grouped_value_pierwotny = []
# for one_value in grouped_value[0][1]:
#     grouped_value_pierwotny.append(int(one_value.replace(" ", "")))
#
# grouped_pierwotny_label = grouped_label[0][1]
#
# print(grouped_value_pierwotny)
# print(grouped_pierwotny_label)
#
# df_new = pd.DataFrame(grouped_value_pierwotny, index=grouped_pierwotny_label)
#
# plot = df_new.plot.pie(subplots=True)
#
# # grupa = df_1.groupby([0])
# #
# # df_1.plot(kind='pie', subplots=True)
# #
# # for oneRow in df_1:
# #    print(oneRow)
#
# plt.show()
