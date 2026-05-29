print("Análise arquivo serviços...")

with open ("servicos.txt" ,"r") as origem:
    with open ("auditoria_inativos.txt" ,"a") as destino:
        for linha in origem:
            if "INATIVO" in linha:
                destino.write(linha)

print("Auditoria finalizada. Dados gravados.")            
        

