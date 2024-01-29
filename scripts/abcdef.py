import pickle
import json
import os
from cryptography.fernet import Fernet
import base64

def fedcba(file) -> base64:
    
    key = Fernet.generate_key()
    f = Fernet(key)
    path = os.path.abspath('.').split("\\")
    path = "\\".join(path)
    with open(path+"\\"+file, 'rb') as jsonfile:
        jf = json.loads(jsonfile.read())
    
    data = pickle.dumps(jf)
    encryptData = f.encrypt(data)

    f = open('config', 'wb')
    f.write(encryptData)
    f.close()
    return key


def abcdef(file, key):

    f = Fernet(key)
    path = os.path.abspath('.').split("\\")
    path = "\\".join(path)
    encrypt = f.decrypt(path+"\\"+file)
    with open(path+"\\"+file, 'rb') as jsonfile:
        jf = json.loads(encrypt)
    
    data = pickle.dumps(jf)
    encryptData = f.encrypt(data)
    
    f = open('config', 'wb')
    f.write(data)
    f.close()
    

