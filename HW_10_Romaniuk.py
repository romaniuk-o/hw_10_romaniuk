

'''
-AddressBook, который наследуется от UserDict, и мы потом добавим логику поиска по записям в этот класс.
-Класс Record, который отвечает за логику добавления/удаления/редактирования необязательных полей и хранения обязательного поля Name.
-Класс Field, который будет родительским для всех полей, в нем потом реализуем логику общую для всех полей.
-Класс Name, обязательное поле с именем.
-Класс Phone, необязательное поле с телефоном и таких одна запись(Record) может содержать несколько.

Критерии приёма
-Реализованы все классы из задания.
-Записи Record в AddressBook хранятся как значения в словаре. В качестве ключей используется значение Record.name.value.
-Record хранит объект Name в отдельном атрибуте.
-Record хранит список объектов Phone в отдельном атрибуте.
-Record реализует методы для добавления/удаления/редактирования объектов Phone.
-AddressBook реализует метод add_record, который добавляет Record в self.data.
'''
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass

# Класс Record, отвечает за логику добавления/удаления/редактирования необязательных полей и хранения обязательного поля Name


class Record():
    def __init__(self, name: Name, phones=[]) -> None:
        self.name = name
        self.phone_lst = phones

    def phone_add(self, phone):
        self.phone_lst.append(phone)

    def phone_del(self, phone):
        self.phone_lst.remove(phone)

    def phone_change(self, old_phone, new_phone):
        self.phone_lst.remove(old_phone)
        self.phone_lst.append(new_phone)

    def printt(self, phone_lst):
        return phone_lst


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
#  Функція декоратор


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return('Enter user name')
        except ValueError:
            return('Value is not correct')
        except IndexError:
            return('Give me name and phone please')
        except TypeError:
            return('Enter the correct command')

    return wrapper


# __Функції____________________


@ input_error
def hello(*args) -> str:
    return 'How can I help you?'


@ input_error
def exit(*args) -> str:
    return 'Bye!'


@ input_error
def add(*args) -> str:
    name = Name(args[0])
    phone = Phone(args[1])
    if name.value in phone_book:
        if phone.value in phone_book[name.value].phone_lst:
            return f'such number alreadey is!!!'
        else:
            phone_book[name.value].phone_add(phone.value)
            return f'Number {phone.value} added to user name {name.value} !!!'
    else:
        phone_book[name.value] = Record(name.value, [phone.value])
        return 'Contact add successful!'


@ input_error
def show_all(*args):
    result = ''
    for k, v in phone_book.items():
        result += str(k) + ':' + str(v.phone_lst) + '\n'
    return result


@ input_error
def change(*args) -> str:
    name = args[0]
    old_phone = args[1]
    new_phone = args[2]
    if name in phone_book:
        phone_book[name].phone_change(old_phone, new_phone)
        return f'Phone number {old_phone} changed on {new_phone} successful!'
    else:
        return f'Contact with name {name} not found!'


@ input_error
def phone(*args) -> str:
    if len(args) == 0:
        return 'Give me name please!'
    else:
        return f'{args[0]} number is {phone_book.get(args[0])}'


@ input_error
def wrong(*args) -> str:
    return 'Unknown command'


#  Функція command_parser - парсер команд
# ___________________________________________________________________________________


COMMAND_DICT = {hello: ['hello'], phone: ['phone'], change: ['change'],  exit: ['exit', 'close', 'good bye'],
                add: ['add'], show_all: ["show all", "show"], }


# @input_error
def command_parser(comm: str):
    for k, v in COMMAND_DICT.items():
        for i in v:
            if comm.lower().startswith(i.lower()):
                return k, comm[len(i):].strip().split(' ')
    else:
        return wrong, []
 # _____________________________________________________________________________


phone_book = AddressBook()


def main():
    while True:
        user_input = input('Please type command: ')
        command, data = command_parser(user_input)
        result = command(*data)
        print(result)
        if command == exit:
            break


if __name__ == '__main__':
    main()
