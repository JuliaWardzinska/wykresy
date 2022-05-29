import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# x = np.linspace(-5,5,25)
# y1 = -x**3 + 3*x - 7
# y2 = 4*x +6
# y3 = 6 + 4*x**3
# # fig, ax1, ax2,ax3 = plt.subplots()
# plt.plot(x,y1, c = 'c', ls = ":", label = '-x**3 + 3*x - 7')
# plt.plot(x,y2, c = 'pink', ls = '-.', label = '4*x +6')
# plt.plot(x,y3, c = 'olive', ls = '-', label =  '6 + 4*x**3')
# plt.grid()
# plt.title('To jest tytuł wykresu')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend()
# plt.show()


# xlsx= pd.ExcelFile('kina4.xlsx')
# df4= pd.read_excel(xlsx, header=0)
#
# print(df4)
# plt.subplot()
# x = df4['Rok'].unique()
# grupa = df4.groupby(by = 'Gestor')
# miejskie = grupa.get_group('miejskie')
# miejskie2 = miejskie.groupby(by = 'Wykaz')
# miejskie_sale = miejskie2.get_group('sale')
# miejskie_miejsca = miejskie2.get_group('miejsca na widowni')
# powiatowe = grupa.get_group('powiatowe')
# wojewódzkie = grupa.get_group('wojewódzkie')
# miejskie_wart_sal = miejskie_sale.groupby('Rok').agg({'Wartosc':['sum']}).values
# miejskie_wart_mie = miejskie_miejsca.groupby('Rok').agg({'Wartosc':['sum']}).values
# powiatowe2 = powiatowe.groupby('Rok').agg({'Wartosc':['sum']}).values
# wojewódzkie2 = wojewódzkie.groupby('Rok').agg({'Wartosc':['sum']}).values
# print(miejskie)
# print(miejskie2)
# print(miejskie_sale)
# print(miejskie_wart_sal)
# print(wojewódzkie2)

# plt.plot(x, miejskie_wart_sal, label="miejskie sale")
# plt.plot(x, miejskie_wart_mie, label="miejskie maijsca")
# plt.plot(x, wojewódzkie2, label="wojewódzkie")
# plt.xlabel('Rok')
# plt.ylabel('Wartość')
# plt.title('Ilość miejsc w kinach')
# # plt.text(2010,4, '129936')
# plt.legend()

# plt.savefig("zadanie2.png")
plt.show()

# df = pd.read_csv('sprzedaz4.csv', header=None, sep="@", decimal=".")
# df_1 = df.T
#
# print(df_1)
#
# grouped_df = df_1.groupby(0)
# grouped_list_label = grouped_df[1].apply(list)
# grouped_list_value = grouped_df[2].apply(list)
# # print(grouped_list_label)
# # print(grouped_list_value)
#
# grouped_list_label = grouped_list_label.reset_index()
# grouped_list_value = grouped_list_value.reset_index()
#
# grouped_label = grouped_list_label.T
# grouped_value = grouped_list_value.T
#
# grouped_label = grouped_label.reset_index()
# grouped_value = grouped_value.reset_index()
#
# grouped_value_gruszki= []
# for one_value in grouped_value[0][1]:
#     grouped_value_gruszki.append(int(one_value))
# grouped_gruszki_label = grouped_label[0][1]
# grouped_value_jablka= []
# for two_value in grouped_value[1][1]:
#     grouped_value_jablka.append(int(two_value))
# grouped_jablka_label = grouped_label[1][1]
# grouped_value_sliwki= []
# for three_value in grouped_value[2][1]:
#     grouped_value_sliwki.append(int(three_value))
# grouped_sliwki_label = grouped_label[0][1]
#
# print(grouped_value_jablka)
#
# # fig, (ax1,ax2,ax3) = plt.subplots()
# plt.plot(grouped_jablka_label,grouped_value_jablka, color = 'c')
# plt.plot(grouped_gruszki_label,grouped_value_gruszki, color = 'r')
# plt.plot(grouped_sliwki_label,grouped_value_sliwki)
#
#
# plt.show()



