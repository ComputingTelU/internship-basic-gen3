class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"
        # add attributes if you need more

    def answer(self):
        key = 0 # variable to store the key

        # your algorithm
        word = open(self.ciphertext, "r")
        new =""
        key = 46
        for x in word.read():
        	i = 0
        	i = ord(str(x)) - key
        	if(i<0):
        		i = i+ 127
        	new += chr(i)
        print(new)
        return(key)
    # add methods if you need more
c = Caesar()
print (c.answer())
#print (word.read())
#text = open("apagitu.txt", "w")
#while(i<127):

# text.close()
# word = open("ciphertext.txt", "r")
# import collections
# s = word.readline()
# print (ord(str(collections.Counter(s).most_common(1))))
	#i+=1
