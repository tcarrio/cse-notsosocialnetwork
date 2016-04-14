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
            print("{}\tstatus:{}".format(uri,r.status_code))
        except:
            status_codes.append(500)
            print("{}\tstatus:{}".format(uri,500))
    return status_codes


def main():
    return (200 in get_status_codes())

if __name__=="__main__":
    main()