AGENDA = {
    "guilherme":{
        "tel":"99999-1010",
        "email": "guilherme@solid.com.br",
        "endereco": "av. 1",
    },
    "maria":{
        
        "tel":"91234-1019",
        "email": "maria@solid.com.br",
        "endereco": "av. 1",
    }, 

    "joaõ": {
      "tel" : "998260-1310",
      "email": "joao@solid.com.br",
      "edereco": "av. 3",  
    }
}

print(AGENDA['guilherme']['tel'])

print("----------mudando os dados-------------")

AGENDA["guilherme"]['endereco'] = "Rua das nações"
print(AGENDA["guilherme"]['endereco'])

print("--------------adicionando novas pessoas------")

AGENDA["gabriel"] = {
    "tel": "88864-2311",
    "email": "gabriel@solid.com.br",
    "endereco": "av. 4",
    
}

for agenda in AGENDA:
    print(agenda)
