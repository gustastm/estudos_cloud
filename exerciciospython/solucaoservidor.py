print("Analisando possíveis erros no arquivo LOG...")

with open ("servidor.log") as arquivo:   

    for linha in arquivo:
        if "ERROR" in linha or "WARNING" in linha:
            print(linha.strip())
        else:
            print("Nenhum erro encontrado nessa linha.")