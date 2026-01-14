import os
def add_contact(name, number):
    name=name.strip().lower()
    if name in address_book.keys():
        address_book[name].append(number)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"the number was added to the contact {name}\n")
    else:
        address_book[name]=[number]
        os.system('cls' if os.name == 'nt' else 'clear')
        print("contact created\n")
    save_address_book()

def eliminate_number(name, number):
    name=name.strip().lower()
    if name in address_book.keys():
        if number in address_book[name]:
            address_book[name].remove(number)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("number eliminated\n")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("number not found\n")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Contact not found\n")
    save_address_book()

def eliminate_contact(name):
    name=name.strip().lower()
    if name in address_book.keys():
        os.system('cls' if os.name == 'nt' else 'clear')
        check=int(input(f"This will eliminate all the numbers associated to the contact {name}, press 1 to confirm\n"))
        if check==1:
            address_book.pop(name)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\ncontact eliminated\n")
        else:
            pass
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
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
            os.system('cls' if os.name == 'nt' else 'clear')
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
            os.system('cls' if os.name == 'nt' else 'clear')
            name=input("name: ")
            number=input("number: ")
            add_contact(name, number)
        case 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            name=(input("name: "))
            eliminate_contact(name)
        case 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            name=input("name: ")
            number=input("number: ")
            eliminate_number(name, number)
        case 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            query=input("insert the name or part of it: ")
            search(query)
        case 5:
            read()
        case 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            pass
        case _:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("choose a valid option\n")