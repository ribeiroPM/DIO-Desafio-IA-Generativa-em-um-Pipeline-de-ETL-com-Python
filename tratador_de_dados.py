import csv
import pandas as pd
import json as js


def tratamento_de_dados(dados_cliente):
	# Função responsável por captar e separar os dados dos clientes
	tipos_de_dados = ["id", "nome", "idade", "perfil", "renda"]
	dados = {tipos_de_dados[x]: dados_cliente[x] for x in range(5)}
	return dados

def analisador_de_perfil(dados_cliente):
	# Função que vai analizar renda e perfil e dispor de um conselho com base nas informações dadas
	conselho = ""
	perfil = dados_cliente["perfil"]
	renda = float(dados_cliente["renda"])

	if perfil == "conservador":
		if renda <= 1300:
			conselho = "Busque investir menos do que 20% da sua renda total"
		elif renda <= 5000:
			conselho = "Busque investimentos de longo prazo"
		elif renda <= 10000:
			conselho = "Busque investimentos imobiliarios"
	elif perfil == "moderado":
		if renda <= 1300:
			conselho = "Busque investir menos do que 20% da sua renda total"
		elif renda <= 5000:
			conselho = "Busque investimentos de longo prazo"
		elif renda <= 10000:
			conselho = "Busque investimentos imobiliarios"
	elif perfil == "arrojado":
		if renda <= 1300:
			conselho = "Busque investir menos do que 20% da sua renda total"
		elif renda <= 5000:
			conselho = "Busque investimentos de longo prazo"
		elif renda <= 10000:
			conselho = "Busque investimentos imobiliarios"

	dados_cliente["conselho"] = conselho
	return dados_cliente


def exporta_arquivo_json(dados_finalizados):
	# Exporta os dados tratados para um arquivo json
	arq_json = open("SDW2023.json", "w")
	arq_json.write(js.dumps(dados_finalizados, indent=4))
	arq_json.close()


def exporta_arquivo_csv(dados_finalizados):
	# Exporta os dados tratados para um novo arquivo csv
	dados_csv = "ID,NOME,IDADE,PERFIL,RENDA,CONSELHO\n"
	for dados in dados_finalizados:
		dados = ",".join([dado for dado in dados.values()])
		dados_csv += f"{dados}\n"
	arq = open("SDW2023.csv", "w")
	arq.write(dados_csv)
	arq.close()


# Metodo de leitura de arquivos csv usando a lib pandas, metodo mais utilizado
# tabela_investidores = pd.read_csv("SDW2023.csv", sep=",")
# print(tabela_investidores)


# Metodo de leitura de arquivos csv usando a lib csv, nativa do python
arquivo = open("SDW2023.csv")
csv_arq = csv.reader(arquivo, delimiter=",")

# Bloco responsável port correr o arquivo csv principal
dados_finalizados = []
for num, dados in enumerate(csv_arq):
	if num == 0:
		continue
	dados_tratados = tratamento_de_dados(dados)
	dados_analisados = analisador_de_perfil(dados_tratados)
	dados_finalizados.append(dados_analisados)

# Fecha o arquivo csv principal
arquivo.close()

# Chama as funções de exportar arquivos
exporta_arquivo_csv(dados_finalizados)
exporta_arquivo_json(dados_finalizados)



