import binascii
import json

from P3REditor.p3rpaddings import P3RPaddings
from SavConverter import get_object_by_path, print_json, replace_object_by_path


class P3RSave:
    def __init__(self, json_content):
        self.json_obj = json.loads(json_content)
        self.offset = P3RPaddings.offset[self.get_save_game_version()]

    def get_save_game_version(self):
        path = [0, 'save_game_version']
        return get_object_by_path(self.json_obj, path)

    def get_save_slot_name(self):
        #return self.json_content[0]
        path = [1, "value", 1, "value"]
        return get_object_by_path(self.json_obj, path)

    def get_firstname(self):
        '''
        firstname = []
        path = [1, "value"]
        objs = get_object_by_path(self.json_obj, path)
        for obj in objs:
            if obj["type"] == "Int8Property" and obj['name'] == 'FirstName':
                firstname.append(obj['value'])
        return ''.join(map(chr, firstname))
        '''
        firstname = []
        for i in range(0, 7):
            firstname.append(self.get_value(P3RPaddings.firstname + i))
        return ''.join(map(chr, firstname))

    def set_firstname(self, value):
        self.set_gameheadder_string('FirstName', value)

    def get_lastname(self):
        lastname = []
        path = [1, "value"]
        objs = get_object_by_path(self.json_obj, path)
        for obj in objs:
            if obj["type"] == "Int8Property" and obj['name'] == 'LastName':
                lastname.append(obj['value'])
        return ''.join(map(chr, lastname))

    def set_lastname(self, value):
        self.set_gameheadder_string('LastName', value)


    def get_money(self):
        return str(self.get_value(P3RPaddings.money))

    def set_money(self, value):
        self.set_value(P3RPaddings.money, value)

    # Utils functions

    def get_gameheadder_string(self, type_value):
        string_value = []
        path = [1, "value"]
        objs = get_object_by_path(self.json_obj, path)
        for obj in objs:
            if obj["type"] == "Int8Property" and obj['name'] == type_value:
                string_value.append(obj['value'])
        return ''.join(map(chr, string_value))

    def set_gameheadder_string(self, type_value, new_value):
        newvalue_objs = []
        for it, char in enumerate(new_value):
            new_obj = {
                "type": "Int8Property",
                "name": type_value,
                "padding_static": "01000000",
                "padding" : "{:02d}".format(it) + "000000",
                "value": ord(char)
            }
            newvalue_objs.append(new_obj)
        self.inject_new_gameheadder(type_value, newvalue_objs)

    def inject_new_gameheadder(self, toinject_type, toinject_objs):
        path = [1, "value"]
        objs = get_object_by_path(self.json_obj, path)
        new_objs = []
        injected = False
        for index, obj in enumerate(objs):
            if 'name' in obj and obj['name'] == toinject_type:
                if not injected:
                    for toinject_obj in toinject_objs:
                        new_objs.append(toinject_obj)
                    injected = True
                else:
                    pass
            else:
                new_objs.append(obj)

        self.json_obj[1]['value'] = new_objs

    def get_value(self, padding):
        for obj in self.json_obj:
            if obj['type'] == "UInt32Property" and obj['name'] == "SaveDataArea":
                if int.from_bytes(binascii.unhexlify(obj['padding']), byteorder="little") ==  padding + self.offset:
                    return obj['value']
        raise Exception("Value not found")

    def set_value(self, padding, new_value):
        for obj in self.json_obj:
            if obj['type'] == "UInt32Property" and obj['name'] == "SaveDataArea":
                if int.from_bytes(binascii.unhexlify(obj['padding']), byteorder="little") ==  padding + self.offset:
                    obj['value'] = new_value
        raise Exception("Value not found")