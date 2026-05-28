# Temos uma lista com apenas 2 servidores 
servidores = ["Web-01", "Banco-01"]

print("Iniciando tentativa de conexão...")

# A linha abaixo VAI EXPLODIR (IndexError), porque a posição 5 não existe!
# SUA TAREFA: Crie o 'try:' e o 'except IndexError:' para blindar essa falha.
try:
    print(f"Conectando ao servidor: {servidores[5]}")

except:
    print("Aviso: Não foi possível concectar ao servidor!")    

# O objetivo é fazer o código sobreviver até chegar aqui:
print("Rotina de conexão encerrada com segurança.")