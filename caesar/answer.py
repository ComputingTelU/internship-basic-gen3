class Caesar:
    def __init__(self):
        self.ciphertext = "ciphertext.txt"
        # add attributes if you need more

    def answer(self):
        key = 0 # variable to store the key

        # your algorithm
        f = open(self.ciphertext, "r")
        text="Tugas" #Di ambil dari clue bahwa ciphertext memuat kata Clue tugas ke prof
        for line in f:
            cond = False
            key = 1
            while not(cond):
                dummy= line
                kanan=[]
                kiri=[]
                for each in dummy:
                    kanan.append(each)
                for i in range(len(kanan)):
                    kanan[i] = chr((int(ord(kanan[i])) + key) % 127)
                for each in dummy:
                    kiri.append(each)
                for i in range(len(kiri)):
                    index=(int(ord(kiri[i])) - key)
                    if index<0:
                        index+=127
                    kiri[i] = chr(index)
                dummy= "".join(kanan)
                if text in dummy:
                    cond=True
                    #buat nge cek hasil dari decode nya
                    print(dummy)
                dummy = "".join(kiri)
                if text in dummy:
                    cond = True
                    # buat nge cek hasil dari decode nya
                    print(dummy)
                else:
                    key+=1
        return (key)
    # add methods if you need more
x= Caesar()
print(x.answer())