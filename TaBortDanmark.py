lista = {"Danmark":"Köpenhamn","Sverige":"Stockholm"}

print(lista)

läggTillLand = input("Lägg till land: ") 
läggTillStad = input("lägg till stad: ")
lista.update({läggTillLand:läggTillStad})

print(lista)

tabort = input("ta bort land: ")

if (tabort in lista):
    lista.pop(tabort)
    print(lista)

else:
    print("NO STOP")
