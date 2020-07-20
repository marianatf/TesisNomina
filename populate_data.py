import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nomina.settings')

import random
import django

django.setup()

from RecursosHumanos.models import *
from ConceptoPago.models import *
from faker import Faker

fakegen = Faker('es_MX')

ESTADOS = ['trabajando', 'desempleado']

generos = ['masculino', 'femenino', 'otro', 'ninguno']

escala_nivel = ['1', '2', '3', '4']

CANTIDAD = [1, 2, 3, 4]

departamento = ['Informatica', 'Finanzas', 'Proyectos', 'Gerencia']

UNIVERSITY = ['Michigan', 'UBA', 'USB', 'UCV', 'California']

TITULO = ['ING', 'LIC', 'DOC', 'MSc']

LUGARES = ['Informatica','Finanzas','Gerencia General']
def add_escalas(n):
	for entry in range(n):
		for grados in range(n):
			for pasos in range(n):
				sueldo = fakegen.ean(length=8)
				sueldof = float(sueldo) + (entry * 2)
				try:
					escala = Escala.objects.get_or_create(escala=(escala_nivel[entry]), grado=(grados), paso=(pasos),
														  sueldo=sueldof)[0]
					escala.save()
				except:
					pass


def add_persona():
	fake_cedula = fakegen.ean8()
	fake_apellido = fakegen.last_name()
	fake_nombre = fakegen.first_name()
	fake_segundo_nombre = fakegen.first_name()
	fakejob = fakegen.job()
	estados = random.choice(ESTADOS)
	fake_segundo_apellido = fakegen.last_name()
	fake_nacimiento = fakegen.date()
	a = Persona.objects.get_or_create(status=estados,
									  cedula=fake_cedula,
									  apellido=fake_apellido,
									  nombre=fake_nombre,
									  segundo_apellido=fake_segundo_apellido,
									  segundo_nombre=fake_segundo_nombre,
									  fecha_nacimiento=fake_nacimiento,
									  ocupacion_actual=fakejob,
									  cargo_optar=fakejob,
									  email=fakegen.email(),
									  telefono=fakegen.phone_number(),
									  genero=random.choice(generos),

									  )[0]
	a.save()
	print(a)
	return a


def add_familia(a):
	fake_cedula = fakegen.ean8()
	fake_apellido = fakegen.last_name()
	fake_nombre = fakegen.first_name()
	fake_segundo_nombre = fakegen.first_name()
	fake_segundo_apellido = fakegen.last_name()
	fake_nacimiento = fakegen.date()

	familias = Familia.objects.get_or_create(
		persona=a,
		cedula=fake_cedula,
		apellido=fake_apellido,
		segundo_apellido=fake_segundo_apellido,
		nombre=fake_nombre,
		segundo_nombre=fake_segundo_nombre,
		fecha_nacimiento=fake_nacimiento,
	)[0]
	print(familias)
	familias.save()


def add_educacion(e):
	universidad = random.choice(UNIVERSITY)
	titulo_o = random.choice(TITULO)
	termino = fakegen.pybool()
	inicios = fakegen.date()
	final = fakegen.date()
	educ = Educacion.objects.get_or_create(
		persona=e,
		titulo=(titulo_o + ' Of ' + universidad),
		fecha_inicio=inicios,
		finalizado=termino,
		fecha_fin=final,
	)[0]
	print(educ)
	educ.save()


def add_educacion(e):
	universidad = random.choice(UNIVERSITY)
	titulo_o = random.choice(TITULO)
	termino = fakegen.pybool()
	inicios = fakegen.date()
	final = fakegen.date()
	educ = Educacion.objects.get_or_create(
		persona=e,
		titulo=(titulo_o + ' Of ' + universidad),
		fecha_inicio=inicios,
		finalizado=termino,
		fecha_fin=final,
	)[0]
	print(educ)
	educ.save()


def add_departamento():
	departamento = Departamento.objects.get_or_create(
		descripcion=random.choice(LUGARES),
	)[0]
	departamento.save()
	print(departamento)
	return departamento

def add_cargo():
	cargo = Cargo.objects.get_or_create(cargo=fakegen.job(), descripcion=fakegen.paragraph())[0]
	cargo.save()
	print(cargo)
	return cargo

def rac(es,carg,dep):
	rac = Rac.objects.get_or_create(codigo_departamento=dep, codigo_cargo=carg, codigo_escala=es)[0]
	rac.save()
	print(rac)
	return rac
def empleado(rac):
	fake_cedula = fakegen.ean8()
	fake_apellido = fakegen.last_name()
	fake_nombre = fakegen.first_name()
	fake_segundo_nombre = fakegen.first_name()
	fakejob = fakegen.job()
	estados = random.choice(ESTADOS)
	fake_segundo_apellido = fakegen.last_name()
	fake_nacimiento = fakegen.date()
	a = Empleado.objects.get_or_create(status_trabajador=estados,
									  cedula=fake_cedula,
									  apellido=fake_apellido,
									  nombre=fake_nombre,
									  segundo_apellido=fake_segundo_apellido,
									  segundo_nombre=fake_segundo_nombre,
									  fecha_nacimiento=fake_nacimiento,
									  email=fakegen.email(),
									  telefono=fakegen.phone_number(),
									  genero=random.choice(generos),
									  codigo_rac=rac,
									sueldo=fakegen.random_digit_not_null()*100)[0]
	a.save()
	print(a)
	return a


for a in range(1, 20):
	cantidad_v = random.choice(CANTIDAD)
	personac = add_persona()
	for a in range(1, cantidad_v):
		add_familia(personac)
	add_educacion(personac)
	empleado(rac(add_escalas(1),add_cargo(),add_departamento()))




#add_escalas()
# if __name__ == '__main__':

# 	print("popula")
# 	populate(2)
# 	print("populating complete")



# obj = Empleado.objects.filter(cod_rac=4).update(cedula=2656564)
# def populate(N=1):

# 	for entry in range(N):

# 		estados = random.choice(estado)
# 		empresa = Empresa.objects.first()
# 		entrada = entry+1
# 		fake_cedula = fakegen.ean8()
# 		fake_apellido = fakegen.last_name()
# 		fake_nombre = fakegen.first_name()
# 		fakejob = fakegen.job()
		


# 		if entry>0:
# 			for grados in range(N):
# 				for pasos in range(N):
# 					sueldo = fakegen.ean(length=8)
# 					escala= Escala.objects.get_or_create(escala=(escalando),grado=(grados),paso=(pasos),sueldo=sueldo, cod_empresa=empresa)


# 		escalat= Escala.objects.get(pk=entrada)

# 		personas = Persona.objects.get_or_create(status=estados, cedula=fake_cedula, apellido=fake_apellido, nombre=fake_nombre, cod_empresa=empresa)
# 		cargos = Cargo.objects.get_or_create(cod_escala=escalat, des_cargo=fakejob, cod_empresa=empresa)
# 		print(cargos)
# 		print(personas)