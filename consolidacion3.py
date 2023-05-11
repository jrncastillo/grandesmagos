nombres = ["Harry Houdini", "David Blaine","Teller","Newton","Hawking","Einstein","Messi","Pele","Juanes"]

magos = ["Harry Houdini", "David Blaine","Teller"]
cientificos = ["Newton","Hawking","Einstein"]
otros = []

for item in nombres:
    if item not in magos and item not in cientificos:
        otros.append(item)

def hacer_grandioso(lista):
    mensaje = "El gran "
    grandesmagos = lista[:]
    for i in range(len(grandesmagos)):
        grandesmagos[i]=mensaje+grandesmagos[i]
    return grandesmagos

def imprimir_nombre(lista):
    for nombre in lista:
        print(nombre)

imprimir_nombre(nombres)
print("")
imprimir_nombre(hacer_grandioso(magos))
print("")
imprimir_nombre(cientificos)
print("")
imprimir_nombre(otros)