import requests  # Importamos a biblioteca que acabámos de instalar

print("=== CONECTANDO À API DA INTERNET ===")

# Vamos usar uma API pública que diz quantos astronautas estão no espaço agora
url = "http://api.open-notify.org/astros.json"

# O Python vai "bater à porta" desse site e guardar a resposta
resposta = requests.get(url)

# Se a resposta for 200, significa que a conexão foi um sucesso!
if resposta.status_code == 200:
    print("✅ Conexão bem-sucedida!")
    
    # Transformamos os dados que vieram da internet num formato que o Python entende (JSON/Dicionário)
    dados = resposta.json()
    
    # Vamos ver quantos astronautas estão lá em cima
    numero_astronautas = dados["quantidade"]
    print(f"\nNeste momento, existem {numero_astronautas} pessoas no espaço!")
    print("--------------------------------------------------")
    
    # Agora usamos o 'for' que aprendeste para listar o nome de cada um
    print("Nome dos astronautas atualmente em órbita:")
    for pessoa in dados["people"]:
        print(f"- {pessoa['name']} (Nave: {pessoa['craft']})")

else:
    print(f"❌ Erro ao conectar à API. Código de status: {resposta.status_code}")

print("\n=== FIM DA REQUISIÇÃO ===")