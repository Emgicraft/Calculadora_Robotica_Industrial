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

#Declaración de variables:
x = y = z = rc = re = tetaC = tetaE = fi = 0.0
px,py,pz=0,1,2
P=[[px],[py],[pz]]
r11=r12=r13=0
r21=r22=r23=1
r31=r32=r33=2
R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]

#Entrada
calcop=str(input("Escriba operación: "))

#*********Operación de conversión de coordenadas*********
#Ingresan Cartesianas
if calcop.startswith("Cart",0,4) or calcop.startswith("cart",0,4):
    calcop=calcop.replace("Cart ","")
    calcop=calcop.replace("cart ","")
    cart=calcop.split(" ")

    if len(cart)==3:
        #Asignación de cada elemento a su respectiva variable:
        x, y, z = float(cart[0]), float(cart[1]), float(cart[2])

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
        print("Error, no ingresó tres coordenadas.")

#Ingresan Cilindricas
elif calcop.startswith("Cil",0,3) or calcop.startswith("cil",0,3):
    calcop=calcop.replace("Cil ","")
    calcop=calcop.replace("cil ","")
    cil=calcop.split(" ")

    if len(cil)==3:
        #Convierción entre sistemas ángulares
        if cil[1].endswith("g"):
            cil[1]=(float(cil[1])*m.pi)/200
        elif cil[1].endswith("rad"):
            pass
        else:
            cil[1]=(float(cil[1])*m.pi)/180

        #Asignación de cada elemento a su respectiva variable:
        rc, tetaC, z = float(cil[0]), float(cil[1]), float(cil[2])

        #Calcula coordenadas cartesianas:
        x=rc*m.cos(tetaC)
        y=rc*m.sin(tetaC)
        
        #CalculA coordenadas esféricas:
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
        print("Error, no ingresó tres coordenadas.")

#Ingresan Esféricas
elif calcop.startswith("Esfer",0,5) or calcop.startswith("esfer",0,5):
    calcop=calcop.replace("Esfer ","")
    calcop=calcop.replace("esfer ","")
    esfer=calcop.split(" ")

    if len(esfer)==3:
        #Convierción entre sistemas ángulares
        if esfer[1].endswith("g"):
            esfer[1]=(float(esfer[1])*m.pi)/200
        elif esfer[1].endswith("rad"):
            pass
        else:
            esfer[1]=(float(esfer[1])*m.pi)/180
        if esfer[2].endswith("g"):
            esfer[2]=(float(esfer[2])*m.pi)/200
        elif esfer[2].endswith("rad"):
            pass
        else:
            esfer[2]=(float(esfer[2])*m.pi)/180

        #Asignación de cada elemento a su respectiva variable:
        re, tetaE, fi = float(esfer[0]), float(esfer[1]), float(esfer[2])

        #Calculo coordenadas cartesianas:
        x=re*m.sin(fi)*m.cos(tetaE)
        y=re*m.sin(fi)*m.sin(tetaE)
        z=re*m.cos(fi)
        
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

#*********Operación con matrices*********
#Solo Traslación:
elif calcop.startswith("T",0,1) or calcop.startswith("t",0,1):
    calcop=calcop.replace("T ","")
    calcop=calcop.replace("t ","")
    Ptem=calcop.split(" ")

    for fila in range(3):
        P[fila][0]=float(Ptem[fila])
    
    for fila in range(3):
        print("Elemento P",fila+1,1," = ",P[fila][0])

#Solo Rotación:
elif calcop.startswith("R",0,1) or calcop.startswith("r",0,1):
    for fila in range(3):
        for columna in range(3):
            print("Elemento R",fila+1,columna+1," = ",R[fila][columna])

#Rotación seguida de Traslación
elif calcop.startswith("Rt",0,2) or calcop.startswith("rt",0,2) or calcop.startswith("rT",0,2) or calcop.startswith("RT",0,2):
    for fila in range(3):
        for columna in range(1):
            print("Elemento P",fila+1,columna+1," = ",P[fila][columna])

    for fila in range(3):
        for columna in range(3):
            print("Elemento R",fila+1,columna+1," = ",R[fila][columna])

#Traslación seguida de Rotación
elif calcop.startswith("Tr",0,2) or calcop.startswith("tr",0,2) or calcop.startswith("tR",0,2) or calcop.startswith("TR",0,2):
    for fila in range(3):
        for columna in range(1):
            print("Elemento P",fila+1,columna+1," = ",P[fila][columna])

    for fila in range(3):
        for columna in range(3):
            print("Elemento R",fila+1,columna+1," = ",R[fila][columna])
else:
    print("Error de entrada, no se reconoció el comando.")