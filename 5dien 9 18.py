# uzd 1

x = int(input("ievadi skaitili "))

for i in range(1,11):
    print(f'{x} * {i} = {x*i}')

i = 1
while i<11:
    print(f'{x} * {i} = {x*i}')
    i = i + 1

# uzd 2

kautkas = "17-+01+-91-+-+--"

nezkas = kautkas.replace("-", "m").replace("+", "n").replace("n", "-").replace("m", "+")
print(nezkas)

# uzd 3

ievadi = input("ievadi virkni ")

neievadi = ievadi.__len__()
print("Ievadītās simbolu virknes", ievadi, "garums ir", neievadi)

# uzd 4

mhm = input("teikums ")

mhmne = len(mhm.split())
print("Ievadītājā simbolu virknē", mhm, "ir", mhmne, "vārdi")

# 5 uzd

import statistics

list = 8, 9, 1, 23, 15, 20, 19, 13, 8, 7, 5, 2, 7, 10, 14, 16

print(statistics.mean(list))

# 6 uzd

ja =  "necelšosi, necelšosi, miedziņš, nāk"

ne = tuple(ja.split())
print(ne)

# 7 uzd

lo = [27823, 9792, "sveiki", "cālīt", True, 7.6]
lt = ['cāļus', 'skaita', 'rudenī', 122, 5.3214, False, 'akmens']

for i in range(1,2):
    print(lo + lt)

# 8 uzd

import itertools

lo = [27823, 9792, "sveiki", "cālīt", True, 7.6]
lt = ['cāļus', 'skaita', 'rudenī', 122, 5.3214, False, 'akmens']

manapnik = itertools.chain(lo, lt)

print(*manapnik)

# 9 uzd 

from datetime import datetime

datuma_ievade = input("dzimene DD.MM.GGGG piemeram, 19.9.2024: ")
dzimsanas_datums = datetime.strptime(datuma_ievade, "%d.%m.%Y")
sodiena = datetime.now()
starpiba = sodiena - dzimsanas_datums

print(f"dienu skaits kops dzimsanas datuma: {starpiba.days} dienas.")

#  10 uzd



# 11 uzd

import math
v1 = 17.991
v2 = -991.0171

print("A) ar 2 zimem aiz komata:")
print(f"   {v1:.2f}")
print(f"   {v2:.2f}")

print("\nB) veseli skaitli")
print(f"   {int(v1)}")
print(f"   {int(v2)}")

print("\nC) dalskaitla laba puse:")
r1 = str(v1).split('.')[1]
r2 = str(v2).split('.')[1]
print(f"   {r1}")
print(f"   {r2}")

print("\nD) noapalosana ar math biblioteku:")
print(f" (uz augsu): {math.ceil(v1)} un {math.ceil(v2)}")
print(f" (uz leju): {math.floor(v1)} un {math.floor(v2)}")