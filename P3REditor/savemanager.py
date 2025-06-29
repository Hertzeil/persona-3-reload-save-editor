import json
import os
import tempfile

from P3REditor.encryption import Encryption
from P3REditor.p3rsave import P3RSave
from SavConverter import read_sav, sav_to_json, json_to_sav


class SaveManager:
    _encryption_key = "ae5zeitaix1joowooNgie3fahP5Ohph"

    def __init__(self):
        self._encryption = Encryption(self._encryption_key)
        self._encrypted_save = False
        self._file_name = None
        self._folder_path = None
        self._complete_path = None
        self._json_content = None

    def load(self, filename):
        self._complete_path = os.path.split(os.path.abspath(filename))
        self._folder_path = self._complete_path[0]
        self._file_name = self._complete_path[1]

        try:
            properties = read_sav(self._complete_path)
            self._json_content = sav_to_json(properties, string = True)
            self._encrypted_save = False
        except Exception: # file is encrypted
            dec_file = self.decrypt_file()
            self._encrypted_save = True
            properties = read_sav(dec_file)
            self._json_content = sav_to_json(properties, string = True)
            os.remove(dec_file)

        return P3RSave(self._json_content)

    def save(self, p3rsave: P3RSave):
        bin_file = json_to_sav(p3rsave.json_obj)
        if self._encrypted_save:
            with tempfile.NamedTemporaryFile(mode='wb', suffix='.sav', delete=False) as f:
                f.write(bin_file)
                temp_file_path = f.name
                f.flush()
            enc_data = self._encryption.xor_shift(temp_file_path, "enc")
            os.remove(temp_file_path)
        else:
            enc_data = bin_file
        with open(os.path.join(self._folder_path, 'generated', self._file_name), 'wb') as f:
            f.write(enc_data)

    def decrypt_file(self):
        dec_data = self._encryption.xor_shift(os.path.join(self._complete_path[0], self._complete_path[1]), "dec")
        with tempfile.NamedTemporaryFile(mode='wb', suffix='.sav', delete=False) as f:
            f.write(dec_data)
            f.flush()
            tmp_file_path = f.name
        return tmp_file_path
