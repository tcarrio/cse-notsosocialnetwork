import requests

def get_status_codes():
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
    return status_codes


def main():
    return (200 in get_status_codes())

if __name__=="__main__":
    main()