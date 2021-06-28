def palindromo(palabra):
    try: 
        if len(palabra) == 0:
            #si la cadena esta vacia genera un error tipo ValueError
            raise ValueError('No se pueden ingresar cadenas vacias')
        return palabra == palabra[::-1]
    except ValueError as ve:
        print(ve)
        return False

def main():
    palabra = input('ingresa una palabra: ')
    
    try:
        #aquí podemos cambiar lo que enviamos, si devuelve True es un palindromo
        if palindromo(palabra):
            print('es un palindromo')
        else:
            print('no es un palindromo')
    except TypeError:
        print('solo se pueden ingresar numeros')

if __name__ == "__main__":
    main()