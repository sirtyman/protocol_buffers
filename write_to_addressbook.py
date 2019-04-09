""" This file represents the very basics of Google protocol buffers serialization """

import addressbook_pb2


save_addressbook_file = "./addressbook.dat"


def enter_person_data(person):
    """ Initializes the Person instance with user input data """

    person.id = int(input("Enter ID: "))
    person.name = input("Enter name: ")
    person.email = input("Enter email: ")
    phone = person.phones.add()
    phone.number = input("Enter phone number: ")
    phone_type = input('Is it [mobile], [home] or [work] phone number?: ')

    if phone_type == 'mobile':
        phone.type = addressbook_pb2.Person.MOBILE
    elif phone_type == 'home':
        phone.type = addressbook_pb2.Person.HOME
    elif phone_type == 'work':
        phone.type = addressbook_pb2.Person.WORK
    else:
        phone.type = None


def read_address_book(addressbook):
    """ Reads data from save and initialize AddressBook instance with the data """

    try:
        with open(save_addressbook_file, 'rb') as sf:
            data = sf.read()
        addressbook.ParseFromString(data)
    except FileNotFoundError:
        pass


def run_until_save():
    """ The main loop of this application.

    Runs until user selects to save current AddressBook instance to save file.
    """

    addressbook = addressbook_pb2.AddressBook()
    read_address_book(addressbook)
    print(str(addressbook))

    while True:
        print("Choose option:\n[1] - to enter new person data\n[2]- to save address book\n")
        option = int(input('[???]'))
        if option == 1:
            enter_person_data(addressbook.people.add())
        elif option == 2:
            print(str(addressbook))
            with open(save_addressbook_file, 'wb') as sf:
                sf.write(addressbook.SerializeToString())
            break


if __name__ == '__main__':
    run_until_save()