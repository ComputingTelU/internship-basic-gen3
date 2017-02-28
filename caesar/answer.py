class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"
        # add attributes if you need more

    def answer(self):
        key = 0

        # your algorithm
        self.ciphertext = open("ciphertext.txt", "r+")
        msg = ''.join([chr(ord(x) - key) for x in str(self.ciphertext.readlines())]) # ____ decripting @return decripted string
        print("Hasil decrypt dengan key %d adalah \n %s" % (key, msg)) # __________________ printing out
        self.ciphertext.close() # _________________________________________________________ close data stream
        return (key)

# instantiation
csr = Caesar()
print(csr.answer());