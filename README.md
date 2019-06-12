# HetrixTools CLI

CLI to extend Hetrixtools functionality and data analysis.

## Enviroment Variables

Setup of Variables needed to run the project:

### MONITORS_START_URL

API endpoint to start fetching the blacklist monitors data.

Example: `MONITORS_START_URL = 'https://api.hetrixtools.com/v2/<API_TOKEN>/blacklist/monitors/<PAGE>/<PER_PAGE>/'`

PAGE = 0

PER_PAGE = 1024 (if you are monitoring less than that you can use your total number of IPs instead)

Documentation: https://hetrixtools.com/dashboard/api-explorer/

### DNSRBLORG_LOOKUP_URL

Lookup URL for dnsrbl.org

Example: 'https://dnsrbl.org/lookup.cgi?ip='