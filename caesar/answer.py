class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"
      

    def answer(self):
        key = 0 
        a = open("ciphertext.txt","r")
        for i in a:
        	print (i)
        a.close()

        return (key)

b= Caesar()
print (b.answer())