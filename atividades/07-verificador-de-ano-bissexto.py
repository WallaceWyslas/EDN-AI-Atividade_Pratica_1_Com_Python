ano = int(input("Digite o ano: "))
verifica_multiplo_100 = False

if ano % 400 == 0:
    print(f"O ano {ano} é Bissexto")
else:
    if ano % 4 == 0 and ano % 100 != 0:
        print(f"O ano {ano} é Bissexto")
    else:
        print(f"O ano {ano} NÃO é Bissexto")