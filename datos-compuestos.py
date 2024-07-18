# Lista
lista = ["Luis Oviedo","tecnotutoriales Jheyson galvis", True, 1.83]
print(lista[1])
lista[3] = "LuisFer"
print(lista[3])

#La tupla es una lista que no se puede modificar
tupla= ("Luis Oviedo","tecnotutoriales Jheyson galvis", True, 1.83)
print(tupla[1])
#creando un conjunto
#Un conjunto no admite elementos duplicados
set = {"Luis Oviedo","tecnotutoriales Jheyson galvis", True, 1.83,1.83}
print(set)
# creando un Map o Diccionario
map = {
    "nombre": "Luis",
    "apellido": "Oviedo",
    "canal de youtube": "tecnotutoriales Jheyson galvis",
    "esta feliz": True,
    "estatura": 1.83}
print(map["esta feliz"])
print(map["nombre"])
print(map["apellido"])