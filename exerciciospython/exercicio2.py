servidor = {"nome": "App-Principal", "status": "Online"}

print("Iniciando verificação...")

# TENTA executar a linha perigosa
try:
    print(f"Uso de memória: {servidor['memoria']}")

# SE DER ERRO (KeyError), faz isso em vez de travar o programa
except KeyError:
    print("Aviso: A memória não foi encontrada!")

print("Verificação finalizada com sucesso.")