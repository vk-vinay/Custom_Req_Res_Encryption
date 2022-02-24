import binascii

import pyaes


class AES256:

    def __init__(self):
        self.iv = 111569809385461024177830520738942257382961841275406254376633720994528967429872
        self.key = b'Yb\xfbx\xa87\xce\x8f\x9d\xd1\x17\xf7qu~\xe7\x19\x99\xfb\x98z\xd8T*\xde\x81\x957\x02\xdb\x13\xca'

    def encrypt(self, plaintext):
        aes = pyaes.AESModeOfOperationCTR(self.key, pyaes.Counter(self.iv))
        ciphertext = aes.encrypt(plaintext)
        return binascii.hexlify(ciphertext).decode()

    def decrypt(self, ciphertext):
        aes = pyaes.AESModeOfOperationCTR(self.key, pyaes.Counter(self.iv))
        decrypted = aes.decrypt(ciphertext)
        return decrypted


