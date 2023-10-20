import xmlrpc.client

# Conectar ao servidor RPC
proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')

# Solicitar dados para um país específico (por exemplo, "Brasil")
pais = 'Brazil'
resultado = proxy.buscar_dados_por_pais(pais)

# Imprimir os resultados
for pessoa in resultado:
    print(f"ID: {pessoa['id']}, Nome: {pessoa['first_name']} {pessoa['last_name']}, País: {pessoa['country']}, Idade: {pessoa['age']}")
