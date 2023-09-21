def parse_gender(gender):
    try:
        if gender == 'Masculino':
            return 'male'
        if gender == 'Feminino':
            return 'female'
    except Exception as e:
        print(f"Problema em parse_gender:" + e)
