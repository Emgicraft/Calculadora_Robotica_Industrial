"""
Nombre del programa: CalcRobotica
Descripción:
    Convierte coordenadas cartesianas a cilindricas y/o esféricas, y viceversa.
    Hace operaciones con matrices de rotación-traslación y viceversa.
Autor: Magh
Creado: 2020.06.06
"""

import math as m

#***Angular Sistem Convert***
#Sexagesimales:
def ascSex(cadena): #Devuelve ángulo en tipo float
    if cadena.endswith("g"):
        cadena=cadena.replace("g","")
        return (float(cadena)*9)/10 #180/200
    elif cadena.endswith("rad"):
        cadena=cadena.replace("rad","")
        return (float(cadena)*180)/m.pi
    else:
        return float(cadena)
#Centesimales:
def ascCen(cadena): #Devuelve ángulo en tipo float
    if cadena.endswith("g"):
        cadena=cadena.replace("g","")
        return float(cadena)
    elif cadena.endswith("rad"):
        cadena=cadena.replace("rad","")
        return (float(cadena)*200)/m.pi
    else:
        return (float(cadena)*200)/180
#Radianes:
def ascRad(cadena): #Devuelve ángulo en tipo float
    if cadena.endswith("g"):
        cadena=cadena.replace("g","")
        return (float(cadena)*m.pi)/200
    elif cadena.endswith("rad"):
        cadena=cadena.replace("rad","")
        return float(cadena)
    else:
        return (float(cadena)*m.pi)/180

#Convierte coordenadas cartesianas a cilindricas:
def cartToCil(x,y,z):
    r=m.hypot(x,y) #Retorna raiz(x^2+y^2)
    theta=m.atan(y/x)
    theta=(theta*180)/m.pi
    print("""
Coordenadas Cilindricas:
r=%s
theta=%s
z=%s"""%(r,theta,z))
#Convierte coordenadas cartesianas a esféricas:
def cartToEsfer(x,y,z):
    r=m.hypot(x,y,z) #Retorna raiz(x^2+y^2+z^2)
    theta=(m.atan(y/x)*180)/m.pi
    phi=(m.acos(z/r)*180)/m.pi
    print("""
Coordenadas Esféricas:
r=%s
theta=%s
phi=%s"""%(r,theta,phi))

#Convierte coordenadas cilindricas a cartesianas:
def cilToCart(modVector,theta,z):
    theta=ascRad(theta)
    x=modVector*m.cos(theta)
    y=modVector*m.sin(theta)
    print("""
Coordenadas Cartesianas:
x=%s
y=%s
z=%s"""%(x,y,z))
#Convierte coordenadas cilindricas a esféricas:
def cilToEsfer(modVector,theta,z):
    r=m.hypot(modVector,z) #Retorna raiz(modVector^2+y^2)
    theta=ascSex(theta)
    phi=(m.acos(z/r)*180)/m.pi
    print("""
Coordenadas Esféricas:
r=%s
theta=%s
phi=%s"""%(r,theta,phi))

#Convierte coordenadas esféricas a cartesianas:
def esferToCart(modVector,theta,phi):
    theta=ascRad(theta)
    phi=ascRad(phi)
    x=modVector*m.sin(phi)*m.cos(theta)
    y=modVector*m.sin(phi)*m.sin(theta)
    z=modVector*m.cos(phi)
    print("""
Coordenadas Cartesianas:
x=%s
y=%s
z=%s"""%(x,y,z))
#Convierte coordenadas esféricas a cilindricas:
def esferToCil(modVector,theta,phi):
    theta=ascSex(theta)
    phi=ascRad(phi)
    r=modVector*m.sin(phi)
    z=modVector*m.cos(phi)
    print("""
Coordenadas Cilindricas:
r=%s
theta=%s
z=%s"""%(r,theta,z))

#Info de las funciones del programa:
print("""
*****Calculadora para el curso de Robótica Industrial*****
Operaciones disponibles:
(Ángulos sexagesimales por defecto, indicar otro con g o rad seguido y al final de cada ángulo.)
    Conversión de coordenadas: (Respetar mayúsculas)
        Cart o cart -> Cartesianas a Cilíndricas y Esféricas
        Cil o cil -> Cilíndricas a Cartesianas y Esféricas
        Esfer o esfer -> Esféricas a Cartesianas y Cilíndricas
    Sistemas tridimensionales: (Al final ingresar vector relativo.)
        T o t -> Solo Traslación
        R o r -> Solo Rotación
        Rt o rt o rT o RT -> Rotación seguida de Traslación
        Tr o tr o tR o TR -> Traslación seguida de Rotación
        V o v -> Vector relativo al sistema auxiliar (OUVW)

Ejemplos de uso:
    Cart 10.45 15.4 13
    esfer 22.7 62g 0.97rad

Para el caso de Sistemas tridimensionales, se ingresará los valores del eje y ángulo de rotación,
el vector de traslación y el vector relativo a ese sistema, si es que hay.
De no haber vector relativo, solo ingresar ceros para cada elemento.

**Importante: El orden en que se ingresan los datos depende del tipo de operación a realizar.**

Algunos ejemplos:
    ****Solo Rotación: R-V****
    R x,0.5236rad
    v 2 4 5
    ****Solo Traslación: T-V****
    T 3.17 14 -2
    v -5 3.1 -1
    ****Traslación seguida de Rotación: T-R-V****
    tr 15 -11 -3    #Primero se ingresa el vector de traslación.
    r y,50g         #Luego la matriz de rotación.
    V 0 0 0         #Por último el vector relativo, que para este ejemplo no hay.
    ****Siempre el vector relativo al final.****

Para el caso de que sean varias rotaciones dejar un espacio en blanco por cada rotación.
Teniendo en cuenta que la primera que se escriba será la primera rotación y no la segunda o última.

Ejemplos:
    ****Rotación seguida de Traslación: R-T-V****
    rt y,100g x,60 z,0.785398rad
    T 3.17 14 -2
    v -5 3.1 -1
    ****Solo Rotación: R-V****
    R z,25 y,0.226rad x,70g
    v 2 4 5""")

#Declaración de variables:
#px,py,pz=0.0,1.0,2.0    #Por ahora no los uso independientemente.
P=[[0.0],[0.0],[0.0]]
r11=r12=r13=0.0
r21=r22=r23=1.0
r31=r32=r33=2.0
R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
#vx,vy,vz=0.0,0.0,0.0
V=[[0.0],[0.0],[0.0]]
Vres=[[0.0],[0.0],[0.0]]

while True:
    #Entrada
    calcop=str(input("\nEscriba operación: "))

    #*********Operación de conversión de coordenadas*********
    #Ingresan Cartesianas
    if calcop.startswith("Cart ",0,5) or calcop.startswith("cart ",0,5):
        calcop=calcop.replace("Cart ","")
        calcop=calcop.replace("cart ","")
        cart=calcop.split(" ")

        if len(cart)==3:
            #Calcula e imprime coordenadas cilindricas:
            cartToCil(float(cart[0]), float(cart[1]), float(cart[2]))
            
            #Calcula e imprime coordenadas esféricas:
            cartToEsfer(float(cart[0]), float(cart[1]), float(cart[2]))
        else:
            print("\nError! No ingresó tres coordenadas.")

    #Ingresan Cilindricas
    elif calcop.startswith("Cil ",0,4) or calcop.startswith("cil ",0,4):
        calcop=calcop.replace("Cil ","")
        calcop=calcop.replace("cil ","")
        cil=calcop.split(" ")

        if len(cil)==3:
            #Calcula coordenadas cartesianas:
            cilToCart(float(cil[0]), cil[1], float(cil[2]))
            
            #Calcula coordenadas esféricas:
            cilToEsfer(float(cil[0]), cil[1], float(cil[2]))
        else:
            print("\nError! No ingresó tres coordenadas.")

    #Ingresan Esféricas
    elif calcop.startswith("Esfer ",0,6) or calcop.startswith("esfer ",0,6):
        calcop=calcop.replace("Esfer ","")
        calcop=calcop.replace("esfer ","")
        esfer=calcop.split(" ")

        if len(esfer)==3:
            #Calculo coordenadas cartesianas:
            esferToCart(float(esfer[0]), esfer[1], esfer[2])
            
            #Calculo coordenadas cilindricas:
            esferToCil(float(esfer[0]), esfer[1], esfer[2])
        else:
            print("\nError! No ingresó tres coordenadas.")

    #*********Operación con matrices*********
    #Solo Traslación:
    elif calcop.startswith("T ",0,2) or calcop.startswith("t ",0,2):
        #Vector Traslación:
        calcop=calcop.replace("T ","")
        calcop=calcop.replace("t ","")
        Ptem=calcop.split(" ")
        for fila in range(3):
            P[fila][0]=float(Ptem[fila])
        
        #Vector relativo:
        calcop=str(input("\nVector relativo: "))
        if calcop.startswith("V ",0,2) or calcop.startswith("v ",0,2):
            calcop=calcop.replace("V ","")
            calcop=calcop.replace("v ","")
            Vtem=calcop.split(" ")
            for fila in range(3):
                V[fila][0]=float(Vtem[fila])
        else:
            print("\nError! No ingresó vector relativo correctamente.")
        
        #Vector resultante
        print("\nVector resultante:")
        for fila in range(3):
            Vres[fila][0]=V[fila][0]+P[fila][0]
            print(Vres[fila][0])

    #Solo Rotación: \\Por terminar, probablemente requiera de funciones que operen matrices.//
    elif calcop.startswith("R ",0,2) or calcop.startswith("r ",0,2):
        #Vector Rotación:
        calcop=calcop.replace("R ","")
        calcop=calcop.replace("r ","")
        angR=calcop.split(" ")
        for ele in range(len(angR)):
            if angR[ele].startswith("X,",0,2) or angR[ele].startswith("x,",0,2):
                angR[ele]=angR[ele].replace("X,","")
                angR[ele]=angR[ele].replace("x,","")
                #Converción a radianes:
                angR[ele]=ascRad(angR[ele])
                
                #Esto es solo temporal y solo aplica para una sola rotación:
                #Matriz de rotación del eje X
                r11,r12,r13=1.0,0.0,0.0
                r21=0.0
                r31=0.0
                r22,r23=m.cos(float(angR[0])),-m.sin(float(angR[0]))
                r32,r33=m.sin(float(angR[0])),m.cos(float(angR[0]))
                R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
            elif angR[ele].startswith("Y,",0,2) or angR[ele].startswith("y,",0,2):
                angR[ele]=angR[ele].replace("Y,","")
                angR[ele]=angR[ele].replace("y,","")
                #Converción a radianes:
                angR[ele]=ascRad(angR[ele])
                
                #Esto es solo temporal y solo aplica para una sola rotación:
                #Matriz de rotación del eje X
                r12=0.0
                r21,r22,r23=0.0,1.0,0.0
                r32=0.0
                r11,r13=m.cos(float(angR[0])),m.sin(float(angR[0]))
                r31,r33=-m.sin(float(angR[0])),m.cos(float(angR[0]))
                R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
            elif angR[ele].startswith("Z,",0,2) or angR[ele].startswith("z,",0,2):
                angR[ele]=angR[ele].replace("Z,","")
                angR[ele]=angR[ele].replace("z,","")
                #Converción a radianes:
                angR[ele]=ascRad(angR[ele])
                
                #Esto es solo temporal y solo aplica para una sola rotación:
                #Matriz de rotación del eje X
                r13=0.0
                r23=0.0
                r31,r32,r33=0.0,0.0,1.0
                r11,r12=m.cos(float(angR[0])),-m.sin(float(angR[0]))
                r21,r22=m.sin(float(angR[0])),m.cos(float(angR[0]))
                R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
            else:
                print("\nError! Mal definido el eje de rotación.")
        
        #Muestro la matriz de rotación resultante, es solo para probar:
        print("\nMatriz de Rotación calculada:")
        for fila in range(3):
            print(R[fila][0]," ",R[fila][1]," ",R[fila][2])
        
        #Vector relativo:
        calcop=str(input("\nVector relativo: "))
        if calcop.startswith("V ",0,2) or calcop.startswith("v ",0,2):
            calcop=calcop.replace("V ","")
            calcop=calcop.replace("v ","")
            Vtem=calcop.split(" ")
            for fila in range(3):
                V[fila][0]=float(Vtem[fila])
        else:
            print("\nError, no ingresó vector relativo correctamente.")
        
        #Vector resultante
        print("\nVector resultante:")
        for fila in range(3):
            Vres[fila][0]=V[0][0]*R[fila][0]+V[1][0]*R[fila][1]+V[2][0]*R[fila][2]
            print(Vres[fila][0])

    #Rotación seguida de Traslación
    elif calcop.startswith("Rt ",0,3) or calcop.startswith("rt ",0,3) or calcop.startswith("rT ",0,3) or calcop.startswith("RT ",0,3):
        #Vector Rotación:
        calcop=calcop.replace("Rt ","")
        calcop=calcop.replace("rt ","")
        calcop=calcop.replace("rT ","")
        calcop=calcop.replace("RT ","")
        angR=calcop.split(" ")
        for ele in range(len(angR)):
            if angR[ele].startswith("X,",0,2) or angR[ele].startswith("x,",0,2):
                angR[ele]=angR[ele].replace("X,","")
                angR[ele]=angR[ele].replace("x,","")
                #Converción a radianes:
                angR[ele]=ascRad(angR[ele])
                
                #Esto es solo temporal y solo aplica para una sola rotación:
                #Matriz de rotación del eje X
                r11,r12,r13=1.0,0.0,0.0
                r21=0.0
                r31=0.0
                r22,r23=m.cos(float(angR[0])),-m.sin(float(angR[0]))
                r32,r33=m.sin(float(angR[0])),m.cos(float(angR[0]))
                R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
            elif angR[ele].startswith("Y,",0,2) or angR[ele].startswith("y,",0,2):
                angR[ele]=angR[ele].replace("Y,","")
                angR[ele]=angR[ele].replace("y,","")
                #Converción a radianes:
                angR[ele]=ascRad(angR[ele])
                
                #Esto es solo temporal y solo aplica para una sola rotación:
                #Matriz de rotación del eje X
                r12=0.0
                r21,r22,r23=0.0,1.0,0.0
                r32=0.0
                r11,r13=m.cos(float(angR[0])),m.sin(float(angR[0]))
                r31,r33=-m.sin(float(angR[0])),m.cos(float(angR[0]))
                R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
            elif angR[ele].startswith("Z,",0,2) or angR[ele].startswith("z,",0,2):
                angR[ele]=angR[ele].replace("Z,","")
                angR[ele]=angR[ele].replace("z,","")
                #Converción a radianes:
                angR[ele]=ascRad(angR[ele])
                
                #Esto es solo temporal y solo aplica para una sola rotación:
                #Matriz de rotación del eje X
                r13=0.0
                r23=0.0
                r31,r32,r33=0.0,0.0,1.0
                r11,r12=m.cos(float(angR[0])),-m.sin(float(angR[0]))
                r21,r22=m.sin(float(angR[0])),m.cos(float(angR[0]))
                R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
            else:
                print("\nError! Mal definido el eje de rotación.")
        
        #Muestro la matriz de rotación resultante, es solo para probar:
        print("\nMatriz de Rotación calculada:")
        for fila in range(3):
            print(R[fila][0]," ",R[fila][1]," ",R[fila][2])
        
        #Vector Traslación:
        calcop=str(input("\nVector Traslación: "))
        if calcop.startswith("T ",0,2) or calcop.startswith("t ",0,2):
            calcop=calcop.replace("T ","")
            calcop=calcop.replace("t ","")
            Ptem=calcop.split(" ")
            for fila in range(3):
                P[fila][0]=float(Ptem[fila])
        
        #Vector relativo:
        calcop=str(input("\nVector relativo: "))
        if calcop.startswith("V ",0,2) or calcop.startswith("v ",0,2):
            calcop=calcop.replace("V ","")
            calcop=calcop.replace("v ","")
            Vtem=calcop.split(" ")
            for fila in range(3):
                V[fila][0]=float(Vtem[fila])
        else:
            print("\nError, no ingresó vector relativo correctamente.")
        
        #Vector resultante
        print("\nVector resultante:")
        for fila in range(3):
            Vres[fila][0]=V[0][0]*R[fila][0]+V[1][0]*R[fila][1]+V[2][0]*R[fila][2]+P[fila][0]
            print(Vres[fila][0])

    #Traslación seguida de Rotación
    elif calcop.startswith("Tr ",0,3) or calcop.startswith("tr ",0,3) or calcop.startswith("tR ",0,3) or calcop.startswith("TR ",0,3):
        calcop=calcop.replace("Tr ","")
        calcop=calcop.replace("tr ","")
        calcop=calcop.replace("tR ","")
        calcop=calcop.replace("TR ","")
        Ptem=calcop.split(" ")
        for fila in range(3):
            P[fila][0]=float(Ptem[fila])
        #Vector Rotación:
        calcop=str(input("\nVector Rotación: "))
        if calcop.startswith("R ",0,2) or calcop.startswith("r ",0,2):
            calcop=calcop.replace("R ","")
            calcop=calcop.replace("r ","")
            angR=calcop.split(" ")
            for ele in range(len(angR)):
                if angR[ele].startswith("X,",0,2) or angR[ele].startswith("x,",0,2):
                    angR[ele]=angR[ele].replace("X,","")
                    angR[ele]=angR[ele].replace("x,","")
                    #Converción a radianes:
                    angR[ele]=ascRad(angR[ele])
                    
                    #Esto es solo temporal y solo aplica para una sola rotación:
                    #Matriz de rotación del eje X
                    r11,r12,r13=1.0,0.0,0.0
                    r21=0.0
                    r31=0.0
                    r22,r23=m.cos(float(angR[0])),-m.sin(float(angR[0]))
                    r32,r33=m.sin(float(angR[0])),m.cos(float(angR[0]))
                    R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
                elif angR[ele].startswith("Y,",0,2) or angR[ele].startswith("y,",0,2):
                    angR[ele]=angR[ele].replace("Y,","")
                    angR[ele]=angR[ele].replace("y,","")
                    #Converción a radianes:
                    angR[ele]=ascRad(angR[ele])
                    
                    #Esto es solo temporal y solo aplica para una sola rotación:
                    #Matriz de rotación del eje X
                    r12=0.0
                    r21,r22,r23=0.0,1.0,0.0
                    r32=0.0
                    r11,r13=m.cos(float(angR[0])),m.sin(float(angR[0]))
                    r31,r33=-m.sin(float(angR[0])),m.cos(float(angR[0]))
                    R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
                elif angR[ele].startswith("Z,",0,2) or angR[ele].startswith("z,",0,2):
                    angR[ele]=angR[ele].replace("Z,","")
                    angR[ele]=angR[ele].replace("z,","")
                    #Converción a radianes:
                    angR[ele]=ascRad(angR[ele])
                    
                    #Esto es solo temporal y solo aplica para una sola rotación:
                    #Matriz de rotación del eje X
                    r13=0.0
                    r23=0.0
                    r31,r32,r33=0.0,0.0,1.0
                    r11,r12=m.cos(float(angR[0])),-m.sin(float(angR[0]))
                    r21,r22=m.sin(float(angR[0])),m.cos(float(angR[0]))
                    R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
                else:
                    print("\nError! Mal definido el eje de rotación.")
        
        #Muestro la matriz de rotación resultante, es solo para probar:
        print("\nMatriz de Rotación calculada:")
        for fila in range(3):
            print(R[fila][0]," ",R[fila][1]," ",R[fila][2])
        
        #Vector relativo:
        calcop=str(input("\nVector relativo: "))
        if calcop.startswith("V ",0,2) or calcop.startswith("v ",0,2):
            calcop=calcop.replace("V ","")
            calcop=calcop.replace("v ","")
            Vtem=calcop.split(" ")
            for fila in range(3):
                V[fila][0]=float(Vtem[fila])
        else:
            print("\nError, no ingresó vector relativo correctamente.")
        
        #Vector resultante
        print("\nVector resultante:")
        for fila in range(3):
            Vres[fila][0]=(V[0][0]+P[0][0])*R[fila][0]+(V[1][0]+P[1][0])*R[fila][1]+(V[2][0]+P[2][0])*R[fila][2]
            print(Vres[fila][0])
    else:
        print("\nError de entrada, no se reconoció el comando.")