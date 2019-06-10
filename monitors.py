import requests

def get_data():
    '''Retrieve all data from blacklist monitors'''

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

    url = 'https://api.hetrixtools.com/v2/a8b6c925e6d01613deaf5f5c48581f8f/blacklist/monitors/0/1024/'
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