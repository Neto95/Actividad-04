#encoding: UTF-8
#Autor: Ernesto Cruz Lpez A01169052 
#Determinar el area, diametro y volumen de una esfera usando el radio

#Funcion principal.
def main():
    radio = float(input("Radio de la esfera"))
    areaDeEsfera = calcularArea(radio)
    diametroDeEsfera = calcularDiametro(radio)
    volumenDeEsfera = calcularVolumen(radio)
    print("Esfera con radio:%.02f" % radio)
    print("Diametro:%.02f" % diametroDeEsfera)
    print("Volumen:%.02f" % volumenDeEsfera)   
    print("Area:%.02f" % areaDeEsfera)
    
#Funcion para calcular el area de la esfera
def calcularArea(radio):
    area = ((4*3.1416)*(radio)**2)
    return area

#Funcion para calcular el diametro de la esfera
def calcularDiametro(radio):
    diametro =(2*radio)
    return diametro

#Funcion para calcular el radio de la esfera
def calcularVolumen(radio):
    volumen = ((4/3*3.1416)*(radio)**3)
    return volumen

main()