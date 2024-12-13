import csv

def save_to_csv(data, filename):
    """
    Salva os dados em um arquivo CSV.
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Dados salvos no arquivo {filename}")