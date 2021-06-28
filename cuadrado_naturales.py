def main():
    natula_list = []
    for i in range(1,101):
        #guarda numeros naturales al cuadrado
        #natula_list.append(i**2)

        #guarda el cuadrado de i en aux
        aux = i**2
        #si aux es dibisible entre 3 guarda aux en natural_list
        if aux%3 != 0:
            natula_list.append(aux)
    print(f"lista de cuadrado de numeros naturales: {natula_list}")

    #con list comprehensions

    natural_list2 = [i**2 for i in range(1,101) if i%3 != 0]
    print(f"lista con list comprehensions: {natural_list2}")

def reto():
    narutal_list = [i for i in range(1,1000) if i%4 == 0 and i%6 == 0 and i%9 == 0]
    print(narutal_list)
    

if __name__ == "__main__":
    #main()
    reto()