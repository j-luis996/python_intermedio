##recibe una cadena y determina si es un palindromo
palindrome = lambda cad: cad == cad[::-1]

def main():
    print(palindrome("ana"))

if __name__ == "__main__":
    main()