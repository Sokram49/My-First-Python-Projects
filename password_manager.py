''' Password manager from Tech With Tim's 5 Mini Python Projects.
    I got the master password to work!!! '''

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def write_key():
    master_pwd = input("Enter master password: ").encode()
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_pwd))
    with open("key.key", "wb") as key_file:
        key_file.write(key + "\n".encode() + salt)
    return key

def load_key():
    master_pwd = input("Enter master password: ").encode()
    with open("key.key", "rb") as f:
        old_key = f.readline().rstrip()
        salt = f.readline().rstrip()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    new_key = base64.urlsafe_b64encode(kdf.derive(master_pwd))
    return new_key if new_key == old_key else quit("Wrong master password")

key = load_key()
f = Fernet(key)

def view():
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print(f"Username: {user} | Password: {f.decrypt(pwd).decode()}")

def add():
    user = input("Username: ")
    pwd = input("Password: ").encode()

    with open("passwords.txt", "a") as file:
        file.write(user + "|" + f.encrypt(pwd).decode() + "\n")

while True:
    mode = input(
        "Would you like to add a new password or view existing ones? (view/add), press q to quit: ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
