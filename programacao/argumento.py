import sys
#arg1 metod// arg 2 - n1 // arg3 - n2
# O indice 0 e o nome do programa  , o indice 1 o método , e o 2 e 3 saõ  as strings que o usuário está passando
argumento = sys.argv


def soma(n1,n2):
   return n1 + n2

def subi(n1,n2):
   return n1-n2

def multi(n1,n2):
   return n1 * n2

n1 = float(argumento[2])
n2 = float(argumento[3])

if argumento[1] == "soma":
   resposta = soma(n1,n2)

elif argumento[1] == "subi":
   resposta = subi(n1,n2)

elif argumento[1] == "multi":
   resposta = multi(n1,n2)  

print(resposta)   

