import hashlib


def pwd_encryption(pwd):
    new_pwd = hashlib.sha1(pwd).hexdigest()
    return new_pwd
