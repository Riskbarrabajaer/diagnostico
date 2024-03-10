from entidades.Persona import Persona
class Profesional(Persona):
    def __init__(self, nombre="", edad=0, sexo="", profesion = "", sueldo = 0):
        super().__init__(nombre, edad, sexo)
        self.__profesion = profesion
        self.__sueldo = sueldo
    
    def get_profesion(self):
        return self.__profesion
    def set_profesion(self, profesion):
        self.__profesion = profesion
    
    def get_sueldo(self):
        return self.__sueldo
    def set_sueldo(self, sueldo):
        self.__sueldo = sueldo
    
    def completar_profesion(self):
        if self.get_profesion() == "I":
            return "Ingeniero"
        if self.get_profesion() == "A":
            return "Abogado"
        return "Otro"
    def __str__(self):
        s = super().__str__()
        s = s + f"Sueldo: {self.__sueldo}" + "\n"
        s = s + f"Profesion: {self.completar_profesion()}" + "\n"
        return s