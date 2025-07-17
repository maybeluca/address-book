def addcont(nome, numero):
    nome = nome.strip().lower()
    rubrica[nome] = numero
    salva_rubrica()
    print("Il contatto è stato salvato.")

def remcont(nome_del):
    nome_del = nome_del.strip().lower()
    if nome_del in rubrica:
        rubrica.pop(nome_del)
        salva_rubrica()
        print("Il contatto è stato eliminato.")
    else:
        print("Contatto non trovato.")

def searchcont():
    query = input("Inserisci il nome o parte del nome da cercare: ").strip().lower()
    risultati = {nome: numero for nome, numero in rubrica.items() if query in nome}

    if risultati:
        print("\nContatti trovati:")
        for nome, numero in risultati.items():
            print(f"{nome} : {numero}")
    else:
        print("Nessun contatto corrisponde alla ricerca.")

def updatecont(nome):
    rubrica[nome]=input("inserisci il numero aggiornato")


def carica_rubrica():
    rub = {}
    try:
        with open("rubrica.txt", "r") as file:
            for line in file:
                if ":" in line:
                    nome, numero = line.strip().split(":", 1)
                    rub[nome.strip().lower()] = numero.strip()
    except FileNotFoundError:
        pass
    return rub

def salva_rubrica():
    with open("rubrica.txt", "w") as file:
        for nome, numero in rubrica.items():
            file.write(f"{nome} : {numero}\n") 

rubrica = carica_rubrica()

while True:
    try:
        control = int(input("digitare 1 per aggiungere un contatto, 2 per eliminare un contatto, 3 per leggere la rubrica, 4 per cercare un contatto, 5 per aggiornare un numero, 6 per uscire\n> "))
    except ValueError:
        print("Inserisci un numero valido.")
        continue

    match control:
        case 1:
            nome = input("inserisci il nome: ")
            numero = input("inserisci il numero: ")
            addcont(nome, numero)

        case 2:
            nome_del = input("inserisci il nome del contatto da eliminare: ")
            remcont(nome_del)

        case 3:
            if not rubrica:
                print("Rubrica vuota.")
            else:
                for nome in sorted(rubrica):
                    print(f"{nome} : {rubrica[nome]}")


        case 4:
            searchcont()

        case 5:
            nome=input("inserisci il nome del contatto da aggiornare")
            updatecont(nome)
            print("il contatto è stato aggiornato")

        case 6:
            print("Uscita dal programma.")
            break




        case _:
            print("Comando sconosciuto.")
