import xmlrpc.server
import xml.etree.ElementTree as ET

# Função para buscar dados com base no campo "country"
def buscar_dados_por_pais(pais):
    tree = ET.parse('dataset.xml')
    root = tree.getroot()
    
    resultado = []
    for person in root.findall('Person'):
        country_element = person.find('country')
        if country_element is not None and country_element.text == pais:
            resultado.append({
                'id': person.find('id').text,
                'first_name': person.find('first_name').text,
                'last_name': person.find('last_name').text,
                'country': country_element.text,
                'age': person.find('age').text
            })
    
    return resultado

# Criar o servidor RPC
server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000))
server.register_function(buscar_dados_por_pais, 'buscar_dados_por_pais')

print("Servidor RPC aguardando solicitações...")
server.serve_forever()
