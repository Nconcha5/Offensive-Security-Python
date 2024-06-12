import hashlib
from hashlib import md5, sha1, sha256, sha384

def get_hash():
    Hash = input("Enter a valid hash: ")
    return Hash

def Read_PassFile():
    with open("PassFile.txt", "r") as File:
        passwords = [x.strip('\n') for x in File.readlines()]
    return passwords

def Hash_Function(password, Hashed_Pass):
    if md5(password.encode()).hexdigest() == Hashed_Pass:
        print(f"Found {Hashed_Pass} : {password} : md5")
        return True
    elif sha1(password.encode()).hexdigest() == Hashed_Pass:
        print(f"Found {Hashed_Pass} : {password} : sha1")
        return True
    elif sha256(password.encode()).hexdigest() == Hashed_Pass:
        print(f"Found {Hashed_Pass} : {password} : sha256")
        return True
    elif sha384(password.encode()).hexdigest() == Hashed_Pass:
        print(f"Found {Hashed_Pass} : {password} : sha384")
        return True
    return False

List = Read_PassFile()

while True:
    cmd = input("$ ").strip()
    if cmd.lower() == "hash":
        Hash = get_hash()
        for password in List:
            if Hash_Function(password, Hash):
                break
        else:
            print("Hash not found.")
    else:
        print("Command Unknown")
