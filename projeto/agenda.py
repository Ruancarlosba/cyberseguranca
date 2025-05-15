AGENDA = {}

AGENDA["guilherme"] ={
    "telefone": "99999928272",
    "email": "guilherme@solyd.com",
    "endereco": "av. 1"
}

AGENDA["maria"] ={
    "telefone": "888923412",
    "email": "maria@solyd.com",
    "endereco": "av. 2"
}

def mostrar_contatos():
  for contato in AGENDA:
   buscar_contato(contato)
   

def buscar_contato(contato):
   print("Nome:",contato)
   print("telefone:",AGENDA[contato]["telefone"])
   print("Email:",AGENDA[contato]["email"])
   print("Edereço:",AGENDA[contato]["endereco"])
   print("--------------------")
def incluir_editar_contato(contato, telefone, email, endereco):
  AGENDA[contato] = {
    'telefone': telefone,
    'email': email,
    'endereco': endereco,
  }
  print()
  print(">>>>> Contato:{} excluido com sucesso".format(contato))
  print()   


def excluir_contato(contato):
  AGENDA.pop(contato)
  print()
  print(">>>>> Contato:{} excluido com sucesso".format(contato))
  print()

def imprimir_menu():
  print("---------------------------")
  print("1 - Mostrar todos os contatos da agenda")
  print("2 - Buscar contato")
  print("3 - incluir contado")
  print("4 - editar contato")
  print("5 - exlcuir contato")
  print("0 - sair do programa")

while True:

  imprimir_menu()
  opcao = input('Escolha uma opçaõ: ')
  print(opcao)

  if opcao == "1":
    mostrar_contatos()

  elif opcao == "2":
    contato = input("digite um nome do contato")
    buscar_contato(contato) 

  elif opcao == "3" or opcao == "4":
    contato = input("digite um nome do contato")
    telefone = input("digite um número de contato")
    email = input("digite um email")
    endereco = input("digite o endereço")
    incluir_editar_contato(contato,telefone,email,endereco)

  elif opcao == "5":
    contato = input("digite um nome do contato")
    excluir_contato(contato)

  elif opcao == "0":
   print(">>>>> fechando o programa")
   break

  else:
   print(">>>>> opaço inválida")   