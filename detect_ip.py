#!/usr/bin/env python3

import requests
ip = requests.get('https://api.ipify.org').content.decode('utf8')
print('My public IP address is: {}'.format(ip))
