import csv
import xml.etree.ElementTree as ET

# Lê o arquivo CSV
with open('dataset.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    
    root = ET.Element('DatasetXML')
    
    for row in csv_reader:
        person = ET.SubElement(root, 'Person')
        
        
        for key, value in row.items():
            campo = ET.SubElement(person, key)
            campo.text = value

tree = ET.ElementTree(root)

tree.write('dataset.xml', encoding='utf-8')

print("Arquivo XML gerado com sucesso.")


