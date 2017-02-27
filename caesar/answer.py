class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"
        # add attributes if you need more

    def answer(self):
        key = 0 # variable to store the key

        # your algorithm
        a = open(self.ciphertext, "r")
        b = ""
        n = 0
        for x in a.read():
            n = ord(str(x))- key
            if (n<0):
                n += 127
            b += chr(n)
        print(b)
        return(key)

    # add methods if you need more
c = Caesar()
print (c.answer())