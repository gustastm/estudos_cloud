with open ("inventario_completo.txt" ,"w") as inventariofinal:
    with open ("grupos.txt", "r")as grupo:
        for linha in grupo:
            inventariofinal.write(linha)
    
    inventariofinal.write("\n")

    with open ("auditoria_inativos.txt" ,"r") as auditoria:
        for linha in auditoria:
            inventariofinal.write(linha)

with open ("inventario_completo.txt", "r") as inventariofinal:
    for linha in inventariofinal:
        print(linha.strip())