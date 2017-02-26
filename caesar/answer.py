class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"
      

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