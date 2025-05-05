listas_precos = [1500, 1000, 8000,2000]


total_imposto = 0
for preco in listas_precos:

    if preco > 1000:
        taxa = 0.15
    else:
        taxa = 0.1
    imposto = taxa * preco
    total_imposto += imposto
    print(f"preço do produto {preco}, imposto é de  {imposto}")

print("Total de imposto", total_imposto)
vendas_23 = {"ja": 15000, "fev": 10000, "março": 5000}
vendas_24 = {"ja": 16000, "fev": 1100, "março": 5100}

#segundo exemplo: usando dicionário
# calculo percentual de crescimento
# 16000 / 15000 - 1 -> qnts % eu creci de um ano para o outro

for mes in vendas_24:
    valor_23 = vendas_23[mes]
    valor_24 = vendas_24[mes]
    crescimento = valor_24 /valor_23 -1
    print(f"no mes de {mes} o cresimento foi de {crescimento}")