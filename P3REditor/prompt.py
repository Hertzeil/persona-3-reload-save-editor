import json
import tempfile

from P3REditor.p3rsave import P3RSave
from P3REditor.savemanager import SaveManager
from SavConverter import print_json


class Prompt:
    def __init__(self, p3rsave: P3RSave, savemanager: SaveManager):
        self._listen_input = False
        self.p3rsave = p3rsave
        self.savemanager = savemanager
        self.base_commands = {
            'save': self.save,
            'json': self.json,
            'help': self.print_usage,
            'exit': self.quit,
            'quit': self.quit
        }
        self.arg_commands = {
            'get': self.get_attribute,
            'set': self.set_attribute,
        }

    def run(self):
        self._listen_input = True
        print('Type help to see usages')
        while self._listen_input:
            command = input('P3REditor> ').lower()
            command_detail = command.split(' ')
            if len(command_detail) == 1:
                self.base_commands[command_detail[0]]()
            elif len(command_detail) == 2:
                self.arg_commands[command_detail[0]](command_detail[1])
            else:
                print('Command not recognised')
                self.print_usage()

    def print_usage(self):
        print("""Usage:
    exit|quit : to exit
    save : save edited data in the save file
    print : show editable value
    edit 'value_name' : edit the value of 'value_name'
    get 'value_name' : get the value of 'value_name'
            """)

    def quit(self):
        print("Exiting...")
        self._listen_input = False

    def get_attribute(self, element_name):
        if element_name == 'save_slot_name' :
            obj = self.p3rsave.get_save_slot_name()
        elif element_name == 'save_game_version' :
            obj = self.p3rsave.get_save_game_version()
        elif element_name == 'firstname':
            obj = self.p3rsave.get_firstname()
        elif element_name == 'lastname':
            obj = self.p3rsave.get_lastname()
        else:
            obj = ''
        print("current value : " + obj)

    def set_attribute(self, element_name):
        new_value = input('Enter new value: ')
        if element_name == 'firstname':
            self.p3rsave.set_firstname(new_value)
        elif element_name == 'lastname':
            self.p3rsave.set_lastname(new_value)
    def json(self):
        '''
        with tempfile.NamedTemporaryFile(mode="wb", suffix=".json") as f:
            json.dump(self.p3rsave.json_obj, f, indent=2)
            temp_file_path = f.name
            f.flush()
            print(temp_file_path)
        '''
        print_json(self.p3rsave.json_obj)
    def save(self):
        self.savemanager.save(self.p3rsave)