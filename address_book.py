def add_contact(name, number):
    name=name.strip().lower()
    if name in address_book.keys():
        address_book[name].append(number)
        print(f"the number was added to the contact {name}\n")
    else:
        address_book[name]=[number]
        print("contact created\n")
    save_address_book()

def eliminate_number(name, number):
    name=name.strip().lower()
    if name in address_book.keys():
        if number in address_book[name]:
            address_book[name].remove(number)
            print("number eliminated\n")
        else:
            print("number not found\n")
    else:
        print("Contact not found\n")
    save_address_book()

def eliminate_contact(name):
    name=name.strip().lower()
    if name in address_book.keys():
        check=int(input(f"This will eliminate all the numbers associated to the contact {name}, press 1 to confirm\n"))
        if check==1:
            address_book.pop(name)
            print("\ncontact eliminated\n")
        else:
            pass
    else:
        print("contact not found\n")
    save_address_book()

def search(query):
    found=False
    query=query.strip().lower()
    for i in address_book.keys():
        if query in i:
            print(f"{i}: {address_book[i]}\n")
            found=True
        if found==False:
            print("contact not found\n")      
    
def read():
    load_address_book()
    for contact, number in address_book.items():
        print(f"{contact}: {number}\n")

def load_address_book():
    rub = {}
    try:
        with open("address_book.txt", "r") as file:
            for line in file:
                if ":" in line:
                    nome, numero = line.strip().split(":", 1)
                    rub[nome.strip().lower()] = numero.strip()
    except FileNotFoundError:
        pass
    return rub

def save_address_book():
    with open("address_book.txt", "w") as file:
        for nome, numero in address_book.items():
            file.write(f"{nome} : {numero}\n") 

address_book=load_address_book()
choice=0
while choice!=6:
    choice=int(input("choose an option:\n1. add contact\n2. eliminate contact\n3. eliminate number\n4. search contact\n5. see address book\n6. exit\n"))
    match choice:
        case 1:
            name=input("name: ")
            number=input("number: ")
            add_contact(name, number)
        case 2:
            name=(input("name: "))
            eliminate_contact(name)
        case 3:
            name=input("name: ")
            number=input("number: ")
            eliminate_number(name, number)
        case 4:
            query=input("insert the name or part of it: ")
            search(query)
        case 5:
            read()
        case 6:
            pass
        case _:
            print("choose a valid option\n")