
class Cipher:
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OPS = LETTERS + LETTERS.lower() + "0123456789" + "$%&?@. "

    def __init__(self, key):
        self.key = key

    def encryptMessage(self, message: str) -> str:
        return self.__translateMessage(self.key, message, self.OPS, "encrypt")

    def decryptMessage(self, message: str) -> str:
        return self.__translateMessage(self.key, message, self.OPS, "decrypt")

    def __translateMessage(self, key: str, message, OPS, mode) -> str:
        translated = list() # stores the encrypted/decrypted message string
        keyIndex = 0
        # key = key.upper()

        for symbol in message:
            num = OPS.find(symbol)
            if num != -1:
                if mode == 'encrypt':
                    num += OPS.find(key[keyIndex])
                elif mode == 'decrypt':
                    num -= OPS.find(key[keyIndex])
                num %= len(OPS)

                translated.append(OPS[num])
                keyIndex += 1
        
                if keyIndex == len(key):
                    keyIndex = 0
            else:
                translated.append(symbol)

        return ''.join(translated)
 