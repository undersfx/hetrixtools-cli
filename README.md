# HetrixTools CLI

CLI to extend Hetrixtools functionality and data analysis.

Some selenium-automated delist process included.

## Enviroment Variables

Setup of Variables needed to run the project:

`MONITORS_START_URL` setup the API endpoint to start fetching the blacklist monitors data.

Example: 
```bash
export MONITORS_START_URL = 'https://api.hetrixtools.com/v2/<API_TOKEN>/blacklist/monitors/0/<PER_PAGE>/'
```

- `<API_TOKEN>` is given to you by Hetrixtools platform.

- `<PER_PAGE>` has a maximum of 1024. If you are monitoring less than that you can use your total number of IPs instead.

`DNSRBLORG_LOOKUP_URL` setup the base URL for dnsrbl.org lookup.

Example:
```bash
export DNSRBLORG_LOOKUP_URL = 'https://dnsrbl.org/lookup.cgi?ip='
```

## Deslist Bots

Before run the automated delist processes be sure that the issue has been solved and the IPs are not sending junk anymore. 

Request delist for a IP that still sending spam will not solve your problem.

The automated processes were intended for run in Windows with Chrome (for another OSs you will need to update the browser driver and for other browsers you will need to write your own script)

## Hetrixtools API

More information abouot the Hetrixtools API [here](https://hetrixtools.com/dashboard/api-explorer/)
