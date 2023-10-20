import xmlrpc.client
import psycopg2

# Conectar ao servidor RPC
proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')

# Solicitar ao usuário que insira o país da pessoa
pais = input("Introduza o país da pessoa: ")

# Chamar a função no servidor RPC com base na entrada do usuário
resultado = proxy.buscar_dados_por_pais(pais)

if resultado:
    # Conectar ao banco de dados PostgreSQL
    conn = psycopg2.connect(
        dbname="ParsingXML",
        user="postgres",
        password="123456",
        host="localhost"
    )
    cursor = conn.cursor()

    try:
        for pessoa in resultado:
            id = pessoa['id']
            first_name = pessoa['first_name']
            last_name = pessoa['last_name']
            country = pessoa['country']
            age = pessoa['age']

            # Imprimir os detalhes da pessoa no terminal
            print(f"ID: {id}, Nome: {first_name} {last_name}, País: {country}, Idade: {age}")

            # Inserir os dados na tabela "Person"
            query = "INSERT INTO Person (id, first_name, last_name, country, age) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (id, first_name, last_name, country, age))

        conn.commit()
        print(f"Os dados das pessoas do país {pais} foram inseridos com sucesso no banco de dados.")
    except Exception as e:
        conn.rollback()
        print(f"Ocorreu um erro ao inserir os dados no banco de dados: {e}")
    finally:
        cursor.close()
        conn.close()
else:
    print(f"Nenhuma pessoa encontrada com o país: {pais}")
