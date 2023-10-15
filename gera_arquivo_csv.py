import csv
import json as js

import random

arq = open("nomes.js")
arquivo = arq.read()
arq.close()
nomes =  js.loads(arquivo)["nomes"]


def sorteia_nomes():
	total_nomes_sorteados = 0
	nomes_sorteados = {}
	while len(nomes_sorteados) < 50:
		nome_sorteado = random.choice(nomes)
		total_nomes_sorteados += 1
		if nome_sorteado not in nomes_sorteados:
			nomes_sorteados[nome_sorteado] = 1
		else:
			if nomes_sorteados[nome_sorteado] <= 1:
				nomes_sorteados[nome_sorteado] += 1
			else:
				pass				
	return nomes_sorteados


def sorteia_idade():
	return random.randint(18, 49)


def sorteia_perfil():
	return random.choice(["conservador", "moderado", "arrojado"])

def sorteia_renda(idade):
	renda = 0
	if 17 < idade < 25:
		renda = random.randint(9, 13)*100
	elif 25 <= idade < 31:
		renda = random.randint(13, 22)*100
	elif 31 <= idade < 50:
		renda = random.randint(22, 99)*100
	return renda


nomes = sorteia_nomes()
arquivo_csv_esqueleto = "ID,NOME,IDADE,PERFIL,RENDA\n"
for num, nome in enumerate(nomes):
	idade = sorteia_idade()
	renda = sorteia_renda(idade)
	perfil = sorteia_perfil()
	arquivo_csv_esqueleto += f"{num+1},{nome},{idade},{perfil},{renda}\n"
arquivo_csv = open("SDW2023.csv", "w")
arquivo_csv.write(arquivo_csv_esqueleto)
arquivo_csv.close()
