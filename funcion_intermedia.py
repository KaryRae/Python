x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


#soluciones
#1
x [1][0] = 15
print(x)
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)
directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)
z[0]['y'] = 30
print(z)

#2
estudiantes2 = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(estudiantes2):
    for elem in estudiantes2:
        for clave, valor in elem.items():
            print(clave, "-" , valor, "," )
iterateDictionary(estudiantes2)


# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)

# Pregunta 3 
def iterateDictionary2(first_name, estudiantes2):
    for first_name in estudiantes2:
        for  valor in first_name.items():
            print( "-" , valor, "," )

iterateDictionary2()




# Pregunta 4

def printInfo(dicc):
    for llave, valores in dicc.items():
        num_valores = len(valores)

        print(f"{num_valores} {llave.upper()}")
        print(valores)
        for valor in valores:
            print(valor)


dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
