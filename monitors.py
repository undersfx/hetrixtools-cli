'''
Module that interact with the blacklist monitors API of hentrixtools
'''

import requests

def get_data(url):
    '''Retrieve all data from blacklist monitors
    
    :type url: string
    :param url: Start url from hetrixtools blacklist monitors API
    '''

    monitors = []

    def get_page(url):
        '''Retrieve data from a specific blacklist monitors page

        :type url: string
        :param url: blacklist monitor page API url
        '''
        print('Parsing Data from: {}'.format(url))
        r = requests.get(url)
        json_data = r.json()
        return json_data

    json_data = get_page(url)

    while True:
        try:
            for ip in json_data[0]:
                monitors.append(ip)
                
            url = json_data[1]['Links']['Pages']['Next']
            json_data = get_page(url)
        except KeyError:
            break

    print('Gathered data from {} IPs!'.format(len(monitors)))

    return monitors