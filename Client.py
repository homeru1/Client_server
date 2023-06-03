import pycades
from ASN1 import ASN1
import socket
import base64


def Encode(msg,num):
    cert = GetCertificate(num)
    hashedData = pycades.HashedData()
    hashedData.Algorithm = pycades.CADESCOM_HASH_ALGORITHM_CP_GOST_3411
    hashedData.Hash(msg)


    envelopedData = pycades.EnvelopedData()
    envelopedData.Content = msg
    envelopedData.Recipients.Add(cert)
    encryptedMessage = envelopedData.Encrypt(pycades.CADESCOM_ENCODE_BASE64)

    signer = pycades.Signer()
    signer.Certificate = cert
    signer.CheckCertificate = True

    signedData = pycades.SignedData()
    signedData.Content = encryptedMessage + hashedData.Value
    signature = signedData.SignCades(signer, pycades.CADESCOM_CADES_BES)

    asn1 = ASN1()
    return asn1.encodeSignAns1(encryptedMessage,signature,hashedData.Value,cert.IssuerName)

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

def GetCertificate(num):
    store = pycades.Store()
    store.Open(pycades.CADESCOM_CONTAINER_STORE, pycades.CAPICOM_MY_STORE, pycades.CAPICOM_STORE_OPEN_MAXIMUM_ALLOWED)
    certs = store.Certificates
    return certs.Item(num+1)

def ReturnCertificates():
    store = pycades.Store()
    store.Open(pycades.CADESCOM_CONTAINER_STORE, pycades.CAPICOM_MY_STORE, pycades.CAPICOM_STORE_OPEN_MAXIMUM_ALLOWED)
    certs = store.Certificates
    cert = []
    if certs.Count == 0:
        cert.append("Certificates with private key not found")
        return cert
    for i in range(certs.Count):
        cert.append(certs.Item(i+1).IssuerName)
    return cert

def start_client(message,host,port):

    client_socket = socket.socket()  
    client_socket.connect((host, port)) 
    client_socket.send(message) 
    client_socket.close()  



if __name__ == "__main__":
    msg = "asdsadsa"
    encoded_msg = Encode(msg,0)
    start_client(encoded_msg)
    #Decode(encoded_msg)