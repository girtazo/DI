# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
from gi.repository import Gtk
from pprint import pprint

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

class Calculadora:

	def descontar(self,valor,porcentaje):

		valor = float(valor)
		porcentaje = float(porcentaje)
		self.resultado = valor - (valor * (porcentaje/100))
		self.descontado = valor - self.resultado
		return self.resultado
		

def calcular(xml):
	try:
		descuento = xml.recoger("descuento")
		modelo = descuento.get_model()
		iterador = descuento.get_active_iter()
		descuento = modelo[iterador][0]

		precio = xml.recoger("precio").get_text()
		if precio != "":

			calculadora = Calculadora()

			resultado = str(calculadora.descontar(precio, descuento))
			descuento = str(calculadora.descontado)

			xml.recoger("total").set_text(resultado+" €")
			xml.recoger("descontado").set_text(descuento+" €")
		else :
			xml.recoger("total").set_text("")
			xml.recoger("descontado").set_text("")

	except Exception, e:
		xml.recoger("error").show_all()

def acercade(xml):
	ventanaAcercaDe = xml.recoger("aboutdialog1")
	ventanaAcercaDe.show_all()

def cerraracercade(xml):
	ventanaAcercaDe = xml.recoger("aboutdialog1")
	print "cerrar"
	ventanaAcercaDe.hide()

def cerrarError(xml):
	xml.recoger("precio").set_text("")
	ventanaError = xml.recoger("error")
	print "cerrar"
	ventanaError.hide()

#obtener interfaz
xml = interfaz("interfaz")

principal = xml.recoger("window1")

# rellenar comboBox
valores = Gtk.ListStore(int)

valores.append([5])
valores.append([10])
valores.append([20])

descuento = xml.recoger("descuento")
descuento.set_model(valores)
renderer_text = Gtk.CellRendererText()
descuento.pack_start(renderer_text, True)
descuento.add_attribute(renderer_text, "text", 0)
descuento.set_active(0)

#crear eventos
xml.recoger("descuento").connect("changed",lambda(self) : calcular(xml))
xml.recoger("precio").connect("changed",lambda(self) : calcular(xml))
xml.recoger("imagemenuitem5").connect("activate",Gtk.main_quit)
xml.recoger("imagemenuitem10").connect("activate",lambda(self) : acercade(xml))
xml.recoger("aboutdialog-action_area1").get_children()[0].connect("clicked",lambda(self) : cerraracercade(xml))
xml.recoger("cerrarError").connect("clicked",lambda(self) : cerrarError(xml))
principal.connect("destroy",Gtk.main_quit)

#Mostrar ventana principal
principal.show_all()

# Lanzar GTK
Gtk.main()
