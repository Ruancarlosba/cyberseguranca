def divisao(a,b):
    try:
        print(a/b)
    except Exception as erro:
        print("divisaõ inválida")
        print(erro)
divisao(20,0)            