# Escola da Nuvem - AWS re/start - AI
---
Lista de atividades referentes ao [Link](https://modulo-ia.s3.us-east-2.amazonaws.com/atividades-propostas.txt) com as 11 atividades

### 1. HELLO WORLD

Objetivo:
Exibir uma mensagem simples na tela.

Instrucoes:
- Escreva um programa que mostre uma mensagem padrao de saudacao ao usuario.
- A mensagem deve ser exibida diretamente no terminal apos a execucao do programa.

Explicacao:
- A linguagem Python possui uma funcao propria para mostrar textos no terminal.
- Essa funcao permite exibir mensagens, valores de variaveis e resultados de calculos.
- O objetivo aqui e se familiarizar com o primeiro comando fundamental da linguagem.

### 2. SOMA DE DOIS NUMEROS

Objetivo:
Calcular a soma de dois numeros definidos no proprio codigo e exibir o resultado.

Instrucoes:
- Escreva um programa que armazene dois numeros e realize a soma entre eles.
- O programa deve exibir o resultado da operacao de forma clara para o usuÃ¡rio.

Explicacao:
- Operacoes matematicas basicas sao realizadas com operadores aritmeticos.
- O simbolo de adicao permite somar dois valores numericos.
- Para que o resultado seja compreendido, ele deve ser apresentado de forma legivel na tela.

### 3. CALCULO DO VOLUME DE UMA CAIXA RETANGULAR

Objetivo:
Multiplicar tres valores correspondentes as dimensoes de uma caixa e calcular seu volume.

Instrucoes:
- Escreva um programa que armazene os valores de comprimento, largura e altura de uma caixa.
- Calcule o volume e exiba o resultado.

Explicacao:
- O volume de uma caixa retangular e calculado multiplicando-se as tres dimensoes.
- Essa e uma aplicacao pratica de multiplicacao entre variaveis.
- O resultado final deve ser exibido com clareza para o usuario.

### 4. TOTAL DA COMPRA

Objetivo:
Calcular o valor total a ser pago por um determinado numero de unidades de um produto.

Instrucoes:
- Escreva um programa que armazene o nome de um produto, seu preco unitario e a quantidade comprada.
- Calcule o valor total da compra e apresente uma descricao detalhada da transacao.

Explicacao:
- O valor total e obtido multiplicando o preco unitario pela quantidade comprada.
- Alem do calculo, a clareza na apresentacao das informacoes e essencial para a compreensao do usuario.
- O programa deve fornecer uma visao geral da compra, como se fosse um recibo simples.

### 5. CLASSIFICADOR DE IDADE

Enunciado:
Crie um programa que solicite a idade do usuario e classifique-o em uma das seguintes categorias:
- Crianca (0 a 12 anos)
- Adolescente (13 a 17 anos)
- Adulto (18 a 59 anos)
- Idoso (60 anos ou mais)

Instrucoes:
- Solicite que o usuario digite sua idade.
- O programa deve interpretar o valor digitado e classifica-lo de acordo com as faixas etÃ¡rias.
- O resultado da classificacao deve ser exibido de forma clara.

Explicacao:
- Esse exercicio utiliza estruturas condicionais para tomar decisoes baseadas em faixas numericas.
- Importante tratar casos invalidos, como idades negativas.
- A logica deve garantir que nenhuma faixa se sobreponha ou fique sem cobertura.

### 6. CALCULADORA DE IMC

Enunciado:
Desenvolva um programa que calcule o Indice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros), calcular o IMC e informar a classificacao de acordo com a tabela padrao.

Instrucoes:
- Solicite os dados do usuario: peso e altura.
- Calcule o IMC usando a formula: IMC = peso / (altura ** 2).
- Exiba o valor do IMC com uma casa decimal e a respectiva classificacao (ex: abaixo do peso, normal, sobrepeso etc.).

Explicacao:
- O exercicio envolve entrada de dados numericos com ponto flutuante, calculos matematicos e estruturas condicionais.
- A classificacao deve seguir os intervalos padrao definidos para o IMC.
- Apresente o resultado de forma clara e arredondado corretamente.

### 7. VERIFICADOR DE ANO BISSEXTO

Enunciado:
Faca um programa que determine se um ano inserido pelo usuario e bissexto ou nao.
Lembre-se:
- Um ano e bissexto se for divisivel por 4;
- Mas anos divisiveis por 100 so sao bissextos se tambem forem divisiveis por 400.

Instrucoes:
- Solicite que o usuario digite um ano.
- Verifique se ele e bissexto ou nao, de acordo com as regras descritas.
- Exiba uma mensagem informando se o ano e bissexto.

Explicacao:
- Este exercicio explora o uso de operadores logicos e condicionais compostos.
- Trata-se de uma aplicacao classica que ajuda a desenvolver o raciocinio para multiplas condicoes encadeadas.
- Teste com diferentes anos para validar a logica.

### 8. CALCULADORA
Desenvolva uma calculadora em Python que realize as quatro operacoes basicas entre dois numeros. 
A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operacao. Siga as especificacoes abaixo:â€‹

- A calculadora deve solicitar ao usuario que insira dois numeros e uma operacao.â€‹
- As operacoes validas sao: + (adicao), - (subtracao), * (multiplicacao) e / (divisao).â€‹
- O programa deve continuar solicitando entradas ate que uma operacao valida seja concluida.â€‹

Trate os seguintes erros:â€‹

- Entrada invalida (nÃ£o numerica) para os numerosâ€‹
- Divisao por zeroâ€‹
- Operacao invalidaâ€‹

- Use try/except para capturar e tratar os erros apropriadamente.â€‹
- Apos cada erro, o programa deve informar o usuario sobre o erro e solicitar nova entrada.â€‹
- Quando uma operacao e concluida com sucesso, exiba o resultado e encerre o programa.â€‹

### 9. REGISTRO DE NOTAS

- Crie um programa que permita a um professor registrar as notas de uma turma. 
- O programa deve continuar solicitando notas ate que o professor digite 'fim'. 
- Notas vÃ¡lidas sÃ£o de 0 a 10. 
- O programa deve ignorar notas invalidas e continuar solicitando. 
- No final, deve exibir a mÃ©dia da turma. Notas = [] -> len(Notas)â€‹

### 10. VERIFICADOR DE SENHAS

- Crie um programa que verifique se uma senha e forte. 
- Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um numero. 
- O programa deve continuar pedindo senhas ate que uma senha valida seja inserida ou o usuario digite 'sair'.

### 11. PAR OU IMPAR

Crie um programa que solicite ao usuario que insira numeros inteiros. 
O programa deve continuar solicitando numeros ate que o usuario digite 'fim'. 
Para cada numero inserido, o programa deve informar se e par ou impar. 
Se o usuario inserir algo que nao seja um numero inteiro, o programa deve informar o erro e continuar. 
No final, o programa deve exibir a quantidade de numeros pares e impares inseridos.

### 12. GORJETA
Crie uma funcao que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.
Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

Parametros:
- valor_conta (float): O valor total da conta
- porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

Retorna:
O valor da gorjeta calculada.

### 13. PALINDROMO
Crie uma funcao que verifique se uma palavra ou frase e um palindromo 
(le-se igual de tras para frente, ignorando espacos e pontuacao). 
Se o resultado E True, responda "Sim", se o resultado for False, responda "Não"

### 14. IDADE EM ANOS
Crie uma funcao que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

### 15. GERADOR DE SENHA ALEATÓRIA
Crie Um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o Usuário a informar a quantidade de caracteres dessa senha aleatório.

### 16. GERADOR DE PERFIL ALEATÓRIO
Crie um programa que gera um perfil de Usuário aleatório usando o API 'Random user Generator'. O programa deve exibir o nome, email e país do Usuário gerado.
randomuser.me

### 17. CONSULTOR DE CEP
Desenvolvo um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
viacep.com.br

### 18. CONSULTOR DE COTAÇÃO
Crie Um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI paro obter os dados de cotação.
https://docs.awesomeapi.com.br/api-de-moedas

### 19. LER ARQUIVO LOG
Leia um arquivo que contém dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de execução constantes.

### 20. LER E ESCREVER DADOS
Crie um script em Python que escreva e leia dados em um arquivo CSV, TXT e JSON. Os arquivos devem conter informações de pessoas, com colunas Nome, Idade e Cidade.