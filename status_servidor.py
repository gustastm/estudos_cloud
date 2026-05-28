# 1. Nossas variáveis (Simulando os dados que viriam de um servidor)
nome_do_servidor = "Banco-de-Dados-Principal"
memoria_usada = 40  # Isso representa 40% de uso
status_ativo = True

print(f"Iniciando diagnóstico do servidor: {nome_do_servidor}")
print("--------------------------------------------------")

# 2. A nossa Lógica de Decisão (Onde o DevOps brilha)
if memoria_usada > 80:
    print(f"🚨 ALERTA CRÍTICO: Uso de memória em {memoria_usada}%!")
    print("Ação Automática: Subindo um servidor extra para ajudar na carga...")
else:
    print(f"✅ STATUS OK: Uso de memória em {memoria_usada}%.")
    print("Ação: Nenhuma intervenção necessária no momento.")

print("--------------------------------------------------")
print("Diagnóstico finalizado.")