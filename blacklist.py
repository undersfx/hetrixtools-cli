def find_blocked(ips, blacklist):
	'''Search the IPs data for blacklisted in given blacklist

	:type ips: dict
	:type blacklist: string
	:param ips: result of monitor api request (monitor.get_data)
	:param blacklist: dns lookup address of the blacklist
	'''
	blacklisted = []

	for ip in ips:
		if ip['Blacklisted_Count'] != '0':
			for rbl in ip['Blacklisted_On']:
				if rbl['RBL'] == str(blacklist):
					blacklisted.append(ip['Target'])
					print('Listed IP found: {}'.format(ip['Target']))

	print('{} IPs listed found in {}'.format(len(blacklisted), blacklist))
	return blacklisted

def count(ips):
	'''Count the total of IPs listed in each blacklist

	:type ips: dict
	:param ips: result of monitor api request (monitor.get_data)
	'''
	rbl_count = {}

	for ip in ips:
		if ip['Blacklisted_Count'] != '0':
			for rbl in ip['Blacklisted_On']:
				rbl_count[rbl['RBL']] = rbl_count.get(rbl['RBL'], 0) + 1	

	return rbl_count

def list_all(ips):
	'''List all IPs listed and their related blacklists

	:type ips: dict
	:param ips: result of monitor api request (monitor.get_data)
	'''

	listed = {}

	for ip in ips:
		if ip['Blacklisted_Count'] != '0':
			for rbl in ip['Blacklisted_On']:
				listed[ip['Target']] = listed.get(ip['Target'], [])
				listed[ip['Target']].append(rbl['RBL'])
	
	return listed