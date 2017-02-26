class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"
      

    def answer(self):
        key = 0 
        a = open("ciphertext.txt","r")
        tmp = 0
        for i in a:
        	a = ord(i) + 5
        	key +=a

        return (key)

b= Caesar()
print (b.answer())