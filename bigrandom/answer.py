class BigRandom:
    def __init__(self):
        self.data = open("data.txt", "r")
        # add attributes if you need more

    def answer(self):
        noh, suc = 0
        nomor = ''.join([str(x) for x in range(10000)]) # 1234567891011121314...999910000
        for line in self.data.readlines(): 
            noh = noh + len([x for x in line if x == '#']) # count seluruh '#'
            suc = suc + sum([ord(x) for x in line]) # sum dari ascii seluruh karakter

            # @return
            #       noh = count suluruh '#' - 10000, karena '#' disetiap penomoran baris tidak dihitung

            #       ord('#') * 10000             = sum ascii dari '#' untuk setiap penomoran baris
            #       sum([ord(x) for x in nomor]) = sum ascii dari seluruh nomor 1234567891011121314...999910000
        return (noh - 10000, suc - (ord('#') * 10000 + sum([ord(x) for x in nomor])))

big = BigRandom()
a, b = big.answer()
print(a, b)