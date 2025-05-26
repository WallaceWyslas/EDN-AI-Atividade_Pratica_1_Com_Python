import requests

random_user = requests.get("https://randomuser.me/api/?inc=name,email,location") #api para geração de usuário, limitado apenas a nome, email e localização

user_data = random_user.json() #gera um usuário aleatório

user = user_data['results'][0] #incorporta todos os dados do usuário
user_name = f"{user['name']['first']} {user['name']['last']}" #pega apenas o nome do usuário
user_email = f"{user['email']}" #pega apenas o email do usuário
user_country = f"{user['location']['country']}" #pega apenas o país do usuário

#print das informações
print(f"Nome: {user_name}")
print(f"E-mail: {user_email}")
print(f"País: {user_country}")