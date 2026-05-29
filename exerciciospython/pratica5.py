status_nos = {"web-01": "online", "web-02": "offline", "db-01": "online", "db-02": "offline"}

for servidor, status in status_nos.items():
    if status == "offline":
        print(f"CRÍTICO!: O servidor {servidor} está indisponivel.")
