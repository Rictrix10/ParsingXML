import xmlrpc.server
import xml.etree.ElementTree as ET

# Função para buscar dados com base no campo "country"
def buscar_dados_por_pais(pais):
    tree = ET.parse('dataset.xml')
    root = tree.getroot()
    
    resultado = []
    for pessoa in root.findall('pessoa'):
        country_element = pessoa.find('country')
        if country_element is not None and country_element.text == pais:
            resultado.append({
                'id': pessoa.find('id').text,
                'first_name': pessoa.find('first_name').text,
                'last_name': pessoa.find('last_name').text,
                'country': country_element.text,
                'age': pessoa.find('age').text
            })
    
    return resultado

# Criar o servidor RPC
server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000))
server.register_function(buscar_dados_por_pais, 'buscar_dados_por_pais')

print("Servidor RPC aguardando solicitações...")
server.serve_forever()
