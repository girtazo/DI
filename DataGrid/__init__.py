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

def windowInsercion( self ):

	interfaz = None
	interfaz = Interfaz("interfaz")

	#Botones
	interfaz.recoger("insertar").connect("clicked",lambda guardar : insertar(interfaz))

def insertar(interfaz):
	usuario = recogidaDatos(interfaz)
	tblUsuarios = Tabla(baseDatos,"usuarios")
	tblUsuarios.insertar(usuario)
	tblUsuarios.cerrar()

def listar( self ):

	tblUsuarios = Tabla(baseDatos,"usuarios")
	usuarios = tblUsuarios.obtenertuplas()
	tblUsuarios.cerrar()

	TreeView = interfaz.recoger("tabla")
	eliminar = interfaz.recoger("eliminar")
	eliminar.set_sensitive(False)


	listore = Gtk.ListStore(str,str,str,str,str,str,str)

	for usuario in usuarios:
		usuario = (str(usuario[0]),usuario[1],usuario[2],usuario[3],usuario[4],usuario[5],usuario[6])
		listore.append(usuario)

	for campo in range(7):
		renderer = Gtk.CellRendererText()
		column = Gtk.TreeViewColumn(campos[campo], renderer, text=campo)
		TreeView.append_column(column)

	TreeView.set_model(listore)
	
	# Menu
	interfaz.recoger("Nuevo").connect("activated",windowInsercion)
	interfaz.recoger("Cerrar").connect("activated",lambda cerrarTabla : cerrar(windowTabla))

	# Barra de Herramientas
	interfaz.recoger("actualizar").connect("clicked",lambda actualizar : actualiza(interfaz))
	eliminar.connect("clicked",lambda eliminar : elimina(interfaz))

	# Seleccion TreeView
	TreeView.connect("cursor-changed",lambda sensitive : eliminacion(interfaz))
	
def actualiza( interfaz ):
	
	window = interfaz.recoger("Tabla")
	tabla = interfaz.recoger("tabla")

	tblUsuarios = Tabla(baseDatos,"usuarios")
	usuarios = tblUsuarios.obtenertuplas()
	tblUsuarios.cerrar()

	

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

def eliminacion( interfaz ):
	btnEliminar = interfaz.recoger("eliminar")
	if btnEliminar.get_sensitive() == True :
		if interfaz.recoger("tabla").get_selection().count_selected_rows() == 0 :
			btnEliminar.set_sensitive(False)
	else :
		btnEliminar.set_sensitive(True)

def crearAcercaDe(self):
	print "entra"
	interfaz = None
	interfaz = interfaz("interfaz")
	ventanaAcercaDe = interfaz.recoger("aboutdialog1")
	ventanaAcercaDe.show_all()
	interfaz.recoger("aboutdialog-action_area1").get_children()[0].connect("clicked",lambda cerrarAcercaDe : quitarAcercaDe(ventanaAcercaDe))

def cerrar(window):
	window.destroy()

#obtener interfaz
interfaz = Interfaz("interfaz")

#obtener ventana principal
windowTabla = interfaz.recoger("Tabla")

#asignar eventos
interfaz.recoger("imagemenuitem10").connect("activate",lambda acercaDe : crearAcercaDe)
windowTabla.connect("destroy",Gtk.main_quit)

#Mostrar ventana principal
windowTabla.show_all()

# Lanzar GTK
Gtk.main()
