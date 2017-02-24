class BigRandom:
    def __init__(self):
        self.data = open("data.txt", "r")
        # add attributes if you need more

    def answer(self):
        noh = 0 # variable to store number of hashtag
                # ommiting line number's hashtag
        suc = 0 # variable to store sum of character's code in ascii,
                # ommiting line number and its hashtag , 393754393
        nomor = ''.join([str(i) for i in range(10000)]) #penomoran di buat list lalu digabungkan 1234567891011..999910000
        
        # your algorithm

        for char in self.data.readlines():
            for i in char:
                if i == '#':
                    noh = noh +1
            for i in char:
                suc = suc+ord(i)

        noh = noh-10000  # pagar diawal, setelah nomor tidak dihitung
        suc = suc - (ord('#') * 10000 + sum([ord(i) for i in nomor])) # jumlah seluruh asci dikurangi pagar awal dan penomoran

        return (noh,suc)

    # add methods if you need more


big = BigRandom()
print(big.answer())