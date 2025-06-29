from P3REditor.encryption import Encryption
from P3REditor.p3rsave import P3RSave

from SavConverter import sav_to_json, read_sav
import os, tempfile


class OpenSave:
    def __init__(self):
        pass

    @staticmethod
    def load(folder_path, mdd, file_name, make_bak):
        target = os.path.join(folder_path, file_name)
        try:
            dec_data = Encryption().xor_shift(target, "ae5zeitaix1joowooNgie3fahP5Ohph", "dec")
            with tempfile.NamedTemporaryFile(mode='wb', suffix='.sav', delete=False) as temp_file:
                temp_file.write(dec_data)
                temp_file_path = temp_file.name
                temp_file.flush()
            json_data = sav_to_json(read_sav(temp_file_path), string=True)
            os.remove(temp_file_path)
            comp = True
        except:
            os.remove(temp_file_path)
            dec_data = open(target, "rb").read()
            with tempfile.NamedTemporaryFile(mode='wb', suffix='.sav', delete=False) as temp_file:
                temp_file.write(dec_data)
                temp_file_path = temp_file.name
                temp_file.flush()
            json_data = sav_to_json(read_sav(temp_file_path), string=True)
            os.remove(temp_file_path)
            comp = False

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as temp_file:
            temp_file.write(json_data)
            temp_file_path = temp_file.name
            temp_file.flush()
        return P3RSave(temp_file_path, mdd, folder_path, file_name, make_bak, comp)
