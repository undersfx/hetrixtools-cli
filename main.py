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

# Chama Selenium para Delistar IPs

browser = webdriver.Chrome()

for ip in blacklisted:
	#browser.get('https://dnsrbl.org/remove.cgi?ip=177.70.232.115')
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


print('all processes completed successfully')

# DEBUG:
# print(blacklisted)
# print(len(blacklisted))

'''
json_data[0] contém a lista com dicts para cada IP
json_data[1] comtém um dict de referéncia para o próximo 

Exemplo de Retorno:

[
	[
		{
			"ID": "da32f23a389794668b03b21261fb4428",
			"Type": "IPv4",
			"Target": "177.70.224.0",
			"Add_Date": 1519929211,
			"Last_Check": 1553140206,
			"Status": "Active",
			"Label": "",
			"Contact_List_ID": "ddb7b88b880072537785efd068370f15",
			"Blacklisted_Count": "0",
			"Blacklisted_On": null,
			"Links": {
				"Report_Link": "https://hetrixtools.com/report/blacklist/b5cf91a559d71711428fa46d47b4225a/",
				"Whitelabel_Report_Link": "http://rbl.allin.com.br/report/blacklist/b5cf91a559d71711428fa46d47b4225a/"
			}
		}
	],
	{
		"Meta": {
			"Total_Records": "24576"
		},
		"Links": {
			"Pages": {
				"Next": "https://api.hetrixtools.com/v2/a8b6c925e6d01613deaf5f5c48581f8f/blacklist/monitors/1/1/"
			}
		}
	}
]

'''