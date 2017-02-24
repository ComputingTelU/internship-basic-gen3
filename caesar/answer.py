class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"
        # add attributes if you need more

    def answer(self):
        key = 0 # variable to store the key

        # your algorithm

        return (key)

    # add methods if you need more
        word = open("ciphertext.txt,","r")
        text = open("apagitu.txt","w");
        i=0
        new=""
        for x in word.readline():
            i=0
            i=ord(str(x))-46
            if(i<0):
                i=i+127
            new += chr(i)
        text.write(new)
        print(new)
        text.close()
        word = open("ciphertext.txt","r")
        import collections
        s = word.readline()
        print(ord(str(collections.Counter(s).most_common(1))))
ans = Caesar()
print (ans.answer())
