a = input("ievadi virkni 1: ")
b = input("ievadi virkni 2: ")

kkasa = 0
kkasb = 0

for i in a:
    kkasa = kkasa + 1

for i in b:
    kkasb = kkasb +  1
    
if kkasa > kkasb:
    print("Virkne", a, "ir garaka par virkni", b)
elif kkasa < kkasb:
    print("Virkne", b, "ir garaka par virkni", a)
elif kkasa == kkasb:
    print("Virkne", a, "ir vienada ar virkni", b)