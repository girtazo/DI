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

	def obtenerTuplas(self):

		self.cursor.execute("SELECT * FROM "+self.nombre)
		tuplas=self.cursor.fetchall()
		return tuplas

	def buquedaTuplas(self,campo,valor):
		
		self.cursor.execute("SELECT * FROM "+self.nombre+" WHERE "+campo+"="+valor)
		tuplas=self.cursor.fetchall()
		return tuplas

	def modificar(self,campo,valor):

		update = "UPDATE "+self.nombre+" SET "
		for c in range(0,campos)
		self.cursor.execute("UPDATE "+self.nombre+" SET usuario="WHERE "+campo+"="+valor)

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

class Window :
	def __init__( self, nombre, nombreInterfaz, principal = True ):
		self.Principal = principal
		self.Nombre = nombre

		self.Interfaz = Interfaz(nombreInterfaz)
		
		self.Window = self.Interfaz.recoger(nombre)

		if self.Principal:
			self.Window.connect("destroy",Gtk.main_quit)

class windowListado(Window) :

	def __init__( self, nombre, nombreInterfaz, principal = True ):
		
		Window.__init__( self, nombre, nombreInterfaz, principal )

		self.btnEliminar = self.Interfaz.recoger("eliminar")
		self.btnEliminar = self.Interfaz.recoger("editar")
		self.btnEditar.set_sensitive(False)
		self.btnEliminar.set_sensitive(False)

		self.crearListado()

		self.Window.show_all()

		# Menu
		self.Interfaz.recoger("Nuevo").connect("activate",lambda Nuevo : windowInsercion("Insertar","interfaz"))
		self.Interfaz.recoger("Salir").connect("activate",lambda cerrarTabla : self.cerrar())
		self.Interfaz.recoger("acercaDe").connect("activate",lambda abrirAcercaDe : windowAcercaDe("aboutdialog1","interfaz"))

		# Barra de Herramientas
		self.Interfaz.recoger("actualizar").connect("clicked",lambda Actualizar : self.actualizar())
		self.btnEliminar.connect("clicked",lambda Eliminar : self.elimina())
		self.btnEditar.connect("clicked",lambda Editar : windowModificacion())

		# Seleccion TreeView
		self.TreeView.connect("cursor-changed",lambda activaEliminacion : self.eliminacion())


	def crearListado(self):

		self.TreeView = self.Interfaz.recoger("tabla")

		self.Tabla = Tabla(baseDatos,"usuarios")
		usuarios = self.Tabla.obtenertuplas()

		listore = Gtk.ListStore(str,str,str,str,str,str,str)

		for usuario in usuarios:
			usuario = (str(usuario[0]),usuario[1],usuario[2],usuario[3],usuario[4],usuario[5],usuario[6])
			listore.append(usuario)

		for campo in range(7):
			renderer = Gtk.CellRendererText()
			column = Gtk.TreeViewColumn(campos[campo], renderer, text=campo)
			self.TreeView.append_column(column)

		self.TreeView.set_model(listore)

	def actualizar(self):

		usuarios = self.Tabla.obtenertuplas()

		listore = Gtk.ListStore(str,str,str,str,str,str,str)

		for usuario in usuarios:
			usuario = (str(usuario[0]),usuario[1],usuario[2],usuario[3],usuario[4],usuario[5],usuario[6])
			listore.append(usuario)

		self.TreeView.set_model(listore)
		self.Window.show_all()

	def elimina(self):

		select = self.TreeView.get_selection()
		usuario, campo = select.get_selected()
		id = usuario[campo][0]
		self.Tabla.borrar("id",id)
		self.actualizar()

	def eliminacion(self):

		if self.TreeView.get_selection().count_selected_rows() == 0 :
			self.btnEliminar.set_sensitive(False)
		else :
			self.btnEliminar.set_sensitive(True)

	def cerrar(self):

		self.Tabla.cerrar()
		self.Window.destroy()

class windowInsercion(Window) :

	def __init__( self, nombre, nombreInterfaz ):

		Window.__init__( self, nombre, nombreInterfaz, False )

		self.Tabla = Tabla(baseDatos, "usuarios") 

		self.Window.show_all()

		#Botones
		self.Interfaz.recoger("btnInsertar").connect("clicked",lambda guardar : self.insertar())

		self.Window.connect("destroy",lambda cerrarFormulario : self.cerrar())

	def getUsuario(self):

		usuario = {}
		usuario['usuario'] = self.Interfaz.recoger("usuario").get_text()
		usuario['password'] = self.Interfaz.recoger("password").get_text()
		usuario['nombre'] = self.Interfaz.recoger("nombre").get_text()
		usuario['apellidos'] = self.Interfaz.recoger("apellidos").get_text()
		usuario['email'] = self.Interfaz.recoger("email").get_text()
		usuario['direccion'] = self.Interfaz.recoger("direccion").get_text()
		return usuario

	def cleanForm(self):

		self.Interfaz.recoger("usuario").set_text("")
		self.Interfaz.recoger("password").set_text("")
		self.Interfaz.recoger("nombre").set_text("")
		self.Interfaz.recoger("apellidos").set_text("")
		self.Interfaz.recoger("email").set_text("")
		self.Interfaz.recoger("direccion").set_text("")

	def insertar(self):

		usuario = self.getUsuario()
		self.Tabla.insertar(usuario)
		self.cleanForm()

	def cerrar(self):

		self.Tabla.cerrar()

class windowModificacion(Window) :

	def __init__( self, nombre, nombreInterfaz ):

		Window.__init__( self, nombre, nombreInterfaz, False )

		self.Tabla = Tabla(baseDatos, "usuarios") 

		self.Window.show_all()

		#Botones
		self.Interfaz.recoger("btnModificar").connect("clicked",lambda cambiar : self.modificar())

		self.Window.connect("destroy",lambda cerrarFormulario : self.cerrar())

	def getUsuario(self):

		usuario = {}
		usuario['usuario'] = self.Interfaz.recoger("usuario").get_text()
		usuario['password'] = self.Interfaz.recoger("password").get_text()
		usuario['nombre'] = self.Interfaz.recoger("nombre").get_text()
		usuario['apellidos'] = self.Interfaz.recoger("apellidos").get_text()
		usuario['email'] = self.Interfaz.recoger("email").get_text()
		usuario['direccion'] = self.Interfaz.recoger("direccion").get_text()
		return usuario

	def cleanForm(self):

		self.Interfaz.recoger("usuario").set_text("")
		self.Interfaz.recoger("password").set_text("")
		self.Interfaz.recoger("nombre").set_text("")
		self.Interfaz.recoger("apellidos").set_text("")
		self.Interfaz.recoger("email").set_text("")
		self.Interfaz.recoger("direccion").set_text("")

	def modificar(self):

		usuario = self.getUsuario()
		self.Tabla.insertar(usuario)
		self.cleanForm()

	def cerrar(self):

		self.Tabla.cerrar()

class windowAcercaDe(Window) :

	def __init__( self, nombre, nombreInterfaz ):

		Window.__init__( self, nombre, nombreInterfaz, False )

		self.Window.show_all()

		# Botones
		self.Interfaz.recoger("aboutdialog-action_area1").get_children()[0].connect("clicked",lambda cerrarAcercaDe : self.Window.destroy())

# Lanzar Aplicacion Tabla
listado = windowListado("Tabla","interfaz")

# Lanzar GTK
Gtk.main()
