print("Bem vindo à calculadora!")

while True:
    print("""
          Operações disponíveis:
                +: adição
                -: subtroçõo
                *: multiplicação
                /: divisão
          """)
    try:
        simb = input("Escolha uma operação: ")
        
        if simb == "+" or simb == "-" or simb == "*" or simb == "/":
            num1 = float(input("Insira o primeiro número: "))
            num2 = float(input("Insira o segundo número: "))
            
            if simb == "+":
                resultado = num1 + num2
            elif simb == "-":
                resultado = num1 - num2
            elif simb == "*":
                resultado = num1 * num2
            elif simb == "/":
                if num2 == 0:
                    print(" ")
                    print("⚠️  Erro: Divisão por zero não é permitida.")
                    continue
                else:
                    resultado = num1 / num2
        else:
            print(" ")
            print("⚠️  Error: Operação inválida.")
            continue

        print(" ")
        print(f"✅  {num1:.2f} {simb} {num2:.2f} = {resultado:.2f}")
        print(" ")
        print("❌  Programa encerrado!")
        print(" ")
        break
    
    except NameError:
        print(" ")
        print("⚠️  Digite um número válido!")
        print(" ")
    except ValueError:
        print(" ")
        print("⚠️  O valor digitado não é um número")
        print(" ")
    except KeyboardInterrupt:
        print(" ")
        print("❌  Programa encerrado!")
        print(" ")
        break