class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"
        # add attributes if you need more

    def answer(self):
        key = 0 # variable to store the key

        # your algorithm
        data = open(chiper.ciphertext, "r")
        Ascii = 127
        key = 127 - 81
        word = data.read()
        translate = ""
        for x in word:
            code = 0
            code = ord(str(x)) - key
            if (code < 0):
                code += Ascii
            translate += chr(code)
        print(translate) 
        data.close()
        return (key)

    # add methods if you need more

chiper = Caesar()
ans = chiper.answer()

print ("Key to encrypt and decrypt chypertext: ", ans)