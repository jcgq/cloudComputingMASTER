import re
class Error(Exception):
	pass

class RecetaSinNombre(Error):
	def nombre_incorrecto(nombre):
		if(nombre == "" or len(nombre)<3):
			return True
		else:
			return False

	def validar_nombre(nombre_recetas):
		try:
			if RecetaSinNombre.nombre_incorrecto(nombre_recetas):
				raise RecetaSinNombre
		except RecetaSinNombre:
			raise Error("ERROR: No se ha introducido un nombre valido")

class RecetaSinAlimentos(Error):
	def alimentos_incorrectos(alimentos, unidades_permitidas, diccionario_alimentos):
		alimentos = alimentos.split(";")
		correcto=True
		for i in range(0, len(alimentos)):
			if not any(alimento in alimentos[i] for alimento in diccionario_alimentos):
				correcto = False
			if not any(unidad in alimentos[i] for unidad in unidades_permitidas):
				correcto = False
		return correcto

	def validar_alimentos(alimentos, unidades_permitidas, diccionario_alimentos):
		try:
			if not RecetaSinAlimentos.alimentos_incorrectos(alimentos, unidades_permitidas, diccionario_alimentos):
				raise RecetaSinAlimentos
		except RecetaSinAlimentos:
			raise Error("ERROR: No se ha introducido un alimento valido")

class RecetaSinElaboracion(Error):
	def elaboracion_incorrecto(elaboracion):
		if(elaboracion == "" or len(elaboracion)<20):
			return True
		else:
			return False

	def validar_elaboracion(elaboracion_recetas):
		try:
			if RecetaSinElaboracion.elaboracion_incorrecto(elaboracion_recetas):
				raise RecetaSinElaboracion
		except RecetaSinElaboracion:
			raise Error("ERROR: No se ha introducido una elaboración valida")

class RecetaSinTiempo(Error):
	def tiempo_incorrecto(tiempo_empleado):
		if(type(tiempo_empleado) == type(1)):
			if tiempo_empleado < 2:
				return True
			else:
				return False
		if(type(tiempo_empleado) == type("1")):
			reg_exp = "[-+]?\d+$"
			aux = re.match(reg_exp, tiempo_empleado)
			if(aux):
				return False
			else:
				return True

	def validar_tiempo(tiempo_empleado):
		try:
			if RecetaSinTiempo.tiempo_incorrecto(tiempo_empleado):
				raise RecetaSinTiempo
		except RecetaSinTiempo:
			raise Error("ERROR: No se ha introducido los minutos correctos de elaboración")
