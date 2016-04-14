import requests

base_url = 'http://127.0.0.1/'
test_urls = [
    '',
    'frontpage',
    'home',
    'contacts',
    'registration',
    'aboutus',
    'profile',
    'login',
    'register',
    'search',
    'logout'
]
status_codes = []

for uri in test_urls:
    r = requests.get('{}{}'.format(base_url,uri))
    status_codes.append(r.status_code)
    

# loose testing
return (200 in status_codes)