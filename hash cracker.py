import hashlib
from hashlib import md5, sha1, sha256, sha384

def get_hash():
    Hash = str(input("Enter a valid hash"))
    return Hash

def Read_PassFile():
    File = open("PassFile.txt","r")
    passwords = [x.strip('\n') for x in File.readlines()]
    File.close()
    return passwords

def Hash_Function(password, Hashed_Pass):
    global Found 
    if md5(password.encode()).hexdigest() == Hashed_Pass:
        Found = True
        print("Found {0} : {1} : md5".format(Hashed_Pass, password))

    elif sha1(password.encode()).hexdigest() == Hashed_Pass:
        Found = True 
        print("Found {0} : {1} : sha1".format(Hashed_Pass. password))

    elif sha256(password.encode()).hexdigest() == Hashed_Pass:
        Found = True 
        print("Found {0} : {1} : 256".format(Hashed_Pass, password))

    elif sha384(password.encode()).hexdigest() == Hashed_Pass:
        Found = True
        print("Found {0} : {1} : sha384".format(Hashed_Pass. password))   

Found = False 
List = Read_PassFile()
while True:
    cmd = str(input("$ "))
    if cmd == "Hash":
        Hash = get_hash()
        for password in List:
            Hash_Function(password, Hash)
            if Found:
                break
        else:
         print("Command Unknown")