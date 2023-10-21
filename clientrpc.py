import xmlrpc.client
import psycopg2

# Conectar ao servidor RPC
proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')

def resultados(resultado):
    if resultado:

        print("a")
        # Conectar ao banco de dados PostgreSQL
        conn = psycopg2.connect(
            dbname="ParsingXML",
            user="postgres",
            password="1234",
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
            print(f"Os dados das pessoas foram inseridos com sucesso no banco de dados.")
        except Exception as e:
            conn.rollback()
            print(f"Ocorreu um erro ao inserir os dados no banco de dados: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print(f"Nenhuma pessoa encontrada com o país.")


# Solicitar ao usuário que insira o país da pessoa

while True:
    print("Escolha uma opção:")
    print("1 - País")
    print("2 - first name")
    print("3 - last name")
    print("4 - Idade")
    print("5 - Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        print("Você escolheu 'País'.")
        pais = input("Insira o seu pais")
        type = 1
        resultado = proxy.buscar_dados_por_pais(pais,type)
        resultados(resultado)
    elif escolha == '2':
        print("Você escolheu 'first name'.")
        first_name = input("Insira o seu first name")
        type = 2
        resultado = proxy.buscar_dados_por_pais(first_name,type)
        resultados(resultado)
    elif escolha == '3':
        print("Você escolheu 'last name'.")
        last_name = input("Insira o seu last name")
        type = 3
        resultado = proxy.buscar_dados_por_pais(last_name,type)
        resultados(resultado)
    elif escolha == '4':
        print("Você escolheu 'age'.")
        age = input("Insira o seu age")
        type = 4
        resultado = proxy.buscar_dados_por_pais(age,type)
        resultados(resultado)
    elif escolha == '5':
        print("Saindo do programa.")
        break  # Isso encerrará o loop.

    else:
        print("Opção inválida. Tente novamente.")

# Chamar a função no servidor RPC com base na entrada do usuário

