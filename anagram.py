#!/usr/bin/python3
# -*- coding:utf-8 -*-

def anagramma(szo1):
    return sorted(list(szo1))


print("1. feladat")
"""Szoveget bekerni es meghatarozni hogy hany kulonbozo elemet tartalmaz az adott szoveg. """
szoveg_bekeres = set(list(input("Adja meg a szoveget: ")))
print("A beirt szoveg {} kulonbozo karaktert tartalmaz".format(len(szoveg_bekeres)))

print("2. feladat")
"""Szavak beolvasasa a szotar.txt--bol es eltarolasa amit en szotarban oldanak meg. Ami a kovetkezo keppen nezne ki:
szotar{
hanyadik szo{
"Szo"=eszesen
"szo karakterekent" = [e,s,z,e,s,e,n]
 }
}
"""
szotar = {}
n = 0
sortor = []
with open("szotar.txt", "rt+", encoding="ASCII") as f:
    for s in f:
        n+=1
        sor = s.replace("\n","")
        szotar[n] = {}
        szotar[n]["szo"] = sor
        szotar[n]["anagramma"] = anagramma(sor)
        for sz in sor:
            sortor.append(sz)
            szotar[n]["szo karakterenkent"] = sortor
        sortor = []

#print(szotar)
print("3. feladat")
"""Minden szo karaktereit egyenkent abc sorrendbe kell tenni es ezt ki kell irni a abc.txt alomanyba.(minden sorhoz kell tartoznia egy erteknek) """
with open("abc.txt", "wt", encoding="ASCII") as f:
    for szo in szotar.values():
        f.write(str(sorted(szo["szo karakterenkent"]))+"\n")

print("4. feladat")
"""Be kell kerni a felhasznalotol 2 szot es meg kell hataronzi hogy anagramma-e egymasnak a ket szo."""
szobekeres1 = list(input("Kerem adja meg az elso vizsgalt szot: "))
szobekeres2 = list(input("Kerem adja meg a masodik vizsgalt szot: "))
szo1 = anagramma(szobekeres1)
szo2 = anagramma(szobekeres2)
if szo1 == szo2:
    print("Anagramma")
else:
    print("Nem anagramma")


print("5. feladat")
"""Felhasznalotol egy szo bekeres es az allomany szavaibol megkeresni hogy ha van talalat akkor egymas ala kiirni."""   
szokereso = list(input("Kerem irjon be egy szot aminek az anagrammajat megkeresi a szotar alomanyban: "))
anagrammak = []
n = 0
for a in szotar.values():
    if anagramma(szokereso) == a["anagramma"]:
        print(a["szo"])
        n+=1
if n == 0:
    print("Nincs a szotarban anagramma.")

print("6. feladat")
"""Meg kell hatarozni hogy a szotar allomanyban melyik a leghosszabb szo es ki kell iratni a kepenyore """
szotarleghosszabb = {}
for k,v in szotar.items():
    szotarleghosszabb[k] = len(v["szo"])
for d,f in szotarleghosszabb.items():
    if f == int(max(sorted(szotarleghosszabb.values()))):
        for k in szotar.keys():
            if k == d:
                print(szotar[k]["szo"])

print("7. feladat")
"""karakter szam szerinti novekvo sorrendbe rendezes, egymas amagramma szavai keruljenek egy sorba szokozzel elvalasztva nem ugyanaz a karaktert \
tartalmazo lista szamvai keruljenek egy sorba kulonboyo hasszusagu szavak egy sor sortoressel keruljenek az alomanyba  """
elozo_hossza = int()
elozo_szo = str()
liest = []
df = []
with open("rendezve.txt","wt", encoding="ASCII") as f:
    for k in szotar.values():
        for a in range(2, int(max(sorted(szotarleghosszabb.values())))):
            if len(k["szo"]) == a:      
                if str(k["anagramma"]) == elozo_szo:
                    df.append(k['szo'])
                else:
                    print(k['szo'])
                    elozo_szo = str(k["anagramma"])
                print(df)
            else:
                df = []
