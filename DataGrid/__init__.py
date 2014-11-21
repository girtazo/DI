# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
from gi.repository import Gtk
import sqlite3
from pprint import pprint


baseDatos = 'tEjercicio'


class Tabla :
	"""Enlaza con la tabla indicada"""
	def __init__(self,baseDatos,nombre):
		self.nombre = nombre;
		self.baseDatos =baseDatos
		self.conexion = sqlite3.connect(baseDatos)
		self.cursor = self.conexion.cursor()
	def insertar(self,campos):
		nombreCampos = "usuario,password,nombre,apellidos,email,direccion"
		valoresCampos = "\'"+campos['usuario']+"\',\'"+campos['password']+"\',\'"+campos['nombre']+"\',\'"+campos['apellidos']+"\',\'"+campos['email']+"\',\'"+campos['direccion']+"\'"
		self.cursor.execute("INSERT INTO "+self.nombre+" ("+nombreCampos+") VALUES ("+valoresCampos+")")
		self.conexion.commit()
	def obtenertuplas(self):
		self.cursor.execute("SELECT * FROM "+self.nombre)
		tuplas=self.cursor.fetchall()
		return tuplas
	def cerrar(self):
		self.conexion.close()

class interfaz :

	def __init__(self,archivo):
		self.xml = Gtk.Builder()
		self.xml.add_from_file(archivo+".glade")

	def asignarsenyales(self,handler,quit=False):
		if(quit) :
			handler["cerrar"] = Gtk.main_quit
		self.xml.connect_signals(handler)

	def recoger(self,id):
		return self.xml.get_object(id)


def recogidaDatos(formulario):
	campos = {}
	campos['usuario'] = formulario.recoger("usuario").get_text()
	campos['password'] = formulario.recoger("password").get_text()
	campos['nombre'] = formulario.recoger("nombre").get_text()
	campos['apellidos'] = formulario.recoger("apellidos").get_text()
	campos['email'] = formulario.recoger("email").get_text()
	campos['direccion'] = formulario.recoger("direccion").get_text()
	return campos

def insertar(widget):
	xml = interfaz("interfaz")
	campos = recogidaDatos(xml)
	tEjercicio = Tabla("tEjercicio","tusuario")
	tEjercicio.insertar(campos)
	tEjercicio.cerrar()

def listar(widget):
	xml = interfaz("interfaz")
	tEjercicio = Tabla("tEjercicio","tusuario")
	datos = tEjercicio.obtenertuplas()
	tEjercicio.cerrar()
	xml = interfaz("listado")
	windowListado = xml.recoger("listado")
	TreeView = xml.recoger("tabla")
	listore = Gtk.ListStore(str,str,str,str,str,str)

	for tupla in datos:
		listore.append(tupla)

	renderer = Gtk.CellRendererText()
	column = Gtk.TreeViewColumn("Usuario", renderer, text=0)
	TreeView.append_column(column)
	renderer = Gtk.CellRendererText()
	column = Gtk.TreeViewColumn("Contraseña", renderer, text=1)
	TreeView.append_column(column)
	renderer = Gtk.CellRendererText()
	column = Gtk.TreeViewColumn("Nombre", renderer, text=2)
	TreeView.append_column(column)
	renderer = Gtk.CellRendererText()
	column = Gtk.TreeViewColumn("Apellidos", renderer, text=3)
	TreeView.append_column(column)
	renderer = Gtk.CellRendererText()
	column = Gtk.TreeViewColumn("Email", renderer, text=4)
	TreeView.append_column(column)
	renderer = Gtk.CellRendererText()
	column = Gtk.TreeViewColumn("Direccion", renderer, text=5)
	TreeView.append_column(column)
	TreeView.set_model(listore)
	windowListado.show()

#obtener interfaz
xml = interfaz("interfaz")

window = xml.recoger("applicationwindow1")

#asignar eventos
xml.recoger("insertar").connect("clicked",insertar)
xml.recoger("listar").connect("clicked",listar)
window.connect("destroy",Gtk.main_quit)

#Mostrar ventana principal
window.show_all()

# Lanzar GTK
Gtk.main()
