"""
Nombre del programa: CalcRobotica
Descripción:
    Convierte coordenadas cartesianas a cilindricas y/o esféricas, y viceversa.
    Hace operaciones con matrices de rotación-traslación y viceversa.
Autor: Magh
Creado: 2020.06.06
"""

import math as m

print("""
*****Calculadora para el curso de Robótica Industrial*****
Operaciones disponibles:
(Ángulos sexagesimales por defecto, indicar otro con g o rad seguido y al final de cada ángulo.)
    Conversión de coordenadas: (Respetar mayúsculas)
        Cart o cart -> Cartesianas a Cilíndricas y Esféricas
        Cil o cil -> Cilíndricas a Cartesianas y Esféricas
        Esfer o esfer -> Esféricas a Cartesianas y Cilíndricas
    Sistemas tridimensionales:
        T o t -> Solo Traslación
        R o r -> Solo rotación
        Rt o rt o rT o RT -> Rotación seguida de Traslación
        Tr o tr o tR o TR -> Traslación seguida de Rotación

Ejemplos de uso:
    Cart 10.45 15.4 13
    Esfer 22.7 62g 0.97rad
Para el caso de Sistemas tridimensionales, se pedirá ingresar el eje y ángulo de rotación, y luego el vector de traslación.
Algunos ejemplos:
    R x,0.5236rad
    r y,50g
    T 3.17 14 -2
    t 15 -11 -3
Para el caso de que sean varias rotaciones dejar un espacio en blanco por cada rotación.
Teniendo en cuenta que la primera que se escriba será la primera rotación y no la segunda o última.
Ejemplos:
    r y,100g x,60 z,0.785398rad
    R z,25 y,0.226rad x,70g
""")

#Lo más simple es ya tener la matriz resultante con toda la formula para cada elemento y simplemente reemplazar.
calcop=str(input("Escriba operación: "))

x = y = z = rc = re = tetaC = tetaE = fi = 0.0

if calcop.startswith("Cart",0,4) or calcop.startswith("cart",0,4):
    calcop=calcop.replace("Cart ","")
    calcop=calcop.replace("cart ","")

    cart=calcop.split(" ")

    x, y, z = float(cart[0]), float(cart[1]), float(cart[2])

    if len(cart)==3:
        #Calculo coordenadas cilindricas:
        rc=m.sqrt(m.pow(x,2)+m.pow(y,2))
        tetaC=m.atan(y/x)
        tetaC=(tetaC*180)/m.pi
        
        #Calculo coordenadas esféricas:
        re=m.sqrt(m.pow(x,2)+m.pow(y,2)+m.pow(z,2))
        tetaE=m.atan(y/x)
        tetaE=(tetaE*180)/m.pi
        fi=m.acos(z/re)
        fi=(fi*180)/m.pi

        print("""
Coordenadas Cilindricas:
r=%s
teta=%s
z=%s

Coordenadas Esféricas:
r=%s
teta=%s
fi=%s
        """%(rc,tetaC,z,re,tetaE,fi))
        
    else:
        print("Error, no ingreso tres coordenadas.")
elif calcop.startswith("Cil",0,3) or calcop.startswith("cil",0,3):
    calcop=calcop.replace("Cil ","")
    calcop=calcop.replace("cil ","")

    cil=calcop.split(" ")

    rc, tetaC, z = float(cil[0]), float(cil[1]), float(cil[2])

    if len(cil)==3:
        #Calculo coordenadas cartesianas:
        x=rc*m.cos(tetaC)
        y=rc*m.sin(tetaC)
        
        #Calculo coordenadas esféricas:
        re=m.sqrt(m.pow(x,2)+m.pow(y,2)+m.pow(z,2))
        tetaE=m.atan(y/x)
        tetaE=(tetaE*180)/m.pi
        fi=m.acos(z/re)
        fi=(fi*180)/m.pi

        print("""
Coordenadas Cartesianas:
x=%s
y=%s
z=%s

Coordenadas Esféricas:
r=%s
teta=%s
fi=%s
        """%(x,y,z,re,tetaE,fi))
    else:
        print("Error, no ingreso tres coordenadas.")
elif calcop.startswith("Esfer",0,5) or calcop.startswith("esfer",0,5):
    calcop=calcop.replace("Esfer ","")
    calcop=calcop.replace("esfer ","")

    esfer=calcop.split(" ")

    re, tetaE, fi = float(esfer[0]), float(esfer[1]), float(esfer[2])

    if len(esfer)==3:
        #Calculo coordenadas cartesianas:
        x=re*m.sin(fi)*m.cos(tetaE)
        y=rc*m.sin(fi)*m*m.sin(tetaE)
        z=rc*m.cos(fi)
        
        #Calculo coordenadas cilindricas:
        rc=m.sqrt(m.pow(x,2)+m.pow(y,2))
        tetaC=m.atan(y/x)
        tetaC=(tetaC*180)/m.pi

        print("""
Coordenadas Cartesianas:
x=%s
y=%s
z=%s

Coordenadas Cilindricas:
r=%s
teta=%s
z=%s
        """%(x,y,z,rc,tetaC,z))
    else:
        print("Error, no ingreso tres coordenadas.")
else:
    print("Error de entrada, no se reconoció el comando.")

px,py,pz=0,1,2
P=[[px],[py],[pz]]
r11=r12=r13=0
r21=r22=r23=1
r31=r32=r33=2
R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]

for fila in range(3):
    for columna in range(1):
        print("Elemento P",fila+1,columna+1," = ",P[fila][columna])

for fila in range(3):
    for columna in range(3):
        print("Elemento R",fila+1,columna+1," = ",R[fila][columna])