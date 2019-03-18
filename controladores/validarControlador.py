import sys
sys.path.append("../Modelos")
from modeloValidar import *


class validarControlador:
	"""El Controlador  ValidarControlador"""
	#print("aqui")
	def __init__(self, un_dialogo):
		self.vnt_datos= un_dialogo
		
		self.mimodeloValidar = modeloValidar("aaa100","anombrea")
		
		#print(self.vnt_datos.email.text())
		#self.modeloValidar = modeloValidar(self.vnt_datos.email.text(), self.vnt_datos.nombre.text())
		#self.mimodeloValidar = modeloValidar("ddda@hotmail.com", "pedro prez")


	def cvalidar_formulario():
		print("fuera delif")
		
		if self.mimodeloValidar.validar_email("hhhha@hotmail.com"):
			print(" entro en contralado valido")
			return True 
		else:
			print(" entro en controlador No valido")
			return False 





  