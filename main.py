from P3REditor.OpenSave import OpenSave

CREDITS = "https://github.com/afkaf/Python-GVAS-JSON-Converter"
import os, sys, logging

if len(sys.argv) > 1:
    try:
        a = sys.argv[1].replace('"', "")
        a = OpenSave().load(os.path.split(os.path.abspath(a))[0], 0, os.path.split(os.path.abspath(a))[1], True)
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
            if a == "exit" or a == "quit":
                sys.exit()
            else:
                OpenSave().load(os.path.split(os.path.abspath(a))[0], 0, os.path.split(os.path.abspath(a))[1], True)
        except FileNotFoundError:
            logging.error("Bad path\n")
        except PermissionError:
            logging.error("Permission error or Bad path error\n")
        except Exception as e:
            if "Failed to read HeaderProperty" in str(e):
                raise Exception("Invalid file format (not persona 3 reload GVAS)")
