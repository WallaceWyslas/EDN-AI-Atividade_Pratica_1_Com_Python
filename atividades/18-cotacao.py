"""
Crie Um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI paro obter os dados de cotação.
https://docs.awesomeapi.com.br/api-de-moedas
"""
import requests

test = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL?token=d304bbe091b0dac958d7dc4eb4f7e351a2e0df24ef43aaf186c31f70680bf7f5")

def cotacao(moeda):
    moeda = moeda.upper()
    consulta = requests.get("https://economia.awesomeapi.com.br/json/last/" + moeda + "-BRL")
    dados = consulta.json()
    
    dados_high = dados[moeda + 'BRL']['high']
    dados_low = dados[moeda + 'BRL']['low']
    dados_data = dados[moeda + 'BRL']['create_date']
    print(f'Máximo: {dados_high}')
    print(f'Mínimo: {dados_low}')
    print(f'Data e Hora: {dados_data}')

def main():
    moeda = input("Digite uma moeda: ")
    cotacao(moeda)

if __name__ == "__main__":
    main()
