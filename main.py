from P3REditor.OpenSave import OpenSave

CREDITS = "https://github.com/afkaf/Python-GVAS-JSON-Converter"
import os, sys

if len(sys.argv) > 1:
    try:
        a = sys.argv[1].replace('"', "")
        a = OpenSave().Load(os.path.split(os.path.abspath(a))[0], 0, os.path.split(os.path.abspath(a))[1], True)
    except FileNotFoundError:
        raise FileNotFoundError("Bad path\n")
    except PermissionError:
        raise FileNotFoundError("Permission error or Bad path error\n")
    except Exception as e:
        if "Failed to read HeaderProperty" in str(e):
            raise Exception("Invalid file format (not persona 3 reload GVAS)")
else:
    while True:
        try:
            a = input("Persona3 Reload sav path : ").replace('"', "")
            a = OpenSave().Load(os.path.split(os.path.abspath(a))[0], 0, os.path.split(os.path.abspath(a))[1], True)
        except FileNotFoundError:
            print("Bad path\n")
        except PermissionError:
            print("Permission error or Bad path error\n")
        except Exception as e:
            if "Failed to read HeaderProperty" in str(e):
                raise Exception("Invalid file format (not persona 3 reload GVAS)")
