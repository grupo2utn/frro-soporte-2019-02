from tkinter import ttk
from tkinter import *
import tkinter as tk

import sys

sys.path.append("C:\\Users\\Gabriel\\Documents\\GitHub\\frro-soporte-2019-02\\practico_05")
sys.path.append("C:\\Users\\Gabriel\\Documents\\GitHub\\frro-soporte-2019-02\\practico_06")

from capa_negocio import NegocioSocio
from ejercicio_01 import Socio

class SociosTK:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title('Manejo de Socios')

        frame = LabelFrame(self.ventana, text = 'Registrar nuevo socio')
        frame.grid(row = 0, column = 1, columnspan = 4, pady = 30)

        Label(frame, text = 'Dni: ').grid(row = 1, column = 0)
        self.dni = Entry(frame)
        self.dni.grid(row = 1, column = 1)

        Label(frame, text = 'Nombre: ').grid(row = 2, column = 0)
        self.nombre = Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row = 2, column = 1)

        Label(frame, text = 'Apellido: ').grid(row = 3, column = 0)
        self.apellido = Entry(frame)
        self.apellido.focus()
        self.apellido.grid(row = 3, column = 1)

        ttk.Button(frame, text = 'Cargar Socio', command = self.alta).grid(row = 4, columnspan = 2, sticky = W + E)

        self.tabla = ttk.Treeview(self.ventana, columns=('Dni', 'Nombre', 'Apellido'))
        self.tabla.heading('#0', text='IdSocio')
        self.tabla.heading('#1', text='Dni')
        self.tabla.heading('#2', text='Nombre')
        self.tabla.heading('#3', text='Apellido')
        self.tabla.column('#1', stretch=tk.YES)
        self.tabla.column('#2', stretch=tk.YES)
        self.tabla.column('#3', stretch=tk.YES)
        self.tabla.column('#0', stretch=tk.YES)
        self.tabla.grid(row=6, columnspan=6, sticky='nsew')

        ttk.Button(text = 'BORRAR', command = self.baja).grid(row = 5, column = 2, sticky = W + E)
        ttk.Button(text = 'EDITAR', command = self.modificacion).grid(row = 5, column = 3, sticky = W + E)

        self.todos()

    def alta(self):
        socio = Socio(dni=int(self.dni.get()), nombre=str(self.nombre.get()), apellido=str(self.apellido.get()))
        NegocioSocio().alta(socio)
        self.todos()

    def baja(self):
        self.id = self.tabla.item(self.tabla.selection())['text']
        NegocioSocio().baja(int(self.id))
        self.todos()

    def modificacion(self):
        id = self.tabla.item(self.tabla.selection())['text']
        self.modificacion_vent = Toplevel()
        self.modificacion_vent.title = 'Modificación de Socio'

        Label(self.modificacion_vent, text = 'Nuevo Dni:').grid(row = 1, column = 1)
        nuevo_dni = Entry(self.modificacion_vent)
        nuevo_dni.grid(row = 1, column = 2)

        Label(self.modificacion_vent, text = 'Nuevo Nombre:').grid(row = 2, column = 1)
        nuevo_nombre= Entry(self.modificacion_vent)
        nuevo_nombre.grid(row = 2, column = 2)

        Label(self.modificacion_vent, text = 'Nuevo Apellido:').grid(row = 3, column = 1)
        nuevo_apellido= Entry(self.modificacion_vent)
        nuevo_apellido.grid(row = 3, column = 2)

        Button(self.modificacion_vent, text = 'Actualizar', command = lambda: self.realizar_modificacion(id, nuevo_dni.get(), nuevo_nombre.get(), nuevo_apellido.get())).grid(row = 4, column = 2, sticky = W)
        self.modificacion_vent.mainloop()

    def realizar_modificacion(self, id, dni, nombre, apellido):
        socio=Socio(id=id, dni=int(dni), nombre=nombre, apellido=apellido)
        NegocioSocio().modificacion(socio)
        self.modificacion_vent.destroy()
        self.todos()

    def todos(self):
        records = self.tabla.get_children()
        for element in records:
            self.tabla.delete(element)
        socios = NegocioSocio().todos()
        for i in socios:
            self.tabla.insert('', 0, text = i.id, values = (i.dni, i.nombre, i.apellido))

if __name__ == '__main__':
    window = Tk()
    application = SociosTK(window)
    window.mainloop()
