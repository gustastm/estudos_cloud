with open ("app.conf" ,"r") as config:
    for linha in config:
        if linha.startswith("#"):
            continue
        print(linha.strip())