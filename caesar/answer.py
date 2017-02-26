class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"

    def answer(self):
        key = 0
        a = open(self.ciphertext,"r")
        x =""
        for i in a: #mengakes perkata
        	for y in i: #mengakses perhuruf
        		tmp = ord(str(y))-key
        		if (tmp<0):
        			tmp += 127
       		x += chr(tmp)
        print (x)
        return (key)

b= Caesar()
print (b.answer())