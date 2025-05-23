print("Bem vindo ao programa de verificar se o número é Par ou Ímpar")

par_contagem = []
par = 0
impar_contagem = []
impar = 0

while True:
    try:
        num = input("Insira um número inteiro (ou digite 'fim'): ")
        
        if num.lower() == 'fim':
            print(" ")
            
            if len(par_contagem) > 0:
                print(f"Numeros pares: {par_contagem}")
            print(f"- Quantidade de números pares digitados: {par}")
            
            print(" ")
            
            if len(impar_contagem) > 0:
                print(f"- Numeros impares: {impar_contagem}")
            print(f"- Quantidade de números impares digitados: {impar}")
            
            print(" ")
            print("❌  Programa encerrado!")
            print(" ")
            break
        
        num = int(num)
        if num % 2 == 0:
            print(f"O número {num} é Par.")
            par_contagem.append(num)
            par += 1
            continue
        elif num % 2 != 0:
            print(f"O número {num} é Ímpar.")
            impar_contagem.append(num)
            impar += 1
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