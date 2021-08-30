def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    indice = peso / altura**2
    if peso > 0 and altura >0:
        if indice < 20:
            print("PESO BAJO")
        elif 20 <= indice <25:
            print("NORMAL")
        elif 25 <= indice < 30:
            print("SOBREPESO")
        elif 30 <= indice < 40:
            print("OBESIDAD")
        elif indice >= 40:
            print("OBESIDAD MORBIDA")
    else:
        print("Revisa tus datos, alguno de ellos es erróneo.")


    

if __name__=='__main__':
    main()