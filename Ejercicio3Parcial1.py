'''
Problema 3/6:

Realice un programa que genere una lista de listas, que emule a una matriz de orden NxM, con N y M
dados por el usuario. Suponga dicha matriz está llena de la forma zig-zag horizontal según la secuencia que
se muestra en el ejemplo:
                           1   2   3
                           6   5   4
                           7   8   9
                           12  11  10
'''

#Se solicita al usuario los valores N y M de la matriz:

n=input("Ingrese el número de filas N:")
m=(input("Ingrese el número de columnas M:"))
fila=[]
columna=[]
matriz=[]
K=0
invertidor=1
nivelador=1

#Se confirma que los valores suministrados sean números válidos:

if not n.isnumeric() or not m.isnumeric():
    raise TypeError("ingrese números enteros positivos porfa")

n=int(n)
m=int(m)
matriz=[]

#crear la matriz
for i in range(n):
    fila=[]
    for j in range(m):
        fila.append(0)
    matriz.append(fila)

#proximos dos ciclos for son para recorrer cada elemento de la matriz
for h in range(n):
    for d in range(m):

#este if es para aumentar la fila para luego restarle ya que no supe como voltearla
# es decir no supe usar el ".reversed"
        if K ==m*invertidor:
            K=(m+K)+1
            invertidor+=2

#este if es para compensar el k ya que le reste "m" tantos
        if K ==(m*nivelador)+1:
            K=K+m-1
            nivelador+=2

#cuando h es impar resto
        if h%2!=0:
            K-=1

#cuando h es par sumo
        if h%2==0:
            K+=1

        matriz[h][d]=K

print(matriz)
