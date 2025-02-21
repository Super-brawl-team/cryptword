import json
from Cryptography.RC4Encrypter import RC4Encrypter as RC4

class CryptoRc4:
    def __init__(self, key):
        print(key)
        self.key = key.encode('utf-8')
        self.nonce = b'nonce'
        self.RC4_Stream = RC4(self.key + self.nonce)
        self.RC4_Stream.update(self.key + self.nonce)
        self.RC4_Stream2 = RC4(self.key + self.nonce)
        self.RC4_Stream2.update(self.key + self.nonce)

    def decrypt(self, data):
        return self.RC4_Stream.update(data)

    def encrypt(self, data):
        return self.RC4_Stream2.update(data)