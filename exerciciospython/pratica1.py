ips_acesso = ["192.168.1.15", "10.0.0.5", "192.168.1.99", "172.16.0.8", "192.254.44.5"]
ip_bloqueado = ["192.168.1.99", "192.254.44.5"]

for ip in ips_acesso:
    if ip in ip_bloqueado:
        print(f"ALERTA: Tentativa de acesso bloqueada pelo firewall: [IP] {ip}")
    else:
        print(f"Acesso Liberado: [IP] {ip}")