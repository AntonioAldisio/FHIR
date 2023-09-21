
from jobs.carregar_dados_pacientes import carregar_dados_pacientes
from jobs.carregar_dados_observacao import carregar_dados_observacao
from jobs.ler_dados_csv import ler_dados_csv


if __name__ == "__main__":
    dados = ler_dados_csv()

    carregar_dados_pacientes(dados)
    carregar_dados_observacao(dados)
