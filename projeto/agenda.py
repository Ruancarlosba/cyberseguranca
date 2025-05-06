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
   print("--------------------")

def buscar_contato(contato):
   print("Nome:",contato)
   print("telefone:",AGENDA[contato]["telefone"])
   print("Email:",AGENDA[contato]["email"])
   print("Edereço:",AGENDA[contato]["endereco"])

mostrar_contatos()  

#buscar_contato('maria')