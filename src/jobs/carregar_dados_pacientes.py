from parse.gender import parse_gender
from parse.name import parse_name
from datetime import datetime
import requests


def carregar_dados_pacientes(data):
    try:
        endpoint = "http://0.0.0.0:8080/fhir/Patient"

        for paciente in data:
            primeiro_nome, sobrenome = parse_name(paciente["Nome"])
            paciente_fhir = {
                "resourceType": "Patient",
                "identifier": [{
                    "system": "http://0.0.0.0.com:8080/fhir/patient-identifier",
                    "value": str(paciente['CPF'])
                    }
                ],
                "name": [{
                    "given": primeiro_nome,
                    "family": sobrenome
                    }
                ],
                "telecom": [{"system": "phone", "value": paciente['Telefone']}],
                "birthDate": datetime.strptime(paciente['Data de Nascimento'],"%d/%m/%Y").strftime("%Y-%m-%d"),
                "gender": parse_gender(paciente['Genero']),
                "address": [{"country": paciente['Pais de Nascimento']}]
            }
            response = requests.post(endpoint, json=paciente_fhir)

            if response.status_code == 201:
                print(f"Paciente {paciente['Nome']} criado com sucesso.")
            else:
                print(f"""Falha ao criar paciente {paciente['Nome']} ->
                        Status code: {response.status_code}""")
    except Exception as e:
        print(e)