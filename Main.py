from entidades.Profesional import *
from entidades.ManejoPersonal import ManejoPersonal
def solicitar_datos1():
    while True:
        print("desea ingresar mas datos S/N")
        r =input("Respuesta:")
        if r == "S":
            return 1
        elif r == "N":
            return 2
        else:
            print("Ingrese una respuesta valida")

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
        sexo = input("Ingrese su sexo (Masculino = M/Femenino = F): ").title()
        if sexo not in ["M", "F"]:
            print("Por favor, ingrese 'Masculino' o 'Femenino'.")
        else:
            break
    
    while True:
        profesion = input("Ingrese su profesión (I = ingeniero/A = abogado/O = Otra): ").title()
        if profesion not in ["I", "A", "O"]:
            print("Por favor, seleccione entre Ingeniero, Abogado u Otra.")
        else:
            break
    while True:
        try:
            sueldo = int(input("Ingrese su edad (número entero mayor a 0): "))
            if edad <= 0:
                print("La edad debe ser un número entero mayor a 0.")
                continue
            break
        except ValueError:
            print("Ingrese un número entero válido para la edad.")
    
    return nombre, edad, sexo, profesion, sueldo
condicion = 1
lista = []
personal = ManejoPersonal(lista)
while condicion != 2:
    print("Bienvenido al registro de personal")
    nombre, edad, sexo, profesion, sueldo = solicitar_datos()
    Nuevo_pro = Profesional(nombre, edad, sexo, profesion, sueldo)
    print(Nuevo_pro)
    lista.append(Nuevo_pro)
    condicion = solicitar_datos1()
personal.mostrar_datos()
    

