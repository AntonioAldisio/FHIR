import csv


def ler_dados_csv():
    try:
        caminho_arquivo = './src/data/patients.csv'

        dados_pacientes = []

        with open(caminho_arquivo, newline='', encoding='UTF-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            for linha in leitor_csv:
                dados_pacientes.append(linha)

        return dados_pacientes
    except Exception as e:
        print(e)
