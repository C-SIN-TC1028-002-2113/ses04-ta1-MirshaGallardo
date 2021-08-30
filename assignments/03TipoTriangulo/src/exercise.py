def main():
    #escribe tu código abajo de esta línea
    x = int(input("Ingresa la medida del lado 1: "))
    y = int(input("Ingresa la medida del lado 2: "))
    z = int(input("Ingresa la medida del lado 3: "))
    if x + y > z and y + z > x:
        if x==y==z:
            print("ES UN TRIANGULO EQUILATERO")
        elif x!=y and y!=z and x!=z :
            print("ES UN TRIANGULO ESCALENO")
        elif (y==z and x!=y and x!=z) or (x==y and z!=y and z!=x) or (x==z and y!=x and y!=z):
            print("ES UN TRIANGULO ISOSCELES")
    else:
        print("NO ES TRIANGULO")

    


if __name__=='__main__':
    main()
