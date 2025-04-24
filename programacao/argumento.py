import sys

argumentos = sys.argv #arg1 metod// arg 2 - n1 // arg3 - n2
# O indice 0 e o nome do programa  , o indice 1 o método , e o 2 e 3 saõ  as strings que o usuário está passando
def soma(n1,n2):
    return  n1 + n2

def sub(n1,n2):
    return n1 - n2

if argumentos[1] == "soma":
   resp = soma(argumentos[2],argumentos[3])

elif argumentos[1] == "sub":
    resp = sub(argumentos[2],argumentos[3])
print(resp)    