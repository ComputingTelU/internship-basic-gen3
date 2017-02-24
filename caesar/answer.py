class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"
        # add attributes if you need more

    def answer(self):
        # variable to store the key      

        # your algorithm    

        # add methods if you need more
	    key = 46 #hehe
	    word = open(self.ciphertext,"r")

	    new=""
	    for x in word.read():
	    	i = ord(str(x))-key
	    	if(i<0):
	    		i=i+127
	    	new = new+chr(i)

	    print(new)
	    return(key)
	    
ans = Caesar()
print (ans.answer())