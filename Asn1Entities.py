from dataclasses import dataclass


@dataclass
class SignFile:
    hash: int
    publicExponent: int
    module: int


@dataclass
class EncryptedFile:
    cipherText: bytes
    encryptedAesKey: int
    publicExponent: int
    module: int
