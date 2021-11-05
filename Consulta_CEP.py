# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 19:34:45 2021

@author: Fin
"""

# -*- coding: utf-8 -*-
import requests
import csv
import time

def consultaCEP(cep):
 

    linkBase = "http://viacep.com.br/ws/{}/json"
    httpResponse = requests.get(linkBase.format(cep))
    if httpResponse.status_code == 200:
        result = httpResponse.json()
        print(httpResponse.status_code) 

        if "bairro" in result:
            print(result["bairro"])
            return result["bairro"]
        else:
            print("ERRO: " + cep)
            return "-"
    else:
        print("erro" + cep)
        return "-"


inputFile = open("result_resp2017-2019_flops.csv", "r")
outputFile = open("result_resp2017-2019_flops_bairros", "wb+")
dados = list(csv.reader(inputFile))

cabecalho = dados[0]
cabecalho.insert(4, "Bairro")
cabecalhocsv = ','.join(cabecalho) + "\n"
outputFile.write(cabecalhocsv.encode ("UTF-8"))

for i in range(1, len(dados)):
    line = dados[i]
    bairro = consultaCEP(line[4])
    line.insert(4, bairro)
    linecsv = ','.join(line) + "\n"
    outputFile.write(linecsv.encode ("UTF-8"))
    print(str(i) + "/" + str(len(dados) - 1))
    time.sleep (5)

inputFile.close()
outputFile.close()
