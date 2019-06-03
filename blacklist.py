def find_blocked(ips, name):
	blacklisted = []

	for ip in ips:
		if ip['Blacklisted_Count'] != '0':
			for rbl in ip['Blacklisted_On']:
				if rbl['RBL'] == str(name):
					blacklisted.append(ip['Target'])
					print('Listed IP found: {}'.format(ip['Target']))

	print(f'{len(blacklisted)} IPs listed found in {name}')
	return blacklisted

def count():
	pass