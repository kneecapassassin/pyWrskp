import sys
import json
import random
import os
sys.path.append('../coder-decoder')
from coder import CoderDecoder as Coder


class Sender:
    def __init__(self):
        self.remote_coder = Coder(print_info=False)
        self.remote_coder_2 = Coder(print_info=False)
        self.remote_coder_3 = Coder(print_info=False)
        self.remote_coder_4 = Coder(print_info=False)

    def create_note(self):
        print('What would you like the password to be?')
        password = input('The person who decodes this needs to know it')
        message = input('What is the message that you would like to send?')
        key = random.randint(0, len(self.remote_coder.abcs) - 1)
        key_for_the_key = random.randint(0, len(self.remote_coder.abcs) - 1)

        self.remote_coder.add_vars(message, key)
        message = self.remote_coder.code()

        self.remote_coder_2.add_vars(password, key)
        password = self.remote_coder_2.code()

        self.remote_coder_3.add_vars(str(key), key_for_the_key)
        key = self.remote_coder_3.code()

        self.remote_coder_4.add_vars(str(key_for_the_key), 15)
        key_for_the_key = self.remote_coder_4.code()

        destroy = input('Would you like the file to be destoryed after reading?\n'
                        'Will be destroyed either way if password is inputed wrong\n'
                        'y/n\n')

        items = []
        for i in range(5):
            item1 = ''
            item2 = ''
            for c in range(6):
                item1 += self.remote_coder.abcs[random.randint(0, len(self.remote_coder.abcs) - 1)]
                item2 += self.remote_coder.abcs[random.randint(0, len(self.remote_coder.abcs) - 1)]
            items.append([item1, item2])

        save_dic = {items[0][0]: items[0][1],
                    'asuydhausdhuashd': password,
                    items[1][0]: items[1][1],
                    'sdifhuegtsydftyas': message,
                    items[2][0]: items[2][1],
                    'asdyatsdftras': key,
                    items[3][0]: items[3][1],
                    'd': destroy,
                    items[4][0]: items[4][1],
                    'gjfosjodjif': key_for_the_key}

        print(save_dic)

        with open('message.txt', 'w') as outfile:
            json.dump(save_dic, outfile)

    def read_note(self):
        try:
            with open('message.txt') as json_file:
                dic = json.load(json_file)
        except FileNotFoundError:
            print('There is no file like this (make sure it is called message.txt)')
            exit(404)

        self.remote_coder_4.add_vars(dic['gjfosjodjif'], 15)
        key_for_the_key = self.remote_coder_4.decode()

        self.remote_coder_3.add_vars(dic['asdyatsdftras'], key_for_the_key)
        key = int(self.remote_coder_3.decode())

        password = input('What is the password?')

        self.remote_coder_2.add_vars(dic['asuydhausdhuashd'], key)
        password_check = self.remote_coder_2.decode()

        if password != password_check:
            print('password incorrect deleting file')
            os.remove("message.txt")
            exit(500)

        self.remote_coder.add_vars(dic['sdifhuegtsydftyas'], key)
        message = self.remote_coder.decode()

        print('The message in this file is:')
        print(message)

        if dic['d'] == 'y':
            print('destroying file')
            os.remove('message.txt')
        else:
            print('The person who sent you this .txt file has decieded that it is not nessary to delete the file,')
            print('Though you may do so if you it it nessary')


if __name__ == '__main__':
    sender = Sender()
    do = input('What do you wish to do?')
    if do == 'create':
        sender.create_note()
    elif do == 'read':
        sender.read_note()
