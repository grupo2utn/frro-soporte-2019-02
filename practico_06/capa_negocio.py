# Implementar los metodos de la capa de negocio de socios.


import sys

sys.path.append("C:\\Users\\Gabriel\\Documents\\GitHub\\frro-soporte-2019-02\\practico_05")
#print (sys.path)

from ejercicio_01 import Socio
from ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def crear_tabla(self):
        Socio.__table__.create()

    def borrar_tabla(self):
        Socio.__table__.drop()

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        return self.datos.buscar(id_socio)

    def buscar_dni(self, dni_socio):
        return self.datos.buscar_dni(dni_socio)

    def todos(self):
       return self.datos.todos()

    def alta(self, socio):
        if(self.regla_1(socio)==False):
            if(self.regla_2(socio)==True):
                if(self.regla_3()==False):
                    return self.datos.alta(socio)
                else:
                    return False
            else:
                return False
        else:
           return False

    def baja(self, id_socio):
        return self.datos.baja(id_socio)

    def modificacion(self, socio):
        if(self.regla_2(socio)==True):
            return self.datos.modificacion(socio)
        else:
            raise LongitudInvalida("LONGITUD INVALIDA.")

    def regla_1(self, socio):
        encontrado=self.datos.buscar_dni(socio.dni)
        if (encontrado is not None):
            raise DniRepetido("DNI REPETIDO.")
        else:
            return False

    def regla_2(self, socio):
        if((len(socio.nombre)>=self.MIN_CARACTERES) and (len(socio.nombre)<=self.MAX_CARACTERES) and
                (len(socio.apellido)>=self.MIN_CARACTERES) and (len(socio.apellido)<=self.MAX_CARACTERES)):
            return True
        else:
            raise LongitudInvalida("LONGITUD INVALIDA.")

    def regla_3(self):
        cantidad=len(self.datos.todos())
        if(cantidad==200):
            raise MaximoAlcanzado("MAXIMA CANTIDA DE SOCIOS ALCANZADA.")
        else:
            return False
