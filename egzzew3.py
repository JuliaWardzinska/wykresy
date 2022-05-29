import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# wykres to samo co w zestawie 2

df_1 = pd.read_csv('ceny3.csv', header=None, sep="#", decimal=".")
plt.subplot()

grouped_df = df_1.groupby(0)
grouped_label = grouped_df[1].apply(list)
grouped_value = grouped_df[4].apply(list)

grouped_value_pierwotny = []
for one_value in grouped_value[0][1]:
    grouped_value_pierwotny.append(int(one_value.replace(" ", "")))

grouped_pierwotny_label = grouped_label[0][1]

print(grouped_value_pierwotny)
print(grouped_pierwotny_label)

# x = df4[0].unique()
# grupa = df4.groupby(by = df4[1])
# ryz = grupa.get_group('ryż - za 1kg')
# maka = grupa.get_group('mąka pszenna - za 1kg')
# ryz2 = ryz.groupby(df4[0]).agg({df4[4]:['sum']}).values
# maka2 = maka.groupby(df4[0]).agg({df4[4]:['sum']}).values
# plt.plot(x, ryz2, label="ryz")
# plt.plot(x, maka2, label="maka")

df_new = pd.DataFrame(grouped_value_pierwotny, index=grouped_pierwotny_label)

plt.plot(df_new)
plt.xlabel('Miesiące')
plt.ylabel('Cena')
plt.title('Cena produktów w danym roku')
plt.text(2017,2, '129936')
plt.legend()
plt.savefig("zadanie2.png")
plt.show()