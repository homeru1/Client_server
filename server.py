import pycades
import socket
from ASN1 import ASN1

def server_program():
    host = socket.gethostname()#"172.29.207.183"
    port = 5000

    server_socket = socket.socket()  
    server_socket.bind((host, port))  
    server_socket.listen(1)
    while True:

        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        message = b''
        while True:
            data = conn.recv(1024)
            message += data
            if not data:
                break
        message = message
        Decode(message)
        conn.close()  # close the connection
        a = int(input("1 break else continue "))
        if a==1:
            break



def Decode(msg):
    asn1 = ASN1()

    encryptedMessage, hash,signature,certificate = asn1.decodeSignAns1(msg)

    envelopedData = pycades.EnvelopedData()
    envelopedData.Decrypt(encryptedMessage)


    hashedData = pycades.HashedData()
    hashedData.Algorithm = pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411
    hashedData.Hash(envelopedData.Content)


    print("Got message:",envelopedData.Content)
    print("Used certificate:",certificate)
    if hashedData.Value == hash:
        print("HASH CHECK OK")
    signedData = pycades.SignedData()
    signedData.VerifyCades(signature, pycades.CADESCOM_CADES_BES)
    print("SIGN CHECK OK")


if __name__ == "__main__":
    server_program()
    #Decode(encoded_msg)