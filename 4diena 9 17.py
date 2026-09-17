# 1 uzd 

teksts = "Labrīt@es@esmu@pirmais@uzdevums"
a = teksts.split("@")
b = " ".join(a)
print(b)

# 2 uzd

c = "Labrīt@es@esmu@pirmais@uzdevums"
d = teksts.split("@")

f = "-".join(c)
print(f)

# 3 uzd

g = ["šodien", "ir", "skaista", "diena"]

g.sort()
print("sakkrtotais saraksts", g)

# 4 uzd 

k = "is it friday"

j = k.split()
print("sakotnejais saraksts", j)

j.sort()
print("sakartotais saraksts", j)

# 5 uzd

saraksts = ["abols", "bumbieris", "apelsins", "citrons", "banans"]
vajag = "apelsins"

if vajag in saraksts:
    print("teksta virkne atrodas saraksta")
else:
    print("teksta virkne neatrodas saraksta")

# 6 uzd

saraksts = ["Mans", "vārds", "nav", "Rihards", "mans", "vārds", "ir"]

mans = [y.lower() for y in saraksts].count("mans")
vards = [y.lower() for y in saraksts].count("vārds")

print(f'simbolu virkne "Mans" sarakstā satopams {mans} reizes')
print(f'Simbolu virkne "vārds" sarakstā satopams {vards} reizes')

# 7 uzd

saraksts = ["viens", "divi", "tris"]

saraksts.reverse()
print("saraksts otradi", saraksts)

# 8 uzd

sakums = ["viens", "divi", "trīs"]

otradi = sakums[::-1]

print("saraksts sakuma", sakums)
print("saraksts otradi:", otradi)

# 9 uzd 

saraksts = ["hello", "this", "skyscraper", "is", "named", "sparta"]

nepara_vards_saraksta = saraksts[::2]

print("nepara vardi ", nepara_vards_saraksta)

# 10 uzd

sarakstsss1 = ["masina", "traktors", "lidmasina"]
sarakstsss2 = ["maja", "telts", "dzivokls", "nojume"]

kopejais_saraksts = sarakstsss1 + sarakstsss2

print(kopejais_saraksts)

# 11 uzd

sarakstsssssss = "mūsdienu", "cienījamā", "kukurūzas", "māja"

for vards in sarakstsssssss:
    print(vards, end=" ")
print()

print (*sarakstsssssss)

# 12 uzd

sarakstins = [ "cranberry", "why", "are", "you", "wading", "in", "the", "swamp" ]

sarakstins.sort(reverse=True)

for v in sarakstins:
    print(v)

# 13 uzd

from collections import Counter

sarakstinsJA = [ "sveiki", "labdien", "sveiki", "labdien", "sveiki", "kaijas"
                , "cienījamais", "dzīvot", "cienījamais", "mūsdienu"
                , "mūsdienu", "cienījamais", "kukurūza", "māja"
                , "sveiciens", "dzīvot", "mūsdienu", "dzīvot", "sveiciens", "māja" ]

analize = Counter(sarakstinsJA)
for v in analize.keys():
    print(v)

sarakstinsNE = [ "sveiki", "labdien", "sveiki", "labdien", "sveiki", "kaijas"
                , "cienījamais", "dzīvot", "cienījamais", "mūsdienu"
                , "mūsdienu", "cienījamais", "kukurūza", "māja"
                , "sveiciens", "dzīvot", "mūsdienu", "dzīvot", "sveiciens", "māja" ]

analize = Counter(sarakstinsNE)

for v, s in analize.items():
    print(f"simbol virkne {v} saraksta var redzet = {s}")