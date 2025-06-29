import os


class Encryption:
    def __init__(self):
        pass

    @staticmethod
    def xor_shift(file, key, mode):
        keylen = len(key)
        with open(file, 'rb') as f:
            data1 = f.read()
        filesize = os.path.getsize(file)
        crypt_data = bytearray(filesize)

        for i in range(filesize):
            key_idx = i % keylen
            if mode == "dec":
                b_var1 = data1[i] ^ ord(key[key_idx])
                crypt_data[i] = (b_var1 >> 4 & 3 | (b_var1 & 3) << 4 | b_var1 & 0xcc)
            elif mode == "enc":
                crypt_data[i] = (
                            (((data1[i] & 0xff) >> 4) & 3 | (data1[i] & 3) << 4 | data1[i] & 0xcc) ^ ord(key[key_idx]))
        return crypt_data
