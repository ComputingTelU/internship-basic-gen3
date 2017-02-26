class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"
        # add attributes if you need more

    def answer(self):
        self.ciphertext = open("ciphertext.txt", "r+")
        key = int(raw_input(":> ")) # _____________________________________________________ get key from user
        msg = ''.join([chr(ord(x) - key) for x in str(self.ciphertext.readlines())]) # ____ decripting @return decripted string
        print("Hasil decrypt dengan key %d adalah \n %s" % (key, msg)) # __________________ printing out
        self.ciphertext.close() # _________________________________________________________ close data stream
        return (msg)

# instantiation
csr = Caesar()
print(csr.answer());