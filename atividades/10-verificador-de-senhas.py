print("Bem vindo ao programa de verificar se sua senha é forte!")

while True:
    try:
        password = input("Digite uma senha: ")
        
        if password.lower() == 'sair':
            print(" ")
            print("❌  Programa finalizado!")
            print(" ")
            break
        elif len(password) < 8:
            print(" ")
            print("⚠️  A senha deve ter pelo menos 8 caracteres.")
            print(" ")
            continue
        else:
            tem_numero = False
            for caractere in password:
                if caractere.isdigit():
                    tem_numero = True
                    print(" ")
                    print("✅  A senha é forte!")
                    print(" ")
                    break
            if not tem_numero:
                print(" ")
                print("⚠️  A senha deve conter pelo menos um número.")
                print(" ")
                continue
        break
    except KeyboardInterrupt:
        print(" ")
        print(" ")
        print("❌  Programa encerrado!")
        print(" ")
        break
                    
    