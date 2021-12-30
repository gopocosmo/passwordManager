from cryptography.fernet import Fernet

# functie de creat cheia, se va folosi o singura data la initializarea listei de parole
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
'''


def load_key():
    file = open("key.key", "rb")
    cheie = file.read()
    file.close()
    return cheie


key = load_key()
fer = Fernet(key)

def add():
    name = input('Cont-Username: ')
    pwd = input("Parola: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Parola:",
                  fer.decrypt(passw.encode()).decode())




while True:
    mode = input(
        "Adauga sau vezi o parola(a, v), sau q to quit? ").lower()
    if mode == "q":
        break

    if mode == "v":
        view()
    elif mode == "a":
        add()
    else:
        print("Invalid.")
        continue
