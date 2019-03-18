import sys
sys.path.append("../Modelos")
from auto import *

class MainControlador():
	"""Controlador MainControlador"""
	def __init__(self,un_dialogo):
		self.auto = Auto()
		self.dialogo =un_dialogo

	def csubir_per(self):
		self.auto.subir_per()
		print (self.auto.cantidad_persona)
		self.actulizar_label()

	def cbajar_per(self):
		self.auto.bajar_per()
		print (self.auto.cantidad_persona)
		self.actulizar_label()

	def actulizar_label(self):
		self.dialogo.lbl_ver.setText(str(self.auto.cantidad_persona))
