class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"
        # add attributes if you need more

    def answer(self):
        key = 0 # variable to store the key

        # your algorithm



    # add methods if you need more
        word = open(self.ciphertext,"r")
        # text = open("apagitu.txt","w");

        new=""
        for x in word.read():
            i=0
            i=ord(str(x))-46
            if(i<0):
                i=i+127
            new += chr(i)
        # text.write(new)
        print(new)
        return (key)
ans = Caesar()
print (ans.answer())
