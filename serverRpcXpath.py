import xml.etree.ElementTree as ET
import xmlrpc.server

def buscar_dados_por_pais(info, type):
    tree = ET.parse('dataset.xml')
    root = tree.getroot()
    
    resultado = []
    for person in root.findall('.//Person'):
        country_element = person.find('country') if type == 1 else \
                         person.find('first_name') if type == 2 else \
                         person.find('last_name') if type == 3 else \
                         person.find('age')
        
        if country_element is not None and country_element.text == info:
            resultado.append({
                'id': person.find('id').text,
                'first_name': person.find('first_name').text,
                'last_name': person.find('last_name').text,
                'country': country_element.text,
                'age': person.find('age').text
            })
    
    return resultado

server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000))
server.register_function(buscar_dados_por_pais, 'buscar_dados_por_pais')

print("Servidor RPC aguardando solicitações...")
server.serve_forever()
