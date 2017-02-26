class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"
<<<<<<< HEAD
      

    def answer(self):
        key = 46 
        a = open("ciphertext.txt","r")
        x =""
        for i in a:
        	for y in i:
        		tmp = ord(str(y))-key
        		if (tmp<0):
        			tmp += 127
       		x += chr(tmp)
        print (x)
        return (key)

b= Caesar()
print (b.answer())
=======
        # add attributes if you need more

    def answer(self):
        key = 0 # variable to store the key

        # your algorithm

        return (key)

    # add methods if you need more
>>>>>>> 64e1f92e25e7147b206ac73695e846881e7f9b0d
