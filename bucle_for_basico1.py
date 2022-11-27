#1 básico 
for i in range(0,151):
    print(i)

#2 Múltiplos de 5
for i in range(5,1000,5):
    print(i)

#3 Contar, a la manera del Dojo:
for contar in range(1,101):
    if contar % 10 == 0:
        print("Coding Dojo")
        continue
    elif contar % 5 == 0:
        print("Coding")
        continue
    print(contar)


#4 Whoa. Es un gran idiota:
#for i in range(1, 500000, 2):
    #print(i)

#5 Cuenta regresiva de a 4:
for i in range(2018, 0, -4):
    print(i)

#6 Contador flexible

def multiplicar(num_list,num):
    print(num_list, num) # la salida debería ser [2,4,10,16] 5
    for x in range(len(num_list)):
        print(x)
        num_list[x] *= num
        print(num_list)
    return num_list
a = [2,4,10,16]
b = multiplicar(a,5)
print(b)
# salida:
#[2,4,10,16] 5
#2
#[2,4,10,16]
#4
#[2,4,10,16]
#10
#[2,4,10,16]
#16
#[2,4,10,16]
#[2,4,10,16]

