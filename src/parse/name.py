import re


def sub_name(nome_completo):
    return re.sub(r'\b(?:da|de)\s(?=[A-Z][a-z])', '', nome_completo)


def parse_name(nome_completo):
    try:
        nome_completo = sub_name(nome_completo)
        partes_nome = nome_completo.split()

        if len(partes_nome) >= 3:
            primeiros_nomes = ' '.join(partes_nome[:2])
            sobrenomes = ' '.join(partes_nome[2:])
            return primeiros_nomes, sobrenomes
        elif len(partes_nome) == 2:
            primeiros_nomes = ' '.join(partes_nome[:1])
            sobrenomes = ' '.join(partes_nome[1:])
            return primeiros_nomes, sobrenomes
        else:
            return '', ''
    except Exception as e:
        print(f"Problema em parse_name:" + e)