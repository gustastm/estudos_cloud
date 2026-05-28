# Dados simulados do nosso sistema
sistemas = [
    {"nome": "Banco de Dados", "ativo": True},
    {"nome": "Site Principal", "ativo": False},
    {"nome": "Sistema de Pagamento", "ativo": True},
    {"nome": "Fórum", "ativo": False}
]

for sistema in sistemas:
    if sistema ["ativo"]:
        print(f"O servidor {sistema['nome']}está ativo")