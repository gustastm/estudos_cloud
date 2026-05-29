print("Iniciando auditoria de permissões...")
usuarios_privilegiados = []

with open("grupos.txt", "r") as origem:
    for linha in origem:
        if "admin" in linha or "root" in linha:
            usuarios_privilegiados.append(linha.strip())


print(f"\nUsuários Privilegiados: {usuarios_privilegiados}")