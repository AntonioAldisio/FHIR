import requests


def post_condition(id, condition):
    try:
        url_observation = 'http://localhost:8080/fhir/Condition'
        body = {
            "resourceType": "Condition",
            "type": {
                "coding": [
                    {
                        "system": "http://0.0.0.0/CodeSystem/",
                        "display": str(condition)
                    }
                ]
            },
            "subject": {
                "reference": "Patient/"+id
            }
        }
        response = requests.post(url_observation, json=body)

        if response.status_code == 201:
            print(f"Adicionado com sucesso ")
        else:
            print(f"""Falha ao criar""")
    except Exception as e:
        print(f"Problema em post_condition:" + e)
