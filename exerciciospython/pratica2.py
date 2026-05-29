servidor_config = {"hostname": "srv-app-01", "cpu": 4, "ram": "8GB"}

try:
    print(f"Sistema Operacional: {servidor_config['os']}")

except KeyError:
    print("Falha na auditoria: Chave 'os' inexistente nos dados do servidor.")
