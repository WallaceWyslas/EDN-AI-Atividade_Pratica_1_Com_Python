while True:
    try:
        ano_nascimento = int(input("Digite o ano que você nasceu (ex.: 1998): "))
        
        if ano_nascimento >= 2025:
            print(" ")
            print("❌  Ano inválido!")
            print(" ")
            continue
        
        ano_nascimento_em_dias = (2025 - ano_nascimento) * 365
        
        print(f"Você tem {ano_nascimento_em_dias} dias de idade.")
        print(" ")
        break
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
    