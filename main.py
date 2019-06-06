from selenium import webdriver
import blacklist
import monitors
import delist
import json
import pprint

try: 
    # Tenta usar arquivo de cache
    with open('cached_data.json', 'r') as f:
        print('Cached data found, using the file.')
        ips = json.load(f)
except FileNotFoundError:
    # Buscar ips bloqueados
    print('Cached data not found, updating.')
    ips = monitors.get_data()

# Salva novo cache
with open('cached_data.json', 'w') as f:
    json.dump(ips, f)

# Printa o resumo de blacklists
bl_count = blacklist.count(ips)

pprint.pprint(sorted(bl_count.items(), key=lambda x: x[1], reverse=True))

# # Identifica quais IPs estão listados em 'dnsrbl.org'
# blacklisted = blacklist.find_blocked(ips, 'dnsrbl.org')

# # Chama Selenium para Delistar IPs
# if blacklisted: delist.dnsrbl(blacklisted)

print('Finished!')