Este projeto, feito como conclusão do desafio do módulo de python, tem copmo objetivo gerar dados aleatórios, e trata-los de forma que o script analize idade e renda de um possível vendedor, e defina para ele um conselho de qual caminho seguir para melhor investir seu dinheiro.

Primeiro, o script "gera_arquivo_csv.py" irá gerar uma tabela, contendo id, nome, idade, perfil e renda. 
Toda essa geração é feita aleatoriamente, utilizando a biblioteca random, do python. 
Os nome, também aleatórios estão armazenados externamente, em um arquivo json.

Segundo, esses dados, aramzenados no arquivo "SDW2023.csv", é absorvido pelo programa principal, nomeado de "tratador_de_dados.py".
Este script será responsável pelo tratamento dos dados, transformando de uma tabela csv para um dicionario.
Em seguida, este dicionario passa por varias funções, que irão analisar renda e idade, afim de definir o melhor conselho de investimento para o possivel investidor em questão.

Terceiro, ainda no script citado anteriormente, os dados serão agrupados novamente em um um arquivo csv de mesmo nome, e será exportado.
Junto deste arquivo csv, também será exportado um arquivo json, para fácil visualização posteriormente.
