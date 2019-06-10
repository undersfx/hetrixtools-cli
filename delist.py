'''
Module that interact with blacklists process of delisting
'''

from selenium import webdriver

def dnsrbl(ips):
	'''Run the delist process for the blacklist dnsrbl.org for the given IPs

	:type ips: dict
	:param ips: result of monitor api request (monitor.get_data)
	'''

	browser = webdriver.Chrome()
	
	for ip in ips:
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