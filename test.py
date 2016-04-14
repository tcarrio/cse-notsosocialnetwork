import requests
import config.env_config as Conf

def get_status_codes():
    base_url = 'http://{}:{}/'.format(Conf.ProductionConfig['EXT_IP'],str(Conf.ProductionConfig['EXT_PORT']))
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
    return status_codes


def main():
    return (200 in get_status_codes())

if __name__=="__main__":
    main()