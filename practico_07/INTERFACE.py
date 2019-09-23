from tkinter import *
from tkinter import ttk
import sys
import tkinter as tk

sys.path.append("C:\\Users\\Gabriel\\Documents\\GitHub\\frro-soporte-2019-02\\practico_05")
sys.path.append("C:\\Users\\Gabriel\\Documents\\GitHub\\frro-soporte-2019-02\\practico_06")

from capa_negocio import NegocioSocio
from ejercicio_01 import Socio, Base, engine


class Interfaz:
    def __init__(self, ventana):
        Base.metadata.bind = engine
        self.ventana = ventana
        self.ventana.title("Carga de Socios")
        self.ventana.geometry('825x285+600+200')
        self.ventana.config(background="light blue")
        self.ventana.resizable(0, 0)

        self.formulario = ttk.Treeview(self.ventana, columns=("nombre", "apellido", "dni"), selectmode=tk.BROWSE)
        self.formulario.heading("#0", text="Id")
        self.formulario.heading("nombre", text="Nombre")
        self.formulario.heading("apellido", text="Apellido")
        self.formulario.heading("dni", text="DNI")
        self.formulario.place(x=10, y=10)


        self.marco = tk.Frame(self.ventana)
        self.marco.place(y=240, x=10, width=801)
        self.marco.config(background="light blue")

        self.btnAlta = tk.Button(self.marco, text="Ingresar", width=6, command=self.alta)
        self.btnAlta.grid(row=0, column=0)
        self.btnBaja = tk.Button(self.marco, text="Eliminar", width=6, command=self.baja)
        self.btnBaja.grid(row=0, column=1, padx=3)
        self.btnModificar = tk.Button(self.marco, text="Modificar", width=7, command=self.modificacion)
        self.btnModificar.grid(row=0, column=2)

        self.mostrar_todos()


    def mostrar_todos(self):
        records = self.formulario.get_children()
        for element in records:
            self.formulario.delete(element)
        socios= NegocioSocio().todos()
        for socio in socios:
            self.formulario.insert("", tk.END, text=socio.IdSocio, values=(socio.Nombre, socio.Apellido, socio.DNI))

    def alta(self):
        id_soc = tk.IntVar
        nombre = tk.StringVar()
        apellido = tk.StringVar()
        dni = tk.StringVar()
        self.alta_window = tk.Toplevel()
        self.alta_window.title("Ingresar Socio")
        self.alta_window.geometry('285x138+625+400')
        self.alta_window.resizable(0, 0)

        label = tk.Label(self.alta_window, text="Id")
        label.grid(row=0, column=0, padx=20)
        entryId = tk.Entry(self.alta_window, textvariable=id_soc, width=20)
        entryId.grid(row=0, column=1, pady=5)

        label = tk.Label(self.alta_window, text="Nombre")
        label.grid(row=1, column=0, padx=20)
        entryNomb = tk.Entry(self.alta_window, textvariable=nombre, width=20)
        entryNomb.grid(row=1, column=1)

        label = tk.Label(self.alta_window, text="Apellido")
        label.grid(row=2, column=0, padx=20)
        entryApel = tk.Entry(self.alta_window, textvariable=apellido, width=20)
        entryApel.grid(row=2, column=1, pady=5)

        label = tk.Label(self.alta_window, text="Dni")
        label.grid(row=3, column=0, padx=20)
        entryDNI = tk.Entry(self.alta_window, textvariable=dni, width=20)
        entryDNI.grid(row=3, column=1)

        btnAceptar = tk.Button(self.alta_window, text='Aceptar', command=lambda: self.agregar(entryId.get(), entryNomb.get(), entryApel.get(), entryDNI.get()))
        btnAceptar.grid(row=4, column=0, padx=10, pady=5)
        btnCancelar = tk.Button(self.alta_window, text='Cancelar', command=self.alta_window.destroy)
        btnCancelar.grid(row=4, column=1, padx=10, pady=5)

    def agregar(self, id_socio, nombre, apellido, dni):
        if (id_socio != "") and (nombre != "") and (apellido != "") and (dni != ""):
            self.formulario.insert("", tk.END, text=id_socio, values=(nombre, apellido, dni))
            self.formulario.place(x=10, y=10)
            self.alta_window.destroy()

    def baja(self):
        seleccion = self.formulario.selection()
        id_socio = self.formulario.item(seleccion, option="text")
        if id_socio != "":
            self.baja_window = tk.Toplevel()
            self.baja_window.title("Eliminar Socio")
            self.baja_window.geometry('285x65+625+400')
            self.baja_window.resizable(0, 0)
            label = tk.Label(self.baja_window, text="¿Desea eliminar este socio?")
            label.grid(row=0, columnspan=2, padx=20, pady=(5, 0))
            btnAceptar = tk.Button(self.baja_window, text='Aceptar', command=lambda: self.borrar(seleccion))
            btnAceptar.grid(row=5, column=0, padx=10, pady=5)
            btnCancelar = tk.Button(self.baja_window, text='Cancelar', command=self.baja_window.destroy)
            btnCancelar.grid(row=5, column=1, padx=10, pady=5)

    def borrar(self, socio):
        self.formulario.delete(socio)
        self.formulario.place(x=10, y=10)
        self.baja_window.destroy()

    def modificacion(self):
        seleccion = self.formulario.selection()
        id_socio= self.formulario.item(seleccion, option="text")
        if id_socio !="":
            self.modifica_window = tk.Toplevel()
            self.modifica_window.title("Modificar Socio")
            self.modifica_window.geometry('235x150+625+400')
            self.modifica_window.resizable(0, 0)
            nombre = tk.StringVar()
            apellido = tk.StringVar()
            dni = tk.StringVar()

            label = tk.Label(self.modifica_window, text="Id: "+id_socio)
            label.grid(row=0, column=0, padx=20)

            label = tk.Label(self.modifica_window, text="Nombre")
            label.grid(row=1, column=0, padx=20)
            entryNomb = tk.Entry(self.modifica_window, textvariable=nombre, width=20)
            entryNomb.grid(row=1, column=1)

            label = tk.Label(self.modifica_window, text="Apellido")
            label.grid(row=2, column=0, padx=20)
            entryApel = tk.Entry(self.modifica_window, textvariable=apellido, width=20)
            entryApel.grid(row=2, column=1, pady=5)

            label = tk.Label(self.modifica_window, text="Dni")
            label.grid(row=3, column=0, padx=20)
            entryDNI = tk.Entry(self.modifica_window, textvariable=dni, width=20)
            entryDNI.grid(row=3, column=1)

            btnAceptar = tk.Button(self.modifica_window, text='Aceptar', command=lambda: self.modificar(seleccion, entryNomb.get(), entryApel.get(), entryDNI.get()))
            btnAceptar.grid(row=4, column=0, padx=10, pady=5)
            btnCancelar = tk.Button(self.modifica_window, text='Cancelar', command=self.modifica_window.destroy)
            btnCancelar.grid(row=4, column=1, padx=10, pady=5)

    def modificar(self, elemento, nombre, apellido, dni):
        if (nombre != "") and (apellido != "") and (dni != ""):
            self.formulario.item(elemento, values=(nombre, apellido, dni))
            self.formulario.place(x=10, y=10)
            self.modifica_window.destroy()


root = tk.Tk()
app = Interfaz(root)
root.mainloop()
