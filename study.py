import random

int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))


print(random.randint(1,6))

first_name = "Zen"
last_name = "Coder"
age = 25
print(f"Mi nombre is {first_name} {last_name} y tengo {age} años de edad.")

mi_lista = [1, 35, 25]
print(len(mi_lista))
print(sorted(mi_lista))
print(min(mi_lista))
print(enumerate(mi_lista))

findesemana = {"Dom": "Domingo", "Sáb": "Sábado"} # notación literal
capitales = {} # crea un diccionario vacío y luego agrega valores
capitales["svk"] = "Bratislava"
capitales["deu"] = "Berlin"
capitales["dnk"] = "Copenhagen"
print(findesemana["Dom"])
print(capitales["svk"])
value_removed = capitales.pop('svk') # eliminará la clave 'svk' y devolverá su valor
del capitales['dnk'] # eliminará la clave y no devolverá nada


