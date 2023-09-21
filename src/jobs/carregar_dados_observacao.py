from get.pacient_id import get_id
from post.condition import post_condition
from post.observation import post_observation


def carregar_dados_observacao(data):
    try:
        for paciente in data:
            if (paciente['Observacao']):
                observacao = paciente['Observacao'].split('|')
                _id = get_id(paciente['CPF'])
                for condicao in observacao:
                    if (condicao == 'Gestante'):
                        post_observation(_id, condicao)
                    else:
                        post_condition(_id, condicao)
    except Exception as e:
        print(e)
