class Persona:
    def __init__(self, nombre = "", edad = 0, sexo = ""):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_edad(self):
        return self.__edad
    def set_edad(self, edad):
        self.__edad = edad
    
    def get_sexo(self):
        return self.__sexo
    def set_sexo(self, sexo):
        self.__sexo = sexo
    
    def completar_sexo(self):
        if self.get_sexo() == "M":
            return "Masculino"
        if self.get_sexo() == "F":
            return "Femenino"
        return "Otro"
    
    def __str__(self) -> str:
        s = f"Nombre: {self.__nombre}" + "\n"
        s = s + f"Edad: {self.__edad}" + "\n"
        s = s + f"Sexo: {self.completar_sexo()}" + "\n"
        return s
        
        