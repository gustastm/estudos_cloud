valor = 0
with open ("server.log" ,"r") as log:
    for linha in log:
        if "ERROR" in linha:
            print(f"Alerta: {linha.strip()}")
            valor += 1


print(f"Foram encontrados: {valor} erros no log {log.name}")