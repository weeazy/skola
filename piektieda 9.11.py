# uzd 1

x = int(input("ievadi nr: "))

y = int(input("ievadi nr: "))

print(x/y)

# uzd 2

street = input("ievadi ielu: ")

pet = input("ievadi dzivnieku: ")

print(f"{street} {pet}")

# uzd 3

c = 3
d = 6

multiply = c * d

print(multiply)

if multiply > d:
    print("reizinajums lielaks par reizinataju")

else: print("reizinajums mazaks par reizinataju")

# uzd 4

l = int(input("ievadi konstanti "))

if l < 0: 
    print("konstante ir negativa ", l)

elif l > 0:
    print("konstante ir pozitiva ", l)

elif l == 0:
    print("konstante ir  ", l)

# uzd 5

l = 169
k = -374
e = 0

def checkNumber(l):
    if l < 0: 
        print("konstante ir negativa ", l)

    elif l > 0:
        print("konstante ir pozitiva ", l)

    elif l == 0:
        print("konstante ir  ", l)

checkNumber(l)
checkNumber(k)
checkNumber(e)

# uzd 6

z = int(input("ievadi skaitli "))

def checkNumber2(z):

    if (z % 2) == 0:
        print(f"{z} para skaitlis")
    else:
        print(f"{z} nepara skaitlis")

checkNumber2(z)

# uzd 7

g = int(input("ievadi skaitli "))
h = int(input("ievadi skaitli "))


for i in range(g, h + 1):
    print(i)

# uzd 8

k = int(input("ievadi skaitli "))
v = int(input("ievadi skaitli "))

sum = sum(range(k, v + 1))

print(sum)

# uzd 9

r = int(input("ievadi skaitli "))
t = int(input("ievadi skaitli "))


for i in range(r, t + 1):
    if (i % 2) == 0:
        print(i)

# uzd 10

kristaps = int(input("ievadi skaitli "))
upenieks = int(input("ievadi skaitli "))

for i in range(1, 7):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# uzd 11

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print("")

# uzd 12

skolotajs = int(input("ievadi skaitli "))
skolotajs2 = int(input("ievadi skaitli "))

for i in range(skolotajs, skolotajs2 + 1):
    if (i % 5) > 0:
        print(i)

# uzd A

salaries = {
"John": 100,
"Ann": 160,
"Bob": 130
}

salary = sum(salaries.values())

print(salary)

# uzd b

menu = {
"width": 100,
"height": 200,
"title": "My menu"
}

def multiplyNumeric(x):

    for value in x.items():
        if isinstance(value, int):
            print(value * 4)

multiplyNumeric(menu)

print(menu)