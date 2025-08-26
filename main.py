import os
import random
import string
from Cryptography.rc4 import CryptoRc4
from ByteStream import ByteStream
request = input("Encrypt or decrypt (e/d) >> ").strip().lower()
if request=="e":
    key = input("Set the key string here (press return to generate a random one) >> ").strip()
    if not key:
        key = ''.join(random.choices(string.ascii_letters + string.digits, k=40))
        print("The randomly generated key is :" + key + " , make sure to keep it")
elif request=="d":
    key = input("Set the key string here >> ").strip()

allFiles = input("Apply to all files in folder? (y/n) >> ").strip().lower()
crypto = CryptoRc4(key)

def encryptFile(file):
    stream = ByteStream(b"")
    with open(file, "rb") as original:
        fileData = original.read()
    data = b"cws"+fileData # ultra coll check for password
    fileExt = file.split('.')[-1]
    encryptedData = crypto.encrypt(data)
    magicBytes = b"\x69\x74crypt"
    stream.writeBytesWithoutLength(magicBytes)
    stream.writeString(fileExt)
    stream.writeVInt(2) # version
    stream.writeBytes(encryptedData, len(encryptedData))
    outputFile = file.replace("." + fileExt, "") + ".cws"
    with open(outputFile, "wb") as encryptedFile:
        encryptedFile.write(stream.getByteArray())
    print(f"Encrypted file saved as: {outputFile}")

def decryptFile(file):
    with open(file, "rb") as encryptedFile:
        fileData = encryptedFile.read()
    stream = ByteStream(fileData)
    magicBytes = stream.readBytes(7)
    if magicBytes == b"SUCCESS":
        print("[ERROR] This file has been encrypted using cws-v1, please use the appropriate decryptor.")
        return
    if not magicBytes == b"\x69\x74crypt":
        print("[ERROR] This file is not a cws-encrypted file!")
        return
    fileExt = stream.readString()
    fileVersion = stream.readVInt()
    if fileVersion != 2:
        print("[ERROR] Incorrect cws version")
        return
    encryptedData = stream.readBytes(stream.readBytesLength())
    decryptedData = crypto.decrypt(encryptedData)
    passwordCheck = decryptedData[:3]
    decryptedData = decryptedData[3:]
    if not passwordCheck == b"cws":
        print("[ERROR] Incorrect decryption password!")
        return
    outputFile = file.replace(".cws", f".{fileExt}")
    with open(outputFile, "wb") as decryptedFile:
        decryptedFile.write(decryptedData)
    print(f"Decrypted file saved as: {outputFile}")

if allFiles == "y":
    for f in os.listdir('.'):
        if request == "e" and os.path.isfile(f) and not f.endswith(".cws"):
            encryptFile(f)
        elif request == "d" and os.path.isfile(f) and f.endswith(".cws"):
            decryptFile(f)
        else:
            print("[WARNING] Invalid choice! Please enter 'e' to encrypt or 'd' to decrypt.")
else:
    file = input("File name >> ").strip()
    if request == "e":
        encryptFile(file)
    elif request == "d":
        decryptFile(file)
    else:
        print("[WARNING] Invalid choice! Please enter 'e' to encrypt or 'd' to decrypt.")
