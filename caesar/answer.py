class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"
        # add attributes if you need more
    def answer(self):
        key = 0 # variable to store the key

        # your algorithm
        sudah = False
        while not sudah:
            tofind = "tugas"
            y = []
            for i in ans.ciphertext:
                w = chr(int((ord(i)+key)%127))
                y.append(w)
            ans.res = "".join(y)
            if tofind in ans.res:
                sudah = True
                return (key)
            key +=1
            
ans = Caesar()
print (ans.answer())
    # add methods if you need more
