"""
Crie Um programa que gera uma senha aleatória com o módulo
random, utilizando caracteres especiais, possibilitando o
Usuário a informar a quantidade de caracteres dessa senha
aleatório.
"""

import random
import string

caracter = string.ascii_letters + string.digits + string.punctuation #adiciona todos os caracteres em uma variavel

def senha_aleatoria(tamanho):
    senha = ''
    for i in range(tamanho):
        caracter_aleatorio = random.choice(caracter) #seleciona um simbolo aleatorio
        senha += caracter_aleatorio #sina caracter_aleatorio na senha, formando uma palavra
    return senha
    

while True:
    try:
        senha = int(input("Digite o tamanho de uma senha (ex.: 5): "))
        
        if senha > 0:    
            print(" ")
            print("✅  Senha aleatória:")
            print(senha_aleatoria(senha))
            print(" ")
            break
        else:
            print(" ")
            print("⚠️  Digite um número maior que 0")
            print(" ")
            continue
    except ValueError:
        print(" ")
        print("⚠️  Digite um número inteiro")
        print(" ")
    except KeyboardInterrupt:
        print(" ")
        print(" ")
        print("❌  Programa encerrado!")
        print(" ")
        break
