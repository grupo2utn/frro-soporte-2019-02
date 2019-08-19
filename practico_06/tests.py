# Implementar los casos de prueba descriptos.
import sys

sys.path.append("C:\\Users\\Gabriel\\Documents\\GitHub\\frro-soporte-2019-02\\practico_05")

import unittest

from ejercicio_01 import Socio
from capa_negocio import NegocioSocio, LongitudInvalida, MaximoAlcanzado, DniRepetido


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_tabla()

    def test_alta(self):
        self.ns.crear_tabla()
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        self.ns.crear_tabla()
        #Agrego un socio
        socio=Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        # valida regla
        valido = Socio(dni=11111111, nombre='Juan', apellido='Perez')
        self.assertFalse(self.ns.regla_1(valido))

        # dni repetido
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertRaises(DniRepetido, self.ns.regla_1, invalido)

    def test_regla_2_nombre_menor_3(self):
        self.ns.crear_tabla()
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Ju', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        self.ns.crear_tabla()
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juannnnnnnnnnnnnnnnn', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        self.ns.crear_tabla()
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Pe')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        self.ns.crear_tabla()
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perezzzzzzzzzzzzzzzzz')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        self.ns.crear_tabla()
        #Agrego un socio
        socio=Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        #Valido la regla
        self.assertFalse(self.ns.regla_3())

    def test_baja(self):
        self.ns.crear_tabla()
        #Agrego un socio
        socio=Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        #Pruebo la baja del socio agregado
        self.assertTrue(self.ns.baja(socio.id))

    def test_buscar(self):
        self.ns.crear_tabla()
        #Agrego un socio
        socio=Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        #Pruebo la busqueda por id del socio agregado
        self.assertTrue(self.ns.buscar(socio.id)==socio)

    def test_buscar_dni(self):
        self.ns.crear_tabla()
        #Agrego un socio
        socio=Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        #Pruebo la busqueda por dni del socio agregado
        self.assertTrue(self.ns.buscar_dni(socio.dni)==socio)

    def test_todos(self):
        self.ns.crear_tabla()
        #Agrego dos socios
        socio1=Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio1)
        socio2=Socio(dni=11111111, nombre='Martin', apellido='Perez')
        self.ns.alta(socio2)

        #Pruebo la función todos
        self.assertTrue(len(self.ns.todos())==2)

    def test_modificacion(self):
        self.ns.crear_tabla()
        socio_3 = self.ns.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
        socio_3.nombre = 'Moria'
        socio_3.apellido = 'Casan'
        socio_3.dni = 13264587
        self.ns.modificacion(socio_3)
        socio_3_modificado = self.ns.buscar(socio_3.id)
        self.assertTrue(socio_3_modificado.id == socio_3.id)
        self.assertTrue(socio_3_modificado.nombre == 'Moria')
        self.assertTrue(socio_3_modificado.apellido == 'Casan')
        self.assertTrue(socio_3_modificado.dni == 13264587)
