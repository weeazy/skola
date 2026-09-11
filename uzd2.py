x = int(input("ievadi skaitli "))
print(x*2)

if x < 18:
    print("mazak par 18")

elif x > 18:
    print("lielaks par 18")

elif x == 18:
    print("tieshi 18")

y = int(input("ievadi sekundes"))

print(y/60, ("minutes"))
print(y/60/60, ("stundas"))

import datetime

m = int(input("Ievadi sekundes: "))

laika_nobide = datetime.timedelta(seconds=m)

print("Laiks ar datetime", laika_nobide)