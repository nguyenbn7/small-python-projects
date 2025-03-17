import hashlib

import requests


def count_password_leaks(response: requests.Response, hash_to_check: str):
    hashes = (line.split(":") for line in response.text.splitlines())
    for hash, count in hashes:
        if hash == hash_to_check:
            return count
    return 0


def make_request_to_pwnedpasswords(first_5_hash_chars: str):
    url = "https://api.pwnedpasswords.com/range/" + first_5_hash_chars
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {response.status_code}, check the api and try again"
        )
    return response


def get_password_leaks_count(password: str):
    hashed_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_chars, tail = hashed_password[:5], hashed_password[5:]
    response = make_request_to_pwnedpasswords(first5_chars)
    return count_password_leaks(response, tail)
