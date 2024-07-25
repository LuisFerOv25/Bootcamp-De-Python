colores = {"1": "Amarillo", "2": "Azul", "3": "Rojo", "4": "Otro"}
colorFav = int(input("Ingresa tu color favorito (1 - Amarillo, 2 - Azul, 3 - Rojo, 4 - Otro ): "))

if colorFav == 1:
   color = colores["1"]
elif colorFav == 2:
  color= colores["2"]
elif colorFav =="3":
  color= colores["3"]
else:
  color = colores["4"]
  
print(f"El color elegido es: {color}")