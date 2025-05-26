import string

def palindromo(palavra):
    palavra = palavra.lower().replace(" ", "").replace(string.punctuation, "")
    if palavra == palavra[::-1]:
        print("É um palindromo")
    else:
        print("Não é um palindromo")

palavra = input("Digite uma palavra: ")
palindromo(palavra)
