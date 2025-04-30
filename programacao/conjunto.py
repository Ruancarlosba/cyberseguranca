# é o tipo de dado set. Ele representa uma coleção não ordenada, mutável e que não permite elementos duplicados.

conjunto_cores = {"vermelho","azul","verde"}

conjunto_cores.add("branco")
conjunto_cores.add("vermelho")

conjunto_cores.remove("branco")

for cor in conjunto_cores:
    print(cor)