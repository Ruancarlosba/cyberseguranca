#Para associar valores a chaves únicas
#Quando usar:
#Quando você quer buscar valores por nome (ou outra chave).
#Quando os dados são relacionados por pares.
dicionario = {
     "tijolo": "objeto para montar muros",
     "constituiçaõ": "lei máxima do brasil"
     
}



print(type(dicionario))
print(dicionario["tijolo"])
print(dicionario["constituiçaõ"])

print("---------------------------------------")

pessoas = {
    "Guilherme": 19,
     "Maria":   17,
     "Joaõ": 23
}

for pessoa in pessoas.values():
    print(pessoa)

teste = {
    ("salvador","bahia","brasil")
}

print(teste)

for testes in teste:
    print(testes)