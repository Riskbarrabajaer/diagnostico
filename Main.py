from entidades.Profesional import *
from entidades.ManejoPersonal import ManejoPersonal

def solicitar_datos():
    nombre = input("Ingrese su nombre: ").title()
    while True:
        try:
            edad = int(input("Ingrese su edad (número entero mayor a 0): "))
            if edad <= 0:
                print("La edad debe ser un número entero mayor a 0.")
                continue
            break
        except ValueError:
            print("Ingrese un número entero válido para la edad.")
    
    while True:
        sexo = input("Ingrese su sexo (Masculino/Femenino): ").title()
        if sexo not in ["Masculino", "Femenino"]:
            print("Por favor, ingrese 'Masculino' o 'Femenino'.")
        else:
            break
    
    while True:
        profesion = input("Ingrese su profesión (Ingeniero/Abogado/Otra): ").title()
        if profesion not in ["Ingeniero", "Abogado", "Otra"]:
            print("Por favor, seleccione entre Ingeniero, Abogado u Otra.")
        else:
            break
    
    return nombre, edad, sexo, profesion

nombre, edad, sexo, profesion = solicitar_datos()
print("Nombre:", nombre)
print("Edad:", edad)
print("Sexo:", sexo)
print("Profesión:", profesion)



