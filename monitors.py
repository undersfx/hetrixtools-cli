import requests

def get_data():
    url = 'https://api.hetrixtools.com/v2/a8b6c925e6d01613deaf5f5c48581f8f/blacklist/monitors/0/1024/'
    monitors = []

    def get(url):
        print('Parsing Data from: {}'.format(url))
        r = requests.get(url)
        json_data = r.json()
        return json_data

    json_data = get(url)

    while True:
        try:
            for ip in json_data[0]:
                monitors.append(ip)
                
            url = json_data[1]['Links']['Pages']['Next']
            json_data = get(url)
        except KeyError:
            break

    print('Monitor Finished!')
    return monitors