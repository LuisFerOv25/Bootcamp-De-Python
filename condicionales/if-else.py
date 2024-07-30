# edad = 17
# if edad >= 18:
#     print("Puedes pasar")
# else: 
#     print("Eres menor de edad, no puedes pasar")

# contrasena_almacenada = "JheysonGalvis"
# contrasena_escrita = "JheysonGalvis"
# if contrasena_almacenada == contrasena_escrita:
#     print("Hay coincidencia")
# else: 
#     print("No hay coincidencia")
ingreso_mensual = 12000
ahorro_mensual = 6000
if ingreso_mensual > 10000:
    if ahorro_mensual < 7000:
        print('Ahora si estas bien')
    else:
        print('Estas gastando mucho, ahorra mas')
elif ingreso_mensual > 1000:
   print('estas bien en latinoamerica')
elif ingreso_mensual > 500:
    print('estas bien en Colombia')
elif ingreso_mensual > 200:
    print('estas bien en Peru')
else:
    print('estas en la pobreza')