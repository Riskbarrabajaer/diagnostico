class ManejoPersonal:
    def __init__(self, personal = []):
        self.__personal = personal
        
    def odtener_numeros(self):
        inge = 0
        abogados = 0
        otros = 0
        sueldo = 0
        for i in self.__personal:
            match i.get_profesion():
                case "I":
                    inge += 1
                case "A":
                    abogados +=1
                case "O":
                    otros += 1
            sueldo = sueldo + i.get_sueldo()
        return inge,abogados,otros,sueldo
    def sacar_procentajes (self, total, grupo):
        return (grupo / total) * 100
    def mostrar_datos(self):
        i,a,o,s = self.odtener_numeros()
        n_personal = len(self.__personal)
        print(f"el porcentage de ingenieros {self.sacar_procentajes(n_personal, i) }")
        print(f"el porcentage de Abogado {self.sacar_procentajes(n_personal, a) }")
        print(f"el porcentage de Otros profesionales {self.sacar_procentajes(n_personal, o)}")
        print(f"el promedio de sueldos es {s / n_personal}")