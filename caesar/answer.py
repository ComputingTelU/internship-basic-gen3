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
                x=[]
                for each in dummy:
                    x.append(each)
                for i in range(len(x)):
                    x[i] = chr((int(ord(x[i])) + key) % 128)
                dummy= "".join(x)
                if text in dummy:
                    cond=True
                    #buat nge cek hasil dari decode nya
                    #print(dummy)
                else:
                    key+=1
        return (key)
    # add methods if you need more
x= Caesar()
print(x.answer())
#jawaban nya ga ada yang benar, 81 buat tulisan dan kata kata benar, 82 buat spasi enter dan angka angka