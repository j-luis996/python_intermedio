import sys

def main(argv):
    try:
        assert len(argv) == 2, f'el uso del programa es: python3 {argv[0]} tu_nombre'  
        assert not argv[1].isnumeric() , 'no debes ingresar numeros como parametro, solo tu nombre'
    except AssertionError as ae:
        print(ae)
    else:
        print(f'hola {argv[1]}')


if __name__ == "__main__":
    main(sys.argv)