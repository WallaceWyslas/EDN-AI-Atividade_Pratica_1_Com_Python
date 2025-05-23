print("Bem vindo ao programa de calculo de médias de notas")

notas = []

while True:
    try:
        nota = input("Insira uma nota (0 - 10) ou digite 'fim' para finalizar: ")
        
        if nota.lower() == 'fim':
            for nota in notas:
                media = sum(notas) / len(notas)
            print(" ")
            print(f"✅  A média é: {media:.2f}")
            print(" ")
            print("❌  Programa finalizado!")
            break
        
        nota = float(nota)
        
        if nota < 0 or nota > 10:
            print("⚠️  Digite um número entre 0 e 10")
            continue
            
        notas.append(nota)
            
    except ValueError:
        print(" ")
        print("⚠️  O valor digitado não é um número")
    except KeyboardInterrupt:
        print(" ")
        print("❌  Programa encerrado!")
        break