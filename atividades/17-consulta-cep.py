import requests

def consulta_cep():
    while True:
        cep_input = input("Digite um CEP: ")
        
        cep_clean = cep_input.replace("-", "").replace(".", "").replace(" ", "") #limpa o cep escrito
        
        if len(cep_clean) == 8:
            try:
                cep_get = requests.get(f"https://viacep.com.br/ws/{cep_clean}/json/")
            
                dados = cep_get.json()

                cep_logradouro = dados['logradouro']
                cep_bairro = dados['bairro']
                cep_cidade = dados['localidade']
                cep_uf = dados['uf']
                
                print(f"Logradouro: {cep_logradouro}")
                print(f"Bairro: {cep_bairro}")
                print(f"Cidade: {cep_cidade}")
                print(f"Estato: {cep_uf}")
                break
            except KeyError:
                print("CEP Inválido!")
                continue
        else:
            print("CEP Inválido!")
            continue

def main():
    consulta_cep()

if __name__ == "__main__":
    main()
        