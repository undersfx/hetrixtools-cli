from selenium import webdriver
import blacklist
import monitors
import delist

# Buscar ips bloqueados
ips = monitors.get_data()

# Identifica quais IPs estão listados em 'dnsrbl.org'
blacklisted = blacklist.find_blocked(ips, 'dnsrbl.org')

# Chama Selenium para Delistar IPs
if blacklisted: delist.dnsrbl(blacklisted)

print('Finished!')