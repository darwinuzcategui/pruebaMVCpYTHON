import sys # El módulo sys es el encargado de proveer variables y funcionalidades, directamente relacionadas con el intérprete
from PyQt5.QtWidgets import QApplication, QDialog # Nos Permite cargar la ventana .uic
from PyQt5 import uic # Nos permite cargar el .ui
sys.path.append("../controladores")
from validarControlador import *
from main_controlador import *


class Dialogo(QDialog):
	"""Contructoe de nuestro  Dialogo"""
	def __init__(self):
		QDialog.__init__(self)
		# llamae al controladores
		self.controlador = validarControlador(self)
		self.controlador1 = MainControlador(self)
		uic.loadUi("formulario1.ui",self)
		#self.email.setText("")
		#self.nombre.setText("")
		#self.lbl_ver.setText("!!! cantidad persona ")
		#self.nombre.textChanged.connect(self.controlador.cvalidar_nombre(nombre))
		#self.email.textChanged.connect(self.controlador.cvalidar_email(email))
		self.boton.clicked.connect(self.controlador.cvalidar_formulario)
		self.btn_add.clicked.connect(self.controlador1.csubir_per)
		self.btn_rest.clicked.connect(self.controlador1.cbajar_per)
	


app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()