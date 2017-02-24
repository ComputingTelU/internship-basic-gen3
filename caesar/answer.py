class Caesar:
    def __init__(self):
        self.ciphertext = open("ciphertext.txt","r")
        # add attributes if you need more

    @property
    def answer(self):
        key = 0 # variable to store the key

        # your algorithm
        b = False
        while not b:
            to_find = "xxx"
            a = []
            for i in c.ciphertext:
                d = chr(int((ord(i)+key)%127))
                a.append(d)
            c.f = "".join(a)
            if to_find in c.ciphertext:
                b = True
                return (key)
            key +=1
c = Caesar()
print (c.answer())
    # add methods if you need more