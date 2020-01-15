import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def password_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head = sha1password[:5]
    tail = sha1password[5:]
    response = request_api_data(head)
    return get_password_leak_count(response, tail)


def main(args):
    for password in args:
        count = password_check(password)
        if count:
            print(f'{password} was found {count}')
        else:
            print(f'{password} was not found!!!!')


main(sys.argv[1:])
