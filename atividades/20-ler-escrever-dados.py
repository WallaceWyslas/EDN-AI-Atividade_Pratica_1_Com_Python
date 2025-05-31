import os
import csv
import json

def ler_arquivo(file_path):
    _, ext = os.path.splitext(file_path)
    
    try:
        if ext == ".json":
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data
        elif ext == ".csv":
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                data = [row for row in reader]
            return data
        elif ext == ".txt":
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.read().splitlines()
            data = [line.split(",") for line in lines if line.strip()]
            return data
        else:
            print("⚠️  Formato inválido!")
            return None
            
    except FileNotFoundError:
        print("❌  Arquivo não encontrado!")
        return None

def escrever_arquivo(file_path, data):
    _, ext = os.path.splitext(file_path)
    
    if ext == ".json":
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return True
    elif ext == ".csv":
        with open(file_path, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        return True
    elif ext == ".txt":
        with open(file_path, "w", encoding="utf-8") as file:
            for row in data:
                file.write(",".join(row) + "\n")
        return True
    else:
        print("⚠️  Formato inválido!")
        return False

def main():
    try:
        print("=== Gerenciador de Arquivos ===")
        file_path = input("Digite o caminho do arquivo (ex: dados.csv): ")
        action = input("Escolha a ação (ler/escrever): ").lower()
        
        if action == "ler":
            dados = ler_arquivo(file_path)
            if dados is not None:
                print("\n📊  Dados lidos:")
                for linha in dados:
                    print(linha)
        elif action == "escrever":
            if file_path.endswith(".json"):
                print("Digite os dados no formato JSON (ex: [{\"Nome\":\"João\", \"Idade\":30, \"Cidade\":\"SP\"}]):")
                raw_data = input()
                data = json.loads(raw_data)
            elif file_path.endswith(".csv"):
                print("Digite os dados no formato CSV (ex: João,30,São Paulo):")
                raw_data = input().strip().split(",")
                data = [raw_data]
            elif file_path.endswith(".txt"):
                print("Digite os dados no formato TXT (ex: João,30,São Paulo):")
                raw_data = input()
                data = [raw_data.split(",")]
            else:
                print("⚠️  Formato de arquivo não suportado!")
                return
            if escrever_arquivo(file_path, data):
                print("✅  Dados gravados com sucesso!")
        else:
            print("❌  Ação inválida!")
    except KeyboardInterrupt:
        print("\n\n❌  Operação cancelada pelo usuário!")

if __name__ == "__main__":
    main()