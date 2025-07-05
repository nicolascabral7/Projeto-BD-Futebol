def validar_idade(idade_str):
    try:
        idade = int(idade_str)
        if idade > 0:
            return idade
        else:
            print("Idade deve ser maior que zero.")
            return None
    except ValueError:
        print("Idade inválida. Digite um número inteiro.")
        return None

def validar_data(data_str):
    # Espera data no formato AAAA-MM-DD
    import datetime
    try:
        datetime.datetime.strptime(data_str, "%Y-%m-%d")
        return data_str
    except ValueError:
        print("Data inválida. Use o formato AAAA-MM-DD.")
        return None
