# Calculadora_Robotica_Industrial
Convierte coordenadas cartesianas a cilíndricas y esféricas, y viceversa. Realiza operaciones con matrices de rotación-traslación y viceversa.

Está calculadora está hecha sin librerias externas, por lo que tendrá ciertas limitantes en las operaciones.
Por ejemplo, una limitante es la cantidad de rotaciones simúltaneas que puede realizar y es que por ahora, solo puede operar una rotación, estó está explicado al final del documento.

Para saber más sobre como se usa, puede leer las siguientes instrucciones, las cuales también se les dará al iniciar el programa:

# **Calculadora para el curso de Robótica Industrial**
## Operaciones disponibles:
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

Para el caso de Sistemas tridimensionales, se ingresará los valores del eje y ángulo de rotación, el vector de traslación y el vector relativo a ese sistema, si es que hay.
De no haber vector relativo, solo ingresar ceros para cada elemento.

**Importante: El orden en que se ingresan los datos depende del tipo de operación a realizar.**

Algunos ejemplos:

    **Solo Rotación: R-V**
    R x,0.5236rad
    v 2 4 5
    **Solo Traslación: T-V**
    T 3.17 14 -2
    v -5 3.1 -1
    **Traslación seguida de Rotación: T-R-V**
    tr 15 -11 -3    #Primero se ingresa el vector de traslación.
    r y,50g         #Luego la matriz de rotación.
    V 0 0 0         #Por último el vector relativo, que para este ejemplo no hay.
    **Siempre el vector relativo al final.**

## Está parte aún no está implementada, pero está en desarrollo.
Para el caso de que sean varias rotaciones dejar un espacio en blanco por cada rotación.
Teniendo en cuenta que la primera que se escriba será la primera rotación y no la segunda o última.

Ejemplos:

	**Rotación seguida de Traslación: R-T-V**
    rt y,100g x,60 z,0.785398rad
    T 3.17 14 -2
    v -5 3.1 -1
    **Solo Rotación: R-V**
    R z,25 y,0.226rad x,70g
    v 2 4 5
