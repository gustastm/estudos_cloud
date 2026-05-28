# 1. Uma lista de servidores (guardando dicionários com os dados de cada um)
servidores = [
    {"nome": "Web-Production-01", "memoria": 45, "ativo": True},
    {"nome": "Web-Production-02", "memoria": 89, "ativo": True},
    {"nome": "Database-Principal", "memoria": 92, "ativo": True},
    {"nome": "Auth-Service", "memoria": 30, "ativo": False},
]

print("=== INICIANDO VARREDURA DO DATA CENTER ===")

# 2. O Loop 'For' (O robô vai passar de servidor em servidor automaticamente)
for servidor in servidores:
    print(f"\nVerificando: {servidor['nome']}")
    
    # Se o servidor estiver desligado (False)pi
    if not servidor["ativo"]:
        print("❌ CRÍTICO: O servidor está FORA DO AR!")
        continue  # Pula para o próximo servidor da lista
        
    # Se estiver ativo, verifica a memória
    if servidor["memoria"] > 80:
        print(f"🚨 ALERTA: Uso de memória elevado em {servidor['memoria']}%!")
    else:
        print(f"✅ ESTÁVEL: Uso de memória em {servidor['memoria']}%")

print("\n=== VARREDURA FINALIZADA ===")