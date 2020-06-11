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
    Sistemas tridimensionales: (Al final ingresar vector relativo.)
        T o t -> Solo Traslación
        R o r -> Solo rotación
        Rt o rt o rT o RT -> Rotación seguida de Traslación
        Tr o tr o tR o TR -> Traslación seguida de Rotación
        V o v -> Vector relativo al sistema auxiliar (OUVW)

Ejemplos de uso:
    Cart 10.45 15.4 13
    Esfer 22.7 62g 0.97rad

Para el caso de Sistemas tridimensionales, se ingresará los valores del eje y ángulo de rotación,
el vector de traslación y el vector relativo a ese sistema, si es que hay.
De no haber vector relativo, solo ingresar ceros para cada elemento.
El orden depende del tipo de operación a realizar.

Algunos ejemplos:
    ****Solo Rotación: R-V****
    R x,0.5236rad
    v 0 0 0
    ****Solo Traslación: T-V****
    T 3.17 14 -2
    v -5 3.1 -1
    ****Traslación seguida de Rotación: T-R-V****
    tr 15 -11 -3    #Primero se ingresa el vector de traslación.
    r y,50g         #Luego la matriz de rotación.
    V -3 5.24 1     #Por último el vector relativo.
    ****Siempre el vector relativo al final.****

Para el caso de que sean varias rotaciones dejar un espacio en blanco por cada rotación.
Teniendo en cuenta que la primera que se escriba será la primera rotación y no la segunda o última.

Ejemplos:
    rt y,100g x,60 z,0.785398rad    #Obviamente después de esto se ingresaría el vector de traslación.
    R z,25 y,0.226rad x,70g
""")

#Declaración de variables:
x = y = z = rc = re = tetaC = tetaE = fi = 0.0
px,py,pz=0.0,1.0,2.0    #Por ahora no los uso independientemente.
P=[[px],[py],[pz]]
r11=r12=r13=0.0
r21=r22=r23=1.0
r31=r32=r33=2.0
R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
vx,vy,vz=0.0,0.0,0.0
V=[[vx],[vy],[vz]]
Vres=[[0.0],[0.0],[0.0]]

#Entrada
calcop=str(input("\nEscriba operación: "))

#*********Operación de conversión de coordenadas*********
#Ingresan Cartesianas
if calcop.startswith("Cart ",0,5) or calcop.startswith("cart ",0,5):
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
        print("\nError, no ingresó tres coordenadas.")

#Ingresan Cilindricas
elif calcop.startswith("Cil ",0,4) or calcop.startswith("cil ",0,4):
    calcop=calcop.replace("Cil ","")
    calcop=calcop.replace("cil ","")
    cil=calcop.split(" ")

    if len(cil)==3:
        #Converción entre sistemas ángulares
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
        print("\nError, no ingresó tres coordenadas.")

#Ingresan Esféricas
elif calcop.startswith("Esfer ",0,6) or calcop.startswith("esfer ",0,6):
    calcop=calcop.replace("Esfer ","")
    calcop=calcop.replace("esfer ","")
    esfer=calcop.split(" ")

    if len(esfer)==3:
        #Converción entre sistemas ángulares
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
        print("\nError, no ingresó vector relativo correctamente.")
    
    #Vector resultante
    print("\nVector resultante:")
    for fila in range(3):
        V[fila][0]=V[fila][0]+P[fila][0]
        print(V[fila][0])

#Solo Rotación: \\Por terminar, probablemente requiera de funciones que operen matrices.//
elif calcop.startswith("R ",0,2) or calcop.startswith("r ",0,2):
    #Vector Rotación:
    calcop=calcop.replace("R ","")
    calcop=calcop.replace("r ","")
    Rtem=calcop.split(" ")
    for ele in range(len(Rtem)):
        if Rtem[ele].startswith("X,",0,2) or Rtem[ele].startswith("x,",0,2):
            Rtem[ele]=Rtem[ele].replace("X,","")
            Rtem[ele]=Rtem[ele].replace("x,","")
            #Converción entre sistemas ángulares
            if Rtem[ele].endswith("g"):
                Rtem[ele]=(float(Rtem[ele])*m.pi)/200
            elif Rtem[ele].endswith("rad"):
                pass
            else:
                Rtem[ele]=(float(Rtem[ele])*m.pi)/180
            
            #Esto es solo temporal y solo aplica para una sola rotación:
            #Matriz de rotación del eje X
            r11,r12,r13=1.0,0.0,0.0
            r21=0.0
            r31=0.0
            r22,r23=m.cos(float(Rtem[0])),-m.sin(float(Rtem[0]))
            r32,r33=m.sin(float(Rtem[0])),m.cos(float(Rtem[0]))
            R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
        elif Rtem[ele].startswith("Y,",0,2) or Rtem[ele].startswith("y,",0,2):
            Rtem[ele]=Rtem[ele].replace("Y,","")
            Rtem[ele]=Rtem[ele].replace("y,","")
            #Converción entre sistemas ángulares
            if Rtem[ele].endswith("g"):
                Rtem[ele]=(float(Rtem[ele])*m.pi)/200
            elif Rtem[ele].endswith("rad"):
                pass
            else:
                Rtem[ele]=(float(Rtem[ele])*m.pi)/180
            
            #Esto es solo temporal y solo aplica para una sola rotación:
            #Matriz de rotación del eje X
            r12=0.0
            r21,r22,r23=0.0,1.0,0.0
            r32=0.0
            r11,r13=m.cos(float(Rtem[0])),m.sin(float(Rtem[0]))
            r31,r33=-m.sin(float(Rtem[0])),m.cos(float(Rtem[0]))
            R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
        elif Rtem[ele].startswith("Z,",0,2) or Rtem[ele].startswith("z,",0,2):
            Rtem[ele]=Rtem[ele].replace("Z,","")
            Rtem[ele]=Rtem[ele].replace("z,","")
            #Converción entre sistemas ángulares
            if Rtem[ele].endswith("g"):
                Rtem[ele]=(float(Rtem[ele])*m.pi)/200
            elif Rtem[ele].endswith("rad"):
                pass
            else:
                Rtem[ele]=(float(Rtem[ele])*m.pi)/180
            
            #Esto es solo temporal y solo aplica para una sola rotación:
            #Matriz de rotación del eje X
            r13=0.0
            r23=0.0
            r31=r32=r33=0.0,0.0,1.0
            r11,r12=m.cos(float(Rtem[0])),-m.sin(float(Rtem[0]))
            r21,r22=m.sin(float(Rtem[0])),m.cos(float(Rtem[0]))
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
    Rtem=calcop.split(" ")
    for ele in range(len(Rtem)):
        if Rtem[ele].startswith("X,",0,2) or Rtem[ele].startswith("x,",0,2):
            Rtem[ele]=Rtem[ele].replace("X,","")
            Rtem[ele]=Rtem[ele].replace("x,","")
            #Converción entre sistemas ángulares
            if Rtem[ele].endswith("g"):
                Rtem[ele]=(float(Rtem[ele])*m.pi)/200
            elif Rtem[ele].endswith("rad"):
                pass
            else:
                Rtem[ele]=(float(Rtem[ele])*m.pi)/180
            
            #Esto es solo temporal y solo aplica para una sola rotación:
            #Matriz de rotación del eje X
            r11,r12,r13=1.0,0.0,0.0
            r21=0.0
            r31=0.0
            r22,r23=m.cos(float(Rtem[0])),-m.sin(float(Rtem[0]))
            r32,r33=m.sin(float(Rtem[0])),m.cos(float(Rtem[0]))
            R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
        elif Rtem[ele].startswith("Y,",0,2) or Rtem[ele].startswith("y,",0,2):
            Rtem[ele]=Rtem[ele].replace("Y, ","")
            Rtem[ele]=Rtem[ele].replace("y, ","")
            #Converción entre sistemas ángulares
            if Rtem[ele].endswith("g"):
                Rtem[ele]=(float(Rtem[ele])*m.pi)/200
            elif Rtem[ele].endswith("rad"):
                pass
            else:
                Rtem[ele]=(float(Rtem[ele])*m.pi)/180
            
            #Esto es solo temporal y solo aplica para una sola rotación:
            #Matriz de rotación del eje X
            r12=0.0
            r21,r22,r23=0.0,1.0,0.0
            r32=0.0
            r11,r13=m.cos(float(Rtem[0])),m.sin(float(Rtem[0]))
            r31,r33=-m.sin(float(Rtem[0])),m.cos(float(Rtem[0]))
            R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
        elif Rtem[ele].startswith("Z,",0,2) or Rtem[ele].startswith("z,",0,2):
            Rtem[ele]=Rtem[ele].replace("Z, ","")
            Rtem[ele]=Rtem[ele].replace("z, ","")
            #Converción entre sistemas ángulares
            if Rtem[ele].endswith("g"):
                Rtem[ele]=(float(Rtem[ele])*m.pi)/200
            elif Rtem[ele].endswith("rad"):
                pass
            else:
                Rtem[ele]=(float(Rtem[ele])*m.pi)/180
            
            #Esto es solo temporal y solo aplica para una sola rotación:
            #Matriz de rotación del eje X
            r13=0.0
            r23=0.0
            r31=r32=r33=0.0,0.0,1.0
            r11,r12=m.cos(float(Rtem[0])),-m.sin(float(Rtem[0]))
            r21,r22=m.sin(float(Rtem[0])),m.cos(float(Rtem[0]))
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
        Rtem=calcop.split(" ")
        for ele in range(len(Rtem)):
            if Rtem[ele].startswith("X,",0,2) or Rtem[ele].startswith("x,",0,2):
                Rtem[ele]=Rtem[ele].replace("X,","")
                Rtem[ele]=Rtem[ele].replace("x,","")
                #Converción entre sistemas ángulares
                if Rtem[ele].endswith("g"):
                    Rtem[ele]=(float(Rtem[ele])*m.pi)/200
                elif Rtem[ele].endswith("rad"):
                    pass
                else:
                    Rtem[ele]=(float(Rtem[ele])*m.pi)/180
                
                #Esto es solo temporal y solo aplica para una sola rotación:
                #Matriz de rotación del eje X
                r11,r12,r13=1.0,0.0,0.0
                r21=0.0
                r31=0.0
                r22,r23=m.cos(float(Rtem[0])),-m.sin(float(Rtem[0]))
                r32,r33=m.sin(float(Rtem[0])),m.cos(float(Rtem[0]))
                R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
            elif Rtem[ele].startswith("Y,",0,2) or Rtem[ele].startswith("y,",0,2):
                Rtem[ele]=Rtem[ele].replace("Y, ","")
                Rtem[ele]=Rtem[ele].replace("y, ","")
                #Converción entre sistemas ángulares
                if Rtem[ele].endswith("g"):
                    Rtem[ele]=(float(Rtem[ele])*m.pi)/200
                elif Rtem[ele].endswith("rad"):
                    pass
                else:
                    Rtem[ele]=(float(Rtem[ele])*m.pi)/180
                
                #Esto es solo temporal y solo aplica para una sola rotación:
                #Matriz de rotación del eje X
                r12=0.0
                r21,r22,r23=0.0,1.0,0.0
                r32=0.0
                r11,r13=m.cos(float(Rtem[0])),m.sin(float(Rtem[0]))
                r31,r33=-m.sin(float(Rtem[0])),m.cos(float(Rtem[0]))
                R=[[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
            elif Rtem[ele].startswith("Z,",0,2) or Rtem[ele].startswith("z,",0,2):
                Rtem[ele]=Rtem[ele].replace("Z, ","")
                Rtem[ele]=Rtem[ele].replace("z, ","")
                #Converción entre sistemas ángulares
                if Rtem[ele].endswith("g"):
                    Rtem[ele]=(float(Rtem[ele])*m.pi)/200
                elif Rtem[ele].endswith("rad"):
                    pass
                else:
                    Rtem[ele]=(float(Rtem[ele])*m.pi)/180
                
                #Esto es solo temporal y solo aplica para una sola rotación:
                #Matriz de rotación del eje X
                r13=0.0
                r23=0.0
                r31=r32=r33=0.0,0.0,1.0
                r11,r12=m.cos(float(Rtem[0])),-m.sin(float(Rtem[0]))
                r21,r22=m.sin(float(Rtem[0])),m.cos(float(Rtem[0]))
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
    print("\Error de entrada, no se reconoció el comando.")