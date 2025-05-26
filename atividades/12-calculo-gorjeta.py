gorjeta = lambda valor, porcentagem: valor * (porcentagem / 100) #funcao para calculo de gorjeta utilizando lambda

while True:
    try:
        valor_conta = float(input("Digite o valor da conta: "))
        porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta (ex.: 15): "))

        print(f"Para a conta de valor R${valor_conta:.2f} com gorjeta de {porcentagem_gorjeta:.1f}%, a gorjeta é de R${gorjeta(valor_conta, porcentagem_gorjeta):.2f}.")
        break
    except ValueError:
        print(" ")
        print("⚠️  Digite um número flutuante")
        print(" ")
    except KeyboardInterrupt:
        print(" ")
        print(" ")
        print("❌  Programa encerrado!")
        print(" ")
        break