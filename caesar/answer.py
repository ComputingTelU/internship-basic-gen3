class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"
        # add attributes if you need more

    def answer(self):
        key = 0 # variable to store the key

        # your algorithm
        data = open (self.ciphertext,"r");
        for x in data.read():
        	i = ord(x)-key
        	if (i<0):
        		i += 127
        	tmp += chr(i)
        data.close()
 	hasil = Caesar()
 	hasil.answer()
    # add methods if you need more