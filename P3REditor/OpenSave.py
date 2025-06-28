from P3REditor.Encryption import Encryption
from P3REditor.P3RSave import P3RSave

from SavConverter import sav_to_json, read_sav
import os, tempfile


class OpenSave:
    def __init__(self):
        pass

    def Load(self, i, mdd, e, make_bak):
        try:
            dec_data = Encryption().XORshift(i + "\\" + e, "ae5zeitaix1joowooNgie3fahP5Ohph", "dec")
            with tempfile.NamedTemporaryFile(mode='wb', suffix='.sav', delete=False) as temp_file:
                temp_file.write(dec_data)
                temp_file_path = temp_file.name
                temp_file.flush()
            json_data = sav_to_json(read_sav(temp_file_path), string=True)
            os.remove(temp_file_path)
            comp = True
        except:
            os.remove(temp_file_path)
            dec_data = open(i + "\\" + e, "rb").read()
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
        return P3RSave(temp_file_path, mdd, i, e, make_bak, comp)
