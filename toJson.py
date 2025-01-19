import csv
import json

csv_file_path = 'products_clean.csv'
json_file_path = 'dados.json'

dados = []

with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    leitor = csv.DictReader(csv_file)
    for linha in leitor:
        dados.append(linha)

with open(json_file_path, mode='w', encoding='utf-16') as json_file:
    json.dump(dados, json_file, indent=4, ensure_ascii=False)

print(f"Arquivo JSON gerado com sucesso: {json_file_path}")
