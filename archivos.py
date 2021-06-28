import sys

def read(nombre_archivo, modo):
    lines = []
    with open(f'./{nombre_archivo}', modo, encoding='utf-8')as f:
        for line in f:
            lines.append(line.replace("\n",""))
        f.close()
    print(lines)


def write(nombre_archivo, modo, mensaje):
    with open(f'./{nombre_archivo}', modo, encoding='utf-8')as f:
         f.write(mensaje)
         f.write("\n")
         f.close()


def main(argv):
    try:
        if(len(argv)!=3):
            raise ValueError(f"Uso del script incorrecto: python3 {argv[0]} nombre_archivo modo[r or w or a]")
        if( not (argv[2] == 'r' or argv[2]=='w' or argv[2]=='a')):
            raise ValueError('Modo de apertura invalido: r para Read w para Write a para agregar contenido')     
    except ValueError as ve:
        print(ve)
        return False
    else: 
        if(argv[2]=='w' or argv[2]=='a'):
            mensaje = input('ingrese un mensaje: ')
            write(argv[1],argv[2],mensaje) 
        elif(argv[2]=='r'):
            try:
                read(argv[1],argv[2])
            except FileNotFoundError:
                print("no se encontró el archivo")

if __name__ == "__main__":
    main(sys.argv)