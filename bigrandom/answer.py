class BigRandom:
    def __init__(self):
        self.data = "data.txt"
        # add attributes if you need more

    def answer(self):
        noh = 0 # variable to store number of hashtag
                # ommiting line number's hashtag
        suc = 0 # variable to store sum of character's code in ascii,
                # ommiting line number and its hashtag

        # your algorithm
        my_file = open (self.data, "r")
        for num in my_file:             #masuk num berisi semua data myfile
            while (num[0] != "#"):      #baca sampek ketemu pagar pertama
                num = num[1:]           #sama seperti num++
            num = num [1:]              #pagar pertama diloncati / tidak dibaca -> pindah karakter setelah pagar
            for line in num:            #baca perbaris
                if (line =="#"):        #cek kondisi kalau pagar tambah saja 1 pagarnya
                    noh +=1
                suc += ord(line)        #penambahan karakter setelah pagar pertama
        my_file.close()
        return (noh,suc)
            

ok = BigRandom()
print(ok.answer())
    

    # add methods if you need more
