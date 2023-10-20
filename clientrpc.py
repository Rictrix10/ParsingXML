import xmlrpc.client

# Conectar ao servidor RPC
proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')

# Solicitar ao usuário que insira o país da pessoa
pais = input("Introduza o país da pessoa: ")

# Chamar a função no servidor RPC com base na entrada do usuário
resultado = proxy.buscar_dados_por_pais(pais)

# Imprimir os resultados
if resultado:
    for pessoa in resultado:
        print(f"ID: {pessoa['id']}, Nome: {pessoa['first_name']} {pessoa['last_name']}, País: {pessoa['country']}, Idade: {pessoa['age']}")
else:
    print(f"Nenhuma pessoa encontrada com o país: {pais}")
