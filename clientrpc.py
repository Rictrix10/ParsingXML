import xmlrpc.client
import psycopg2
import os
import time

# Conectar ao servidor RPC
proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')

def resultados(resultado):
    if resultado:

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
            input("Insira qualquer tecla para continuar!")
        except Exception as e:
            conn.rollback()
            print(f"\nOcorreu um erro ao inserir os dados no banco de dados: \033[91m{e}\033[0m ")
            input("Insira qualquer tecla para continuar!")
        finally:
            cursor.close()
            conn.close()
    else:
        print("\nNenhum dado encontrado.")
        input("\nInsira qualquer tecla para continuar!")

while True:
    os.system('cls')
    print("<--Escolha uma opção-->")
    print("< 1 - País            >")
    print("< 2 - Primeiro nome   >")
    print("< 3 - Último nome     >")
    print("< 4 - Idade           >")
    print("< 0 - Sair            >")
    print("<--------------------->")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        os.system('cls')
        pais = input("Insira o seu pais: ")
        type = 1
        resultado = proxy.buscar_dados_por_pais(pais,type)
        resultados(resultado)
    elif escolha == '2':
        os.system('cls')
        first_name = input("Insira o seu Primeiro nome: ")
        type = 2
        resultado = proxy.buscar_dados_por_pais(first_name,type)

        resultados(resultado)
    elif escolha == '3':
        os.system('cls')
        last_name = input("Insira o seu último nome: ")
        type = 3
        resultado = proxy.buscar_dados_por_pais(last_name,type)
        resultados(resultado)
    elif escolha == '4':
        os.system('cls')
        age = input("Insira a idade: ")
        type = 4
        resultado = proxy.buscar_dados_por_pais(age,type)
        resultados(resultado)
    elif escolha == '0':
        print("A sair")
        for _ in range(3):
            time.sleep(1)  
            print(".") 
        break  

    else:
        print("Opção inválida. Tente novamente.")

# Chamar a função no servidor RPC com base na entrada do usuário

