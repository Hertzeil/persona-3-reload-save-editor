from P3REditor.p3rsave import P3RSave
from P3REditor.savemanager import SaveManager


class Prompt:
    def __init__(self, p3rsave: P3RSave, savemanager: SaveManager):
        self._listen_input = False
        self.p3rsave = p3rsave
        self.savemanager = savemanager
        self.base_commands = {
            'save': self.save,
            'help': self.print_usage,
            'exit': self.quit,
            'quit': self.quit
        }
        self.arg_commands = {
            'get': self.get_attribute,
            'set': self.set_attribute,
            'read': self.read_address,
            'write': self.write_address
        }
        self.get_attributes = {
            'save_slot_name': self.p3rsave.get_save_slot_name,
            'save_game_version': self.p3rsave.get_save_game_version,
            'firstname': self.p3rsave.get_firstname,
            'lastname': self.p3rsave.get_lastname,
            'money': self.p3rsave.get_money,
        }
        self.set_attributes = {
            'firstname': self.p3rsave.set_firstname,
            'lastname': self.p3rsave.set_lastname,
            'money': self.p3rsave.set_money,
        }

    def run(self):
        self._listen_input = True
        print('Type help to see usages')
        while self._listen_input:
            command = input('P3REditor> ').lower()
            command_detail = command.split(' ')
            if len(command_detail) == 1:
                if command_detail[0] in self.base_commands:
                    self.base_commands[command_detail[0]]()
                else:
                    print('Unknown command')
            elif len(command_detail) == 2:
                if command_detail[0] in self.arg_commands:
                    self.arg_commands[command_detail[0]](command_detail[1])
                else:
                    print('Unknown command')
            else:
                print('Unknown command')
                self.print_usage()

    def print_usage(self):
        print("""Usage:
    exit|quit : to exit
    save : save edited data in the save file
    print : show editable value
    edit 'value_name' : edit the value of 'value_name'
    get 'value_name' : get the value of 'value_name'
    read 'address' : try to read raw value at specified 'address'
    write 'address' : write raw value at specified 'address'
            """)

    def quit(self):
        print("Exiting...")
        self._listen_input = False

    def get_attribute(self, element_name):
        if element_name in self.get_attributes:
            obj = self.get_attributes[element_name]()
            print("current value : " + obj)
        else:
            print('Unknown attribute')

    def set_attribute(self, element_name):
        if element_name in self.set_attributes:
            new_value = input('Enter new value: ')
            self.set_attributes[element_name](new_value)
        else:
            print('Unknown attribute')

    def read_address(self, address):
        try:
            value = self.p3rsave.get_value(int(address))
            print('Value at address' + str(address) + ': ' + str(value))
        except:
            print('Address not found')
    def write_address(self, address):
        try:
            new_value = input('Enter new value: ')
            self.p3rsave.set_value(int(address), int(new_value))
        except:
            print('Cant write !')

    def save(self):
        self.savemanager.save(self.p3rsave)
