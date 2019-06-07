def find_blocked(ips, name):
	blacklisted = []

	for ip in ips:
		if ip['Blacklisted_Count'] != '0':
			for rbl in ip['Blacklisted_On']:
				if rbl['RBL'] == str(name):
					blacklisted.append(ip['Target'])
					print('Listed IP found: {}'.format(ip['Target']))

	print('{} IPs listed found in {}'.format(len(blacklisted), name))
	return blacklisted

def count(ips):
	rbl_count = {}

	for ip in ips:
		if ip['Blacklisted_Count'] != '0':
			for rbl in ip['Blacklisted_On']:
				rbl_count[rbl['RBL']] = rbl_count.get(rbl['RBL'], 0) + 1	

	return rbl_count

def list_all(ips):
	listed = {}

	for ip in ips:
		if ip['Blacklisted_Count'] != '0':
			for rbl in ip['Blacklisted_On']:
				listed[ip['Target']] = listed.get(ip['Target'], [])
				listed[ip['Target']].append(rbl['RBL'])
	
	return listed