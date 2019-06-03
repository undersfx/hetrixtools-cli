def find_blocked(ips, rbl):
	blacklisted = []

	for ip in ips:
		if ip['Blacklisted_Count'] != '0':
			for rbl in ip['Blacklisted_On']:
				if rbl['RBL'] == str(rbl):
					blacklisted.append(ip['Target'])
					print('Listed IP found: {}'.format(ip['Target']))

	print('Total listed IPs found: {}'.format(len(blacklisted)))
	return blacklisted

def count():
	pass