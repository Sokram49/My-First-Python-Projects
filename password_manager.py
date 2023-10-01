'''
Password manager from Tech With Tim's 5 Mini Python Projects.
I'm not sure how the master password works.
'''

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def key():
    master_pwd = input("Enter master password: ").encode()
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    return base64.urlsafe_b64encode(kdf.derive(master_pwd))

fer = Fernet(key())

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print(f"Username: {user} | Password: {fer.decrypt(pwd).decode()}")

def add():
    user = input("Username: ")
    pwd = input("Password: ").encode()

    with open("passwords.txt", "a") as f:
        f.write(user + "|" + fer.encrypt(pwd).decode() + "\n")

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
