# Visualizacion del ZEN de python
# import this

# Estructuras de datos en conjuntos (Sets)
"""
Los conjuntos agrupan elementos que tienen datos en comun
como paises, nombres de personas, etc

- Propiedades:
    - Se pueden modificar
    - No tienen un orden
    - No permiten duplicados

"""

set_countries = {'Colombia', 'Mexico', 'Bolivia', 'Colombia'}
print(f"Conjunto = {set_countries} de tipo: {type(set_countries)}")
# Cuando un dato se repite en un conjunto este por defecto lo elimina.
# Consultando si existe informacion en un conjunto
print(f"Informacion existente: {'Colombia' in set_countries}")

# Agregar datos a un conjunnto
set_countries.add('Peru')
print(f"Paises: {set_countries}")




set_numbers = {1, 2, 2, 3, 4, 5, 6}
print(f"Conjunto = {set_numbers} de tipo: {type(set_numbers)}")

set_type = {1, "Hola", False, 12.11}
print(f"Conjunto = {set_type} de tipo: {type(set_type)}")

# Creamos un conjunto a partir de un string
set_from_string = set('hola mundo')
print(f"Conjunto = {set_from_string} de tipo: {type(set_from_string)}")

# Conjunto a partir de una tupla
set_from_tuples = set(('abc', 'asc', 'abc'))
print(f"Conjunto = {set_from_tuples} de tipo: {type(set_from_tuples)}")

"""
Si queremos dejar los valores unicos solo basta en convertirlo en un 
conjunto con la funcion set
"""
number = [1, 2, 3, 4, 1, 2, 3, 4]
set_number = set(number)
print(f"Conjunto = {set_number} de tipo: {type(set_number)}")
# Lista de resultados unicos
unique_number = list(set_number)
print(f"Conjunto = {unique_number} de tipo: {type(unique_number)}")



