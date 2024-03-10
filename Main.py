from entidades.Profesional import *
from entidades.ManejoPersonal import ManejoPersonal

hyli = Profesional("hily", 28, "M", "I", 20)
upset = Profesional("upset", 23, "F", "O", 212)
personal = ManejoPersonal([upset, hyli])
personal.mostrar_datos()


