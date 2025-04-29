# Para armazenar uma coleção de itens imutáveis e ordenados
# Quando usar:
# Quando você não quer que os dados mudem.
# Pode ser usada como chave em um dicionário (listas não podem).
import time
cores = ("amarelo","azul","roxo")

for cor in cores:
    print(cor)
    time.sleep(2)