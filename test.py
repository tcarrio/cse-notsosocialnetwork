import requests
from config.env_config import ProductionConfig as conf

def get_status_codes():
    base_url = '{}:{}/'.format('127.0.0.1','8080')
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
        try:
            r = requests.get('{}{}'.format(base_url,uri))
            status_codes.append(r.status_code)
        except:
            status_codes.append(500)
    return status_codes


def main():
    for ind,val in enumerate(test_urls):
        print("{}\tstatus:{}".format(test_urls[ind],str(status_codes[ind])))
    return (200 in get_status_codes())

if __name__=="__main__":
    main()