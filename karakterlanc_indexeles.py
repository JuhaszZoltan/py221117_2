karlanc:str = "Hörcsög"

# str első karaktere (0-ás indexű)
print(karlanc[0])
# str 1es indexű karakterétől az str 4-es indexű karakteréig
# (zárt -> NYÍLT, tehát 1, 2, 3)
print(karlanc[1:4])
# str végéről első karakter
print(karlanc[-1])
# str elejérő 1es indexűtől az utolsóig,
# DE továbbra is zárt-> NYÍLT, tehát 1, 2, 3, 4, 5
print(karlanc[1:-1])
# a nulla elhagyható
# ez a str utolsó kivételével összes karaktere:
print(karlanc[:-1])

# itt is van OoR exception:
# print(karlanc[100])

karakterek_szama = len(karlanc)
print(karakterek_szama)