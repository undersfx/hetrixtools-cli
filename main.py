from selenium import webdriver
import requests

url = 'https://api.hetrixtools.com/v2/a8b6c925e6d01613deaf5f5c48581f8f/blacklist/monitors/0/1024/'

def get_data(url):
	r = requests.get(url)
	json_data = r.json()
	return json_data

json_data = get_data(url)

# Identifica quais IPs estão listados em 'dnsrbl.org'

blacklisted = []

while True:
	print('Parsing JSON data. Size: {}'.format(len(json_data[0])))
	# json_data[0] contém a lista com dicts para cada IP
	# json_data[1] comtém um dict de referéncia para o próximo 
	for ip in json_data[0]:
		if ip['Blacklisted_Count'] != '0':
			for rbl in ip['Blacklisted_On']:
				if rbl['RBL'] == 'dnsrbl.org':
					blacklisted.append(ip['Target'])
					print('Listed IP found: {}'.format(ip['Target']))
	try:
		url = json_data[1]['Links']['Pages']['Next']
		json_data = get_data(url)
		print('Parsing Data from: {}'.format(url))
	except KeyError:
		break

print('Total listed IPs found: {}'.format(len(blacklisted)))

# Chama Selenium para Delistar IPs

if blacklisted:
	browser = webdriver.Chrome()
	
	for ip in blacklisted:
		# browser.get('https://dnsrbl.org/remove.cgi?ip=177.70.232.115')
		browser.get('https://dnsrbl.org/lookup.cgi?ip={}'.format(ip))
		print('Delisting: {}'.format(ip))
		
		try:
			elem = browser.find_element_by_css_selector('#gobutton')
			elem.click()
		except Exception as e:
			print('Erro: {}'.format(e))
			raise e
		else:
			print('{} Delisted.'.format(ip))

browser.close()

print('Finished!')