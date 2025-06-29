import os


class Encryption:

    def __init__(self, encryption_key):
        self._crypt_data = None
        self._filesize = None
        self._encryption_key = encryption_key
        self._keylen = len(encryption_key)
        self._data = None

    def xor_shift(self, file, mode):
        self.load_file(file)

        for i in range(self._filesize):
            if mode == "dec":
                self.dec_byte(i)
            elif mode == "enc":
                self.enc_byte(i)

        return self._crypt_data

    def load_file(self, file):
        with open(file, 'rb') as f:
            self._data = f.read()
        self._filesize = os.path.getsize(file)
        self._crypt_data = bytearray(self._filesize)

    def enc_byte(self, i):
        key_idx = i % self._keylen
        b_var1 = (((self._data[i] & 0xff) >> 4) & 3 | (self._data[i] & 3) << 4 | self._data[i] & 0xcc)
        b_var2 = ord(self._encryption_key[key_idx])
        self._crypt_data[i] = (b_var1 ^ b_var2)

    def dec_byte(self, i):
        key_idx = i % self._keylen
        b_var1 = self._data[i] ^ ord(self._encryption_key[key_idx])
        self._crypt_data[i] = (b_var1 >> 4 & 3 | (b_var1 & 3) << 4 | b_var1 & 0xcc)
