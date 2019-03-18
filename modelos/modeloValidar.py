import sys
import re
from PyQt5.QtWidgets import QMessageBox

class modeloValidar:
	
	"""La Clase  modeloValidar"""
	def __init__(self, email, nombre ):
		self.email = email
		self.nombre = nombre
		
	def validar_nombre(self,nombre):
		#nombre= self.nombre.text()
		validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', nombre, re.I)
		if nombre=="":

			#self.nombre.setStyleSheet("border: 5px solid yellow;")
			return False
		elif not validar:
			#self.nombre.setStyleSheet("border: 5px solid red;")
			return False
		else:
			#self.nombre.setStyleSheet("border: 5px solid blue;")
			return True

	def validar_email(self,email):
		#email = self.email.text()
		validar = re.match('^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$', email, re.I)
		if email == "":
			#self.email.setStyleSheet("border: 5px solid yellow;")
			return False
		elif not validar:
			#self.email.setStyleSheet("border: 5px solid red;")
			return False
		else:
			#self.email.setStyleSheet("border: 5px solid blue;")
			return True
		
	def validar_formulario(self, nombre, email):
		if self.validar_nombre(nombre) and self.validar_email(email):
			return True
			#QMessageBox.information(self, "Formulario correcto", "Validación correcta", QMessageBox.Discard)
		else:
			return False
			#QMessageBox.warning(self, "Formulario incorrecto", "Validación incorrecta", QMessageBox.Discard)
		

#mivalidar=modeloValidar("Darwin","nn")
#print(mivalidar.validar_email("222@hhh.com"))
#print(mivalidar.validar_nombre("222@hhh.com"))
#print(mivalidar.validar_formulario("Darwin", "hhhha@hotmail.com"))
