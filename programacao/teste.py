import sys

argumentos = sys.argv

# function
def soma(n1,n2):
   resutado = n1+n2
   return resutado

# conversaõ para float
n1 = float(argumentos[2])
n2 = float(argumentos[3])


if argumentos[1] != "soma":
   print("diferente")

elif n1 <= 0:
    print("argumento 2  positivo")
    
elif n2 <= 0:
   print("argumento  3 precisa ser positivo") 

elif argumentos[1] == "soma":
   resultado = soma(n1,n2)
   print( resultado)


      