print("Calculo do IMC")
print("==============")

altura = float(input("Qual é sua altura? "))
peso = float(input("Qual é o seu peso? "))

imc = peso / (altura ** 2)

if imc < 16:
    print(f"Imc: {imc:.2f}")
    print("Classificação: Magreza grau III")
elif imc <= 16.9:
    print(f"Imc: {imc:.2f}")
    print("Classificação: Magreza grau II")
elif imc <= 18.4:
    print(f"Imc: {imc:.2f}")
    print("Classificação: Magreza grau I")
elif imc <= 24.9:
    print(f"Imc: {imc:.2f}")
    print("Classificação: Eutrofia")
elif imc <= 29.9:
    print(f"Imc: {imc:.2f}")
    print("Classificação: Pré-obesidade")
elif imc <= 34.9:
    print(f"Imc: {imc:.2f}")
    print("Classificação: Obesidade moderada (grau I)")
elif imc <= 39.9:
    print(f"Imc: {imc:.2f}")
    print("Classificação: Obesidade severa (grau II)")
else:
    print(f"Imc: {imc:.2f}")
    print("Classificação: Obesidade muito severa (grau III)")