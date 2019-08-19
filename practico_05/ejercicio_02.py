# Implementar los metodos de la capa de datos de socios.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Socio


class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def crear_tabla(self):
        Socio.__table__.create()

    def borrar_tabla(self):
        Socio.__table__.drop()

    def buscar(self, id_socio):
        socio=self.session.query(Socio).filter(Socio.id==id_socio).first()
        return socio

    def buscar_dni(self, dni_socio):
        socio=self.session.query(Socio).filter(Socio.dni==dni_socio).first()
        return socio

    def todos(self):
        socios=self.session.query(Socio).all()
        return socios

    def borrar_todos(self):
        self.session.query(Socio).delete()
        self.session.commit()
        socios=self.session.query(Socio).all()
        if socios is None:
            return True
        else:
            return False

    def alta(self, socio):
        self.session.add(socio)
        self.session.commit()
        return socio

    def baja(self, id_socio):
        socio=self.session.query(Socio).filter(Socio.id==id_socio).first()
        if (socio is None):
            return False
        else:
            self.session.delete(socio)
            self.session.commit()
            return True

    def modificacion(self, socio):
        self.session.query(Socio).filter(socio.id==Socio.id).\
            update({Socio.nombre:socio.nombre,Socio.apellido:socio.apellido,Socio.dni:socio.dni})
        self.session.commit()
        socio=self.session.query(Socio).filter(socio.id==Socio.id).first
        return socio

def pruebas():

    # alta
    datos = DatosSocio()

    #Creo la tabla para poder ejecutar las pruebas
    datos.crear_tabla()

    socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    assert socio.id > 0

    # baja
    assert datos.baja(socio.id) == True

    # buscar
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id) == socio_2

    # buscar dni
    assert datos.buscar_dni(socio_2.dni) == socio_2

    # modificacion
    socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    socio_3.nombre = 'Moria'
    socio_3.apellido = 'Casan'
    socio_3.dni = 13264587
    datos.modificacion(socio_3)
    socio_3_modificado = datos.buscar(socio_3.id)
    assert socio_3_modificado.id == socio_3.id
    assert socio_3_modificado.nombre == 'Moria'
    assert socio_3_modificado.apellido == 'Casan'
    assert socio_3_modificado.dni == 13264587

    # todos
    assert len(datos.todos()) == 2

    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0

    #Borro la tabla para poder ejecutar nuevamente, caso contrario, tiraría error el crear tabla porque la misma ya existe
    datos.borrar_tabla()

if __name__ == '__main__':
    pruebas()
