import sys

try:
       
    argumento = sys.argv

    n1 = float(argumento[2])
    n2 = float(argumento[3])

    def soma(n1,n2):
        return n1 + n2

    def subitracao(n1,n2):
        return n1 - n2

    def divisao(n1,n2):
        return n1/n2


    if n1 < 0 or n2 < 0:
        resposta = print("precisa ser números")
        exit()

    if argumento[1] == "soma":
        resposta = soma(n1,n2)

    elif argumento[1] == "subitracao":
        resposta = subitracao(n1,n2)

    elif argumento[1] == "divisao":
        resposta = divisao(n1,n2)

    print(resposta)
    
except:
    print("Deu ruim")    