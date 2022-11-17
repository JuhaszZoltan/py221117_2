karlanc:str = "hÖrCsÖg"

nagykezdobetus:str = karlanc.capitalize()
print(nagykezdobetus)

csupanagy:str = karlanc.upper()
print(csupanagy)

csupakicsi:str = karlanc.lower()
print(csupakicsi)

# karlanc = "Aa\tBb\tCc"
print(karlanc.expandtabs(0))
print(karlanc.endswith("sÖg"))
print(karlanc[-3:] == 'sÖg')

print(karlanc.startswith('h'))

ind:int = karlanc.find('sÖg')
print(ind)

print(karlanc.isalnum())

print(karlanc.replace('Ö', 'O'))

karlanc = "     12342143;Béla;Győr\n\t\t\t\t"
print(karlanc.strip().split(';')[1])


karlanc = karlanc.strip()
darabok:list[str] = karlanc.split(';')

print(darabok)

