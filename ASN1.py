from asn1 import Decoder, Encoder, Numbers
from Asn1Entities import SignFile, EncryptedFile


class ASN1:
    def encodeSignAns1(self, encrypted_file,sign,hash_,crtificate):
        asn = Encoder()
        asn.start()
        asn.enter(Numbers.Sequence)
        asn.write(b'Encrypted file', Numbers.UTF8String)
        asn.enter(Numbers.Sequence)
        asn.write(encrypted_file, Numbers.UTF8String)
        asn.leave()
        asn.write(b'Hash', Numbers.UTF8String)
        asn.enter(Numbers.Sequence)
        asn.write(hash_, Numbers.UTF8String)
        asn.leave()
        asn.write(b'Signature', Numbers.UTF8String)
        asn.enter(Numbers.Sequence)
        asn.write(sign, Numbers.UTF8String)
        asn.leave()
        asn.write(b'Certificate', Numbers.UTF8String)
        asn.enter(Numbers.Sequence)
        asn.write(crtificate, Numbers.UTF8String)
        asn.leave()
        asn.leave()
        return asn.output()

    def decodeSignAns1(self, asn1Data):
        asn = Decoder()
        asn.start(asn1Data)
        asn.enter()
        asn.read()
        asn.enter()
        encrypted_msg = asn.read()[1]
        asn.leave()
        asn.read()
        asn.enter()
        hash_ = asn.read()[1]
        asn.leave()
        asn.read()
        asn.enter()
        sign = asn.read()[1]
        asn.leave()
        asn.read()
        asn.enter()
        crtificate = asn.read()[1]
        asn.leave()
        return encrypted_msg,hash_,sign,crtificate
