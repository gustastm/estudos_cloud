with open ("testecarga.log" ,"w") as dados:
    for i in range (1, 6):
        dados.write("Processo de numero {i} executado.\n")
