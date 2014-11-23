# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
from gi.repository import Gtk
import sqlite3
from pprint import pprint


baseDatos = 'BaseDatos'
campos = ("id","usuario","password","nombre","apellidos","email","direccion")


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
	def borrar(self,campo,valor):
		self.cursor.execute("DELETE FROM "+self.nombre+" WHERE "+campo+"="+valor)
		self.conexion.commit()
	def cerrar(self):
		self.conexion.close()

class Interfaz :

	def __init__(self,archivo):
		self.xml = Gtk.Builder()
		self.xml.add_from_file(archivo+".glade")

	def asignarsenyales(self,handler,quit=False):
		if(quit) :
			handler["cerrar"] = Gtk.main_quit
		self.xml.connect_signals(handler)

	def recoger(self,id):
		return self.xml.get_object(id)


def recogidaDatos( formulario ):
	campos = {}
	campos['usuario'] = formulario.recoger("usuario").get_text()
	campos['password'] = formulario.recoger("password").get_text()
	campos['nombre'] = formulario.recoger("nombre").get_text()
	campos['apellidos'] = formulario.recoger("apellidos").get_text()
	campos['email'] = formulario.recoger("email").get_text()
	campos['direccion'] = formulario.recoger("direccion").get_text()
	return campos

def insertar( interfaz ):
	usuario = recogidaDatos(interfaz)
	tblUsuarios = Tabla(baseDatos,"usuarios")
	tblUsuarios.insertar(usuario)
	tblUsuarios.cerrar()

def crearlistado( self ):
	interfaz = None
	interfaz = Interfaz("interfaz")

	tblUsuarios = Tabla(baseDatos,"usuarios")
	usuarios = tblUsuarios.obtenertuplas()
	tblUsuarios.cerrar()
	window = interfaz.recoger("listado")
	TreeView = interfaz.recoger("tabla")

	listore = Gtk.ListStore(str,str,str,str,str,str,str)

	for usuario in usuarios:
		usuario = (str(usuario[0]),usuario[1],usuario[2],usuario[3],usuario[4],usuario[5],usuario[6])
		listore.append(usuario)

	for campo in range(7):
		renderer = Gtk.CellRendererText()
		column = Gtk.TreeViewColumn(campos[campo], renderer, text=campo)
		TreeView.append_column(column)

	TreeView.set_model(listore)
	window.show_all()

	interfaz.recoger("actualizar").connect("clicked",lambda actualizar : actualiza(interfaz))
	interfaz.recoger("eliminar").connect("clicked",lambda eliminar : elimina(interfaz))
	TreeView.connect("row-activated",lambda sensitive : eliminacion(interfaz))
	
def actualiza( interfaz ):
	tabla = interfaz.recoger("tabla")
	tblUsuarios = Tabla(baseDatos,"usuarios")
	usuarios = tblUsuarios.obtenertuplas()
	tblUsuarios.cerrar()
	window = interfaz.recoger("listado")

	listore = Gtk.ListStore(str,str,str,str,str,str,str)

	for usuario in usuarios:
		usuario = (str(usuario[0]),usuario[1],usuario[2],usuario[3],usuario[4],usuario[5],usuario[6])
		listore.append(usuario)

	tabla.set_model(listore)
	window.show_all()

def elimina( interfaz ):
	tabla = interfaz.recoger("tabla")
	select = tabla.get_selection()
	usuario, campo= select.get_selected()
	tblUsuarios = Tabla(baseDatos,"usuarios")
	id = usuario[campo][0]
	tblUsuarios.borrar("id",id)
	actualiza(interfaz)

def eliminacion(interfaz):
	print "entra"
	eliminar = interfaz.recoger("eliminar")
	if eliminar.sensitive :
		eliminar = False
	else:
		eliminar = True

#obtener interfaz
interfaz = Interfaz("interfaz")

#obtener ventana principal
windowInsercion = interfaz.recoger("insercion")

#asignar eventos
interfaz.recoger("insertar").connect("clicked",lambda grabar : insertar(interfaz))
interfaz.recoger("listar").connect("clicked",crearlistado)
windowInsercion.connect("destroy",Gtk.main_quit)

#Mostrar ventana principal
windowInsercion.show_all()

# Lanzar GTK
Gtk.main()
