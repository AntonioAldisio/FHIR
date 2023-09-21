import requests


def get_id(cpf):
    try:
        url_get_id_pacient = 'http://0.0.0.0:8080/fhir/Patient?identifier='+cpf
        retorno = requests.get(url_get_id_pacient)
        retorno_json = retorno.json()
        _id = retorno_json.get('entry')[0].get('resource').get('id')
        return _id
    except Exception as e:
        print(f"Problema em get_id:" + e)
