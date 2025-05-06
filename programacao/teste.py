dicionario_produtos = {"ipad": 7000, "iphone": 5000, "airpod": 2000}

# pegar o valor de um item 

print(dicionario_produtos["iphone"])

# adicionar um item
dicionario_produtos["macbook"] = 1200
print(dicionario_produtos["macbook"])

# editar um item
dicionario_produtos["iphone"] = 5500
print(dicionario_produtos["iphone"])

# remover um item
dicionario_produtos.pop("macbook")
print(dicionario_produtos)

# vericar se existe um item
print("iphone" in dicionario_produtos)
print("iphone" in dicionario_produtos.keys())
print(2000 in dicionario_produtos.values())

#transformando em listas
produtos = list(dicionario_produtos.keys())
print(produtos)

precos = list(dicionario_produtos.values())
print(precos)