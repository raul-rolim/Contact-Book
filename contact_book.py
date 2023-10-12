import sqlite3

#Auto Increment Só funciona quando é escrito integer primary key, devido a um bug da dependência
def create_database():
    conn = sqlite3.connect('contactBook.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE if not exists contacts(
                id INTEGER PRIMARY KEY,
                first_name text not null,
                last_name text not null,
                address text not null,
                contact_number integer not null
                )""")
    conn.commit()
    conn.close()

def add_contact():
    first_name_input = input("\nInsert the First Name: ")
    last_name_input = input("\nInsert the Last Name: ")
    address_input = input("\nInsert the Contact's Address: ")
    contact_input = input("\nInsert the Contact's Number: ")

    conn = sqlite3.connect('contactBook.db')
    c = conn.cursor()

    c.execute("INSERT INTO contacts(first_name, last_name, address, contact_number) VALUES (:first_name_input, :last_name_input, :address_input, :contact_input)",
              {
                  'first_name_input': first_name_input,
                  'last_name_input': last_name_input,
                  'address_input': address_input,
                  'contact_input': contact_input
              })

    conn.commit()
    conn.close()

def search_contact():
    conn = sqlite3.connect('contactBook.db')
    global rows, c
    c = conn.cursor()
    print("\nWhat do you want to Search")
    pending_response = True

    while pending_response:
        try:
            choice = int(input("\n1 - First Name\n2 - Last Name\n3 - Address\n" +
                                    "4 - Contact Number\n5 - Return\nChoice: "))

            if choice == 1:
                search = input("\nInsert the First Name That You Want to Search: ")
                c.execute("SELECT * FROM contacts WHERE first_name = '{}'".format(search))
                lister()
                pending_response = False

            elif choice == 2:
                search = input("\nInsert the Last Name That You Want to Search: ")
                c.execute("SELECT * FROM contacts WHERE last_name = '{}'".format(search))
                lister()
                pending_response = False

            elif choice == 3:
                search = input("\nInsert the Address That You Want to Search: ")
                c.execute("SELECT * FROM contacts WHERE address = '{}'".format(search))
                lister()
                pending_response = False

            elif choice == 4:
                search = input("\nInsert the Contact That You Want to Search: ")
                c.execute("SELECT * FROM contacts WHERE contact_number = '{}'".format(search))
                lister()
                pending_response = False

            elif choice == 5:
                pending_response = False
            else:
                print("\nInvalid Choice! Try Again\n")

        except ValueError:
            print("\nChoose an Option")

    conn.commit()
    conn.close()
    pass

def drop_table():
    conn = sqlite3.connect('contactBook.db')
    c = conn.cursor()
    c.execute("DROP TABLE contacts")
    conn.commit()
    conn.close()
    create_database()

def lister():
    global rows, c
    rows = c.fetchall()
    for row in rows:
        print("\n")
        print(row)

def update_contact():

    conn = sqlite3.connect('contactBook.db')
    global rows, c
    c = conn.cursor()
    running = True
    while running:
        try:
            change = int(input("What do you want to change?\n1 - First Name\n2 - Last Name\n3 - Address\n" +
                               "4 - Contact Number\n5 - Nothing/Return"))
            if change == 1:
                alteration = "first_name"
                search = input("Which First Name do you want to change: ")
                update = input("\nInsert the First Name: ")
                running = False

            elif change == 2:
                alteration = "last_name"
                search = input("Which Last Name do you want to change: ")
                update = input("\nInsert the Last Name: ")
                running = False
            elif change == 3:
                alteration = "address"
                search = input("Which Address do you want to change: ")
                update = input("\nInsert the Address: ")
                running = False
            elif change == 4:
                alteration = "contact_number"
                search = input("Which Contact do you want to change: ")
                update = input("\nInsert the Contact's Number: ")
                running = False
            elif change == 5:
                running = False
                pass
            else:
                print("Invalid Option! Try Again\n")
            sql = ('''UPDATE contacts SET "{0}" = "{1}" WHERE "{0}" = "{2}"'''.format(alteration, update, search))
            c.execute(sql)
        except ValueError:
            print("\nChoose an Option")

    conn.commit()
    conn.close()

def delete_entry():
    conn = sqlite3.connect('contactBook.db')
    global rows, c
    c = conn.cursor()

    running = True
    while running:
        try:
            delete = int(input("DELETE ENTRY\nSearch by:\n1 - First Name\n2 - Last Name\n3 - Address\n" +
                                   "4 - Contact Number\n5 - Nothing/Return"))
            if delete == 1:
                target = "first_name"
                search = input("Insert the First Name of the Person that you want to Delete: ")
                running = False
            elif delete == 2:
                target = "last_name"
                search = input("Insert the Last Name of the Person that you want to Delete: ")
                running = False
            elif delete == 3:
                target = "address"
                search = input("Insert the Address of the Person that you want to Delete: ")
                running = False
            elif delete == 4:
                target = "contact_number"
                search = input("Insert the Contact's Number that you want to Delete: ")
                running = False
            elif delete == 5:
                running = False
                pass
            else:
                print("Invalid Option! Try Again\n")
            sql = ('''DELETE FROM contacts WHERE "{0}" = "{1}"'''.format(target, search))
            c.execute(sql)

        except ValueError:
            print("\nChoose an Option")


    conn.commit()
    conn.close()
def menu():
    create_database()
    print("Welcome to the Contact Book!")
    program_running = True

    while program_running:
        try:
            choice = int(input("\n1 - Add a Contact\n2 - Consult\n3 - Update\n4 - Delete\n5 - Exit\n6 - Drop Table\nChoice: "))

            if choice == 1:
                add_contact()
            elif choice == 2:
                search_contact()
            elif choice == 3:
                update_contact()
            elif choice == 4:
                delete_entry()
            elif choice == 5:
                exit()
            elif choice == 6:
                drop_table()
            else:
                print("\nInvalid Choice!")
        except ValueError:
            print("\nChoose an Option")

menu()