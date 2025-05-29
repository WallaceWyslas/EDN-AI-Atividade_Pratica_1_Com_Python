import requests

def cotacao():
    while True:
        moeda = input("Digite uma moeda: ")
        moeda = moeda.upper()
        consulta = requests.get("https://economia.awesomeapi.com.br/json/last/" + moeda + "-BRL")
        dados = consulta.json()
        moeda_completa = moeda + 'BRL'
        
        try:
            if moeda_completa in dados:
                dados_bid = dados[moeda_completa]['bid']
                dados_high = dados[moeda + 'BRL']['high']
                dados_low = dados[moeda + 'BRL']['low']
                dados_data = dados[moeda + 'BRL']['create_date']
                
                print('')
                print(f"Cotação da moeda {moeda}-BRL")
                print(f'Valor atual:    {float(dados_bid):.4f}')
                print(f'Valor Máximo:   {float(dados_high):.2f}')
                print(f'Valor Mínimo:   {float(dados_low):.2f}')
                print(f'Data e Hora:    {dados_data}')
                break
            else:
                if 'status' in dados and dados['status'] == 404:
                    print("Erro: Código Inválido!")
                    continue
            
        except KeyboardInterrupt:
            print("Programa encerrado!")        

def main():
    cotacao()

if __name__ == "__main__":
    main()
