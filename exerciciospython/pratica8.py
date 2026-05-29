with open ("grupos.txt" ,"r") as origem:
    with open("grupos_backup.txt" ,"w") as destino:
        for linha in origem:
            destino.write(linha)

print(f"Finalizado backup do arquivo de origem: {origem.name} para {destino.name}")
