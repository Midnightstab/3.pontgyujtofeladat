homerseklet= [0,12,13,9,2,7]


i  = 0

while i < len(homerseklet) -1:
    if (homerseklet[i] - homerseklet[i + 1] > 3):
        print(f"{i + 2}. napra")
    # elágazás vége
    i += 1
# ciklus vége

""" Csak az első olyan napot írja ki, amikor 3-mal csökkent a hőmérséklet """

i = 0

while (i < len(homerseklet) - 1) and (homerseklet[i] - homerseklet[i + 1] <= 3):
    i +=1
# ciklus vége
# i = 2

if (i<len(homerseklet) - 1):
    print(f"{i+2}. napra ")
else:
    print(f"Nincs ilyen nap")


"""" ha az i = 1 """

i  = 1

while i < len(homerseklet):
    if (homerseklet[i-1] - homerseklet[i + 1] > 3):
        print(f"{i + 1}. napra")
    # elágazás vége
    i += 1
# ciklus vége




